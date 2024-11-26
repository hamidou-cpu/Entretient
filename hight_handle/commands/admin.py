from django.contrib import admin
from .models import Command, CommandItem, FactureCommand, Fournisseur, Bon, FactureBon

# Register your models here.

admin.site.register (Command)
admin.site.register (CommandItem)
admin.site.register (FactureCommand)
admin.site.register (Fournisseur)
admin.site.register (Bon)
admin.site.register (FactureBon)