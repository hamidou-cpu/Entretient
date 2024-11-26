from django.forms import ModelForm
from .models import Item, Category


class ItemForm (ModelForm):
   
    class Meta:
        model = Item
        fields = ['name', 'shape', 'id_category', 'id_modality', 'using', 'secondary_repercutions']


class CategoryForm (ModelForm):

    class Meta:
        model = Category
        fields = '__all__'