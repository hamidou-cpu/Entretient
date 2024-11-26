from django import forms
from items.models import Modality, Item
from clients.models import Client 

class SaleAddForm (forms.Form):

    modality = forms.ModelChoiceField (queryset=Modality.objects.all (), empty_label="Choississez une modalité", error_messages={"required": "Champ requis"})
    item = forms.ModelChoiceField(queryset=Item.objects.all (), empty_label="Choississez un produit", error_messages={"required": "Champ requis"})
    quantity_sale = forms.IntegerField (min_value=1)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'adress']
