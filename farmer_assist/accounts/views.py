from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Signup View
def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if email is already registered
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')
        
        # Create new user
        user = User.objects.create_user(username=email, password=password, first_name=name)
        user.save()
        messages.success(request, "Signup successful! Please login.")
        return redirect('login')
    
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if email is registered
        if not User.objects.filter(username=email).exists():
            messages.error(request, "Email not registered!")
            return redirect('login')
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    
    return render(request, 'login.html')

# Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
def home_view(request):
    return render(request, 'home.html')
def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contactus.html')
