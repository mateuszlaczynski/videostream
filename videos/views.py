from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video, Comment
from .forms import CommentForm, VideoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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
            return HttpResponseRedirect(reverse('detail', args=[str(video.slug)]))
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
def like(request, id):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))
    video.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(video.slug)]))

@login_required
def dislike(request, id):
    video = get_object_or_404(Video, id=request.POST.get('video_id'))
    video.likes.remove(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(video.slug)]))


@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return HttpResponseRedirect(reverse('detail', args=[str(video.slug)]))
    else:
        form = VideoForm()
    context = {
        'form': form
    }
    return render(request,'add-video.html', context)


