from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    video = models.FileField(upload_to="videos")
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="thumbnails")
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id) +"-"+self.title)
        super(Video,self).save()
    
    def get_absolute_url(self):
        return f"watch/{self.slug}"