from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pharmacy

class PharmacyForm (ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'


class PharmacianRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Ajouter la classe form-control aux champs du formulaire
        for field_name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.TextInput) or isinstance(widget, forms.EmailInput) or isinstance(widget, forms.PasswordInput):
                widget.attrs.update({'class': 'form-control mb-3 text-center'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
