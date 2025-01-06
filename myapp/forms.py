from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    class Meta():
        model = User
        fields = ['username', 'email', 'phone', 'category']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-3'}),
            'phone':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'category':forms.Select(attrs={'class':'select'})
        }

class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))