from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import UserSignUpForm, UserEditForm, ProfileEditForm
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
    videos = Video.objects.filter(author=request.user).order_by('date')
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
 
@login_required
def unfollow(request, id): 
    profile = get_object_or_404(Profile, id=request.POST.get('profile_id'))
    if profile.user != request.user:
        profile.followers.remove(request.user)
    return HttpResponseRedirect(reverse('profile-view', args=[str(profile.user.username)]))

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('my-profile')
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)        
        
    context = {
        'profile':profile,
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'edit-profile.html',context)