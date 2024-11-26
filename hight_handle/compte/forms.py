from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
   
    telephone = forms.CharField(max_length=15, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'email', 'telephone', 'password1', 'password2']
