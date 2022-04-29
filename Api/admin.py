from django.contrib import admin

from .models import Profile, FollowUnfollow

# Register your models here.

admin.site.register(Profile)
admin.site.register(FollowUnfollow)