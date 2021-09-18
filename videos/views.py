from django.shortcuts import render
from .models import Video
from django.shortcuts import get_object_or_404

def home(request):
    videos = Video.objects.all()
    context = {
        "videos":videos,
    }
    return render(request,'home.html', context)

def detail(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)
    video.views = video.views + 1
    video.save()
    context = {
        "video": video,
    }
    return render(request,'detail.html', context)