from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required

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
def profile(request):
    return render(request,'profile.html')