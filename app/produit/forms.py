from django import forms
from .models import Produit
from .models import Tag

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'quantite_en_stock', 'tag', 'image', 'description']



class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nom']