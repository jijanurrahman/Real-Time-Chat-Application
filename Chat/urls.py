from django.contrib import admin
from django.urls import path, include
from Chat import views

urlpatterns = [
    path('', views.Authenticate, name='authenticate'),
    path('home', views.Home, name='home'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('chat/<int:user_id>/', views.live_chat, name='live_chat'),
    path('search/', views.search_profile, name='search_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('messages/', views.message_box, name='message_box'),
    path('logout/',views.LogoutPage,name='logout')

]