from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .models import Follow, Message, UserProfile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def Authenticate(request):
    if request.method == "POST":
        if "signup" in request.POST:
            username = request.POST['txt']
            email = request.POST['email']
            number = request.POST['number']
            password = request.POST['pswd']

            # Check if the user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Signup successful! Please login.")

        elif "login" in request.POST:
            email = request.POST['email']
            password = request.POST['pswd']

            # Authenticate user by email
            user = User.objects.filter(email=email).first()
            if user:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.username}!")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid email or password.")
            else:
                messages.error(request, "No account found with this email.")
    
    return render(request, 'authenticate.html')

@login_required(login_url='authenticate')
def search_profile(request):
    query = request.GET.get('query', '')
    if query:
        results = User.objects.filter(
            username__icontains=query
        ) | User.objects.filter(email__icontains=query)

        results = results.exclude(is_superuser=True)
        
        if not results.exists():
            messages.error(request, 'No results found.')
    else:
        results = User.objects.exclude(is_superuser=True)

    # Add the follow status for each user to the context
    follow_status = {}
    if request.user.is_authenticated:
        for user in results:
            follow_status[user.id] = Follow.objects.filter(follower=request.user, following=user).exists()

    return render(request, 'search_result.html', {'results': results, 'follow_status': follow_status})


@login_required(login_url='authenticate')
def Home(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        website = request.POST.get('website')
        github = request.POST.get('github')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')

        profile, created = UserProfile.objects.get_or_create(user=request.user)
        if profile_picture:
            profile.profile_picture = profile_picture
        if address:
            profile.address = address
        if profession:
            profile.profession = profession
        if website:
            profile.website = website
        if github:
            profile.github = github
        if twitter:
            profile.twitter = twitter
        if instagram:
            profile.instagram = instagram
        if facebook:
            profile.facebook = facebook
        profile.save()

        return redirect('home')

    profile = UserProfile.objects.filter(user=request.user).first()

    return render(request, 'home.html', {'profile': profile})

@login_required(login_url='authenticate')
def follow_user(request, user_id):
    if request.user.is_authenticated:
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow == request.user:
            return JsonResponse({'status': 'error', 'message': 'You cannot follow yourself'}, status=400)

        existing_follow = Follow.objects.filter(follower=request.user, following=user_to_follow)

        if existing_follow.exists():
            # Unfollow the user
            existing_follow.delete()
            return JsonResponse({
                'status': 'unfollowed', 
                'follower_count': user_to_follow.followers.count(),
                'message': f'You unfollowed {user_to_follow.username}.'
            })
        else:
            # Follow the user
            Follow.objects.create(follower=request.user, following=user_to_follow)
            return JsonResponse({
                'status': 'followed', 
                'follower_count': user_to_follow.followers.count(),
                'message': f'You followed {user_to_follow.username}.'
            })
    else:
        return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
    
@login_required(login_url='authenticate')
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            user_profile.profile_picture = fs.url(filename)
        
        user_profile.address = request.POST['address']
        user_profile.profession = request.POST['profession']
        user_profile.website = request.POST['website']
        user_profile.github = request.POST['github']
        user_profile.twitter = request.POST['twitter']
        user_profile.instagram = request.POST['instagram']
        user_profile.facebook = request.POST['facebook']
        user_profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('home')
    
    return render(request, 'edit_profile.html', {'user_profile': user_profile})

@login_required(login_url='authenticate')
def live_chat(request, user_id):
    if request.user.is_authenticated:
        receiver = get_object_or_404(User, id=user_id)
        # Get the chat messages between the sender and the receiver
        messages = Message.objects.filter(sender=request.user, receiver=receiver) | \
                   Message.objects.filter(sender=receiver, receiver=request.user)
        messages = messages.order_by('timestamp')

        if request.method == 'POST':
            content = request.POST.get('content')
            file = request.FILES.get('file')  # Get the uploaded file

            if content:
                # Create a new message with text content
                Message.objects.create(sender=request.user, receiver=receiver, content=content)

            if file:
                # Create a new message with the file
                Message.objects.create(sender=request.user, receiver=receiver, file=file)

            return JsonResponse({'status': 'sent'}, status=200)

        return render(request, 'chat.html', {'messages': messages, 'receiver': receiver})

    return redirect('authenticate')

@login_required
def message_box(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        receiver = get_object_or_404(User, id=receiver_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )
        messages.success(request, "Message sent successfully.")

    # Fetch messages involving the current user
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    sent_messages = Message.objects.filter(sender=request.user).order_by('-timestamp')

    return render(request, 'message_box.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
    })


def LogoutPage(request):
    logout(request)
    return redirect('authenticate')
