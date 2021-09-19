from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=2000)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default.jpg")
    bio = models.TextField(blank=True, max_length=5000)

    def __str__(self):
        return self.user.username

