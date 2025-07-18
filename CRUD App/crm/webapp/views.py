from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth import aauthenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Record

def home(request):
    
    return render(request, template_name='webapp/home.html')




# - Register
def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully")

            return redirect('login')

    return render(request, template_name='webapp/register.html', context={'form':form})



# - Login
def login_view(request):
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
                # login(request, user)
 
            user = form.get_user()  # Get the logged-in user
            login(request, user)   # Log them in


            return redirect('dashboard')

    
    return render(request, template_name='webapp/login.html', context={'form':form})


# - Logout
def logout_view(request):
    logout(request)
    
    return redirect('home')



# - Dashboard
@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()

    return render(request, template_name='webapp/dashboard.html', context={'records':my_records})


# - Create a record
@login_required(login_url='login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":
        
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Record was created")

            return redirect("dashboard")

    return render(request, template_name='webapp/create-record.html', context={'form':form})


# - Read / View a singular record
@login_required(login_url='login')
def show_individual_record(request, pk):

    record = Record.objects.get(id=pk)
    return render(request, template_name='webapp/record.html', context={'record':record})



# - Update record
@login_required(login_url='login')
def update_record(request, pk):
    
    current_record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=current_record)
    
    if request.method == "POST":
        
        form = UpdateRecordForm(request.POST, instance=current_record)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Record was updated")

            return redirect('dashboard')
        
    return render(request, template_name='webapp/update-record.html', context={"form":form})
    

# - Delete record
@login_required(login_url='login')
def delete_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    record.delete()

    messages.success(request, "Record wasa deleted")

    return redirect('dashboard')