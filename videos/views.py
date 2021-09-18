from django.shortcuts import render
from .models import Video

def home(request):
    videos = Video.objects.all()
    context = {
        "videos":videos,
    }
    return render(request,'home.html', context)

def detail(request, video_slug):
    video = Video.objects.get(slug=video_slug)
    context = {
        "video": video,
    }
    return render(request,'detail.html', context)