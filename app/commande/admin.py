from django.contrib import admin
from .models import Commande, CommandeProduit, CommandeHistorique

# Register your models here.

admin.site.register(Commande)
admin.site.register(CommandeProduit)
admin.site.register(CommandeHistorique)

