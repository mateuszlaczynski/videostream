from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from videos.models import Video
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignUpForm()
    context = {
        'form': form
    }
    return render(request,'signup.html', context)

@login_required
def my_profile(request):
    videos = Video.objects.filter(author=request.user).order_by('-date')
    context = {
        'videos':videos,
        }
    return render(request,'my-profile.html', context)

def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = get_object_or_404(Profile, user=user)
    videos = Video.objects.filter(author=user)
    context = {
        'profile': profile,
        'videos':videos,
        }
    return render(request,'profile-view.html', context)

@login_required
def follow(request, id): 
    profile = get_object_or_404(Profile, id=request.POST.get('profile_id'))
    if profile.user != request.user:
        profile.followers.add(request.user)
    return HttpResponseRedirect(reverse('profile-view', args=[str(profile.user.username)]))
 
