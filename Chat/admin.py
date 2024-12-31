from django.contrib import admin
from Chat.models import Follow, Message, UserProfile

# Register your models here.
admin.site.register(Follow)
admin.site.register(Message)
admin.site.register(UserProfile)