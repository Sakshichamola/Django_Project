from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Member
from .models import Blog


# ✅ Signup View
def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate Passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check for Existing Username & Email
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Create User
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Store in Member Model
        member = Member.objects.create(user=user, full_name=full_name, email=email)
        member.save()

        # Auto-login After Signup
        login(request, user)
        messages.success(request, "Signup successful! You are now logged in.")
        return redirect('index')  # Redirect to home page

    return render(request, 'signup.html')

# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')

# ✅ Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# ✅ Home Page (Only for Logged-in Users)
@login_required
def index_view(request):
    return render(request, 'index.html', {'user': request.user})

@login_required
def update_account_view(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('index')
    return render(request, 'update_account.html')

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    return render(request, 'delete_account.html')


def blog_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get name safely
        title = request.POST.get('title')
        content = request.POST.get('content')

        if name and title and content:  # Ensure all fields exist
            Blog.objects.create(name=name, title=title, content=content)
            return redirect('blog_list')  # Redirect after submission

    return render(request, 'blog_form.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})