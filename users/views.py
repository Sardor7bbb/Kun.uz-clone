# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            messages.success(request, 'Siz yaxshi royxatdan otdingiz :')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/register.html', {'form': form})


