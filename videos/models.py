from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    video = models.FileField(upload_to="videos")
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="thumbnails")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = f"{self.id}/{slugify(self.title)}"
        super(Video,self).save()
