from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('dashboard')
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('login')
