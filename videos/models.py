from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1500)
    video = models.FileField(upload_to="videos")
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="thumbnails")
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True, related_name="author")
    likes = models.ManyToManyField(User, blank=True, related_name="video")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id) +"-"+self.title[:40])
        super(Video,self).save()
    
    def get_absolute_url(self):
        return f"/watch/{self.slug}/"
    

class Comment(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=1500)
    video = models.ForeignKey(Video,null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.author}: {self.content[:30]}"
