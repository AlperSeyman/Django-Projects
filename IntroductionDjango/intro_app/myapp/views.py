from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from myapp.models import Feature

# Create your views here.

def home_page(request):
    features = Feature.objects.all()
    return render(request, template_name='index.html', context={'features':features})

def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register_page')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register_page')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('login_page')
        else:
            messages.info(request, "Password Not The Same")
            return redirect('register_page')

    return render(request, template_name='register_page.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login_page')
        
    return render(request, template_name='login_page.html')

def logout(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home_page')

def post_page(request, pk):
    return render(request, template_name='post_page.html', context={'pk':pk})



def counter_page(request):
    posts = [1, 2, 3, 4, 5, 6, 7, 'kobe', 'lebron', 'jordan', 'tesla']
    return render(request, template_name='counter.html', context={'posts':posts})