from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UpdateProfile, UpdateUser
from django.contrib import messages
from .forms import CreateProfile
from .models import Profile


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUser(request.POST, instance=request.user)
        p_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Information has been updated successfully')
            return redirect('profile')
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(request.FILES, instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    path = 'users/profile.html'
    return render(request, path, context)


def register(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created successfully for {username}. Please, proceed to Login ')
            return redirect('home')

    else:
        form = CreateProfile()

    path = 'users/register.html'
    return render(request, path, {'form': form})

