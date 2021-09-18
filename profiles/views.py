from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
    return render(request,'my-profile.html')

def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile
        }
    return render(request,'profile-view.html', context)
