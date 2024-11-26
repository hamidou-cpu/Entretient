from django import forms

from client.models import Client
from .models import Commande, Produit


class CommandeForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta:
        model = Commande
        fields = ['client', 'status', 'produits']

    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all()
        # Ajouter dynamiquement les champs de quantité pour les produits
        for produit in self.fields['produits'].queryset:
            self.fields[f'quantite_{produit.id}'] = forms.IntegerField(
                label=f'Quantité pour {produit.nom}',
                required=False,
                min_value=0,
                initial=0,
                widget=forms.HiddenInput()  # Cacher le champ jusqu'à ce qu'il soit sélectionné
            )
