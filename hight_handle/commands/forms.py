from django.forms import ModelForm
from .models import Fournisseur


class FournisseurForm (ModelForm):

    class Meta:
        model = Fournisseur
        fields = ['name', 'adress', 'contact']