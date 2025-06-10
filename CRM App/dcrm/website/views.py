from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record


def home_page(request):

    records = Record.objects.all() # fetch all records


    # Check to see if the logging in 
    # Login Part
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In")
            return redirect('home_page')
        else:
            messages.error(request, "There Was An Error Logging, Please Try Again")
            return redirect('home_page')
    else:
        return render(request, template_name='home_page.html', context={'title':'Home', 'records':records})

# register 
def register_user(request):
    
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # Authenticate and Login
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home_page')
    else:
        register_form = RegisterForm()
        return render(request, template_name='register_page.html', context={'title':'Register', 'register_form':register_form})
    
    return render(request, template_name='register_page.html', context={'title':'Register', 'register_form':register_form})
    
    



# log out 
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home_page')



# show individual record page
def customer_record(request, pk):
    if request.user.is_authenticated: # check user login
        customer_record = Record.objects.get(id=pk) # Look up record
        return render(request, template_name="customer_record.html", context={'title':'Customer Info','customer_record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page..")
        return redirect('home_page')
    

# delete record
def delete_record(request,pk):
    if request.user.is_authenticated: # check user login
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home_page')
    else:
        messages.success(request, "You Must Be Logged In To Do..")
        return redirect('home_page')
    


# add new record
def add_record(request):
    if request.user.is_authenticated:
        add_record_form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if add_record_form.is_valid():
                add_record_form.save()
                messages.success(request,"Record Added")
                return redirect('home_page')
        return render(request, template_name="add_record.html", context={'title':'Add Customer', 'add_record_form':add_record_form})
    else:
        messages.success(request, "You Must Be Logged In To Do..")
        return redirect('home_page')
    

# update record
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        updated_record_form = AddRecordForm(request.POST or None, instance=current_record) # pre-fill form fields.
        if updated_record_form.is_valid():
            updated_record_form.save()
            messages.success(request,"Record Updated")
            return redirect('home_page')
        return render(request, template_name="update_record.html", context={"title":"Update Record", 'updated_record_form':updated_record_form})
    else:
        messages.success(request, "You Must Be Logged In To Do..")
        return redirect('home_page')
        