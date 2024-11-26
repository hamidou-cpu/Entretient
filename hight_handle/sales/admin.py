from django.contrib import admin
from .models import Sale, SaleItem, FactureSale

# Register your models here.

admin.site.register (Sale)
admin.site.register (SaleItem)
admin.site.register (FactureSale)
