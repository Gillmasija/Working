from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User

# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return render(request, 'accounts/signup.html', {'form': form})
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
                return render(request, 'accounts/signup.html', {'form': form})

            # Save the user without the password being hashed yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Set password securely
            user.save()  # Save user to database

            # Log the user in immediately
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, 'Account created and logged in successfully!')
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'Error logging in after registration.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user with provided credentials
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('dashboard')  # Redirect to dashboard
            else:
                # If authentication fails, show the appropriate error message
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# Dashboard View (just a simple redirect or placeholder)
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
