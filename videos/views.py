from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video, Comment
from .forms import CommentForm, VideoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from profiles.models import Profile
from django.contrib.auth.models import User
import datetime
import random

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
    videos = list(Video.objects.all().exclude(id=video.id))
    videos = random.sample(videos,7)
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

@login_required
def subbox(request):
    subbed_chanels = Profile.objects.filter(followers=request.user)
    videos = []
    for i in range(len(subbed_chanels)):
        videos += Video.objects.filter(author = subbed_chanels[i].user)
    context = {
        'subbed_chanels': subbed_chanels,
        'videos':videos,
    }
    return render(request,'subbox.html', context)

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if request.method == 'POST':
        comment.delete()
        return HttpResponseRedirect(reverse('detail', args=[str(comment.video.slug)]))
    context = {
        'comment':comment
    }
    return render(request, 'delete-comment.html', context)

@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.content = comment.content[:-30]
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        comment_form = form.save(commit=False)
        comment_form.content += f"<br>(edited: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})"
        comment_form.save()
        return HttpResponseRedirect(reverse('detail', args=[str(comment.video.slug)]))
    else:
        form = CommentForm(instance=comment)
    context = {
        'comment':comment,
        'form': form
    }
    return render(request, 'edit-comment.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST.get('search')
        videos = Video.objects.filter(title__contains=searched)
        users = User.objects.filter(username__contains=searched)
    context = {
        'searched':searched,
        'videos':videos,
        'users':users,
    }
    return render(request, 'search-results.html', context)

@login_required
def dashboard(request):
    videos = Video.objects.filter(author=request.user)
    context = {
        'videos':videos
    }
    return render(request, 'dashboard.html', context)

@login_required
def edit_video(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)
    form = VideoForm(request.POST or None, instance=video)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detail', args=[str(video.slug)]))
    context = {
        'video': video,
        'form':form
    }
    return render(request, 'edit-video.html', context)

@login_required
def delete_video(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)
    if request.method == 'POST':
        video.delete()
        return redirect('dashboard')
    context = {
        'video':video
    }
    return render(request, 'delete-video.html', context)
