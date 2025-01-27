from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .registration_form import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data.get('phone_number', '')
            birth_date = form.cleaned_data.get('birth_date', None)

            # Create a new user
            user= User.objects.create_user(username=username, email=email, password=password)
        
            messages.success(request, "Registration successful! Please log in.")
        else:
            # Form errors will automatically be displayed in the template
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
