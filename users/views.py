from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile , User
from Blog_sys.models import FollowRequest


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)
    following_count = FollowRequest.objects.filter(sender=user).count()
    followers_count = FollowRequest.objects.filter(receiver=user).count()

    if FollowRequest.objects.filter(sender=user , receiver=user):
        followers_count = followers_count - 1
        following_count= following_count - 1
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'followers_number' : followers_count,
        'following_number' : following_count,
    }

    return render(request, 'users/profile.html', context)

@login_required
def profile_image(request):
    
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }

    return render(request, 'users/profile_image.html', context)

