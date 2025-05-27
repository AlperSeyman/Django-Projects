from django.shortcuts import render, redirect
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def home_page(request):
    return render(request, template_name='main/home_page.html', context={'title':'Home'})


def items_page(request):
    # Purchase Operation    
    if request.method == "POST":
        purchased_item = request.POST.get('purchased-item')
        if purchased_item:

            purchased_item_object = Item.objects.get(name=purchased_item)
            purchased_item_object.owner = request.user
            purchased_item_object.save()
            messages.success(request, f'You bought {purchased_item_object.name} for ${purchased_item_object.price}')
        
        return redirect('items_page')

    items = Item.objects.filter(owner=None)
    return render(request, template_name='main/items_page.html', context={'title':'Item', 'items':items})


def register_page(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, f'You have registered your account successfully! Logged in as {user.username}')
            return redirect('home_page') # urls.py ---> url's name
        else:
            messages.error(request, f'Account registration was unsuccessful with errors: {register_form.errors}')
            return redirect('register_page')
        
    return render(request, template_name='main/register_page.html', context={'title':'Register'})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items_page')
        else:
            return redirect('login_page')
        

    return render(request, template_name='main/login_page.html', context={'title':'Login'})

def logout_page(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('home_page')

