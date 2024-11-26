from django.contrib import admin
from .models import Item, Category, ShapeItem, Modality

# Register your models here.

admin.site.register (Item)
admin.site.register (Category)
admin.site.register (ShapeItem)
admin.site.register (Modality)