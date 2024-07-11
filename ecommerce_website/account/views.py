from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('shop:index'))
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('shop:index'))
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('shop:index'))

