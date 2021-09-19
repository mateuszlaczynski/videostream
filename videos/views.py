from django.shortcuts import render
from .models import Video, Comment
from .forms import CommentForm, VideoForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
    description_length = len(video.description)
    videos = Video.objects.all()
    comments = Comment.objects.filter(video=video)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.author = request.user
            form.video = video
            form.save()
            return redirect('home')
    else:
        comment_form = CommentForm()
    context = {
        "video": video,
        "videos": videos,
        "description_length":description_length,
        "comments": comments,
        "comment_form":comment_form,
    }
    return render(request,'detail.html', context)


@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return redirect('home')
    else:
        form = VideoForm()
    context = {
        'form': form
    }
    return render(request,'add-video.html', context)