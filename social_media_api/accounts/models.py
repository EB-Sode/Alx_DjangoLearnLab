from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=3000)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical = False, related_name="followed", blank = True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='follows', blank = True)

    
    # def follow(self, user):
    #     """Follow another user"""
    #     if user != self:
    #         self.following.add(user)

    # def unfollow(self, user):
    #     """Unfollow a user"""
    #     self.following.remove(user)

    # def is_following(self, user):
    #     return self.following.filter(id=user.id).exists()

    # def is_followed_by(self, user):
    #     return self.followers.filter(id=user.id).exists()

    # def __str__(self):
    #     return self.username

