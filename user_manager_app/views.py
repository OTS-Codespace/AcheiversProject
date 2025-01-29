
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import role_required

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


# views for user roles
@role_required(['instructor'])
def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

@role_required(['student'])
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@role_required(['admin'])
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
# Views for user roles end here

# Views for user registration and login
def Register(request):
    if request.method == 'POST':                                                                                                                                          
        first_name = request.POST.get('fist_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get(date_of_birth)

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
             user_data_has_error = True
             messages.error(request, "Username already exist")

        if User.objects.filter(email=email).exists():
             user_data_has_error = True
             messages.error(request, "Email already exist")

        if len(password) < 5:
           user_data_has_error = True
           messages.error(request, "Password must be at least five characters")
        
        if  user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created")
            return redirect('login')


    return render(request, 'registration_page.html')
# Views for user registration and login ends here



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


    #  logout view 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfuly.')
        return redirect('home')
    else:
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
