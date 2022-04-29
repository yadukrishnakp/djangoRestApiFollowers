from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=200, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    mobile_number = models.CharField(max_length=50, null=False, blank=False)
    place = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.id)


class FollowUnfollow(models.Model):
    Follow = (
        ('follow', 'Follow'),
        ('unfollow', 'Unfollow')
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    follow_status = models.CharField(max_length=25, choices=Follow)

    def __str__(self):
        return self.follow_status
