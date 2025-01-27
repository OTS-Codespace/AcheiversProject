from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.views import View
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)





@login_required
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # here Update or creates user
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()

        # here will update Profile
        profile.bio = request.POST.get('bio')
        profile.address = request.POST.get('address')
        profile.phone_number = request.POST.get('phone_number')
        if request.FILES.get('profile_image'):  
            profile.profile_image = request.FILES.get('profile_image')
        profile.save()

        return redirect('profile')

    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'profile_edit.html', context)