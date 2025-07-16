from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Register/Create a user
class CreateUserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

# Create record form
class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# Update recod form
class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

        