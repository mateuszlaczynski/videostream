from django.shortcuts import render
from .models import Video, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

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
        "comments": comments,
        "comment_form":comment_form,
    }
    return render(request,'detail.html', context)