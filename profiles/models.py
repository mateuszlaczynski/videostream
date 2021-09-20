from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=2000)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_pictures", default="profile_pictures/default.jpg")
    bio = models.TextField(blank=True, max_length=5000)
    followers = models.ManyToManyField(User, related_name="followers", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def count_followers(self):
        return self.followers.count()

    def save(self, *args, **kwargs):
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        super(Profile, self).save(*args, **kwargs)


