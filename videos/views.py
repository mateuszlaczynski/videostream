from django.shortcuts import render
from .models import Video

def home(request):
    videos = Video.objects.all()
    context = {
        "videos":videos,
    }
    return render(request,'home.html', context)