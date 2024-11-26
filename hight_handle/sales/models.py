from django.db import models
from django.contrib.auth.models import User
from items.models import Item, Modality
from commands.models import Command
from clients.models import Client

# Create your models here.

class Sale (models.Model):
    sum_sale = models.IntegerField(null=False)
    quantity_sale = models.IntegerField(null=False)
    code_pharmacian = models.ForeignKey(User, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_sale = models.DateTimeField(null=False, auto_now_add=True)

    def __str__ (self):
        return str(self.id)

    class Meta:
        verbose_name = "VENTE"
        verbose_name_plural = "VENTES"



class SaleItem (models.Model):
    remise = models.IntegerField(null=True)
    quantity_sale = models.IntegerField(null=False)
    code_sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    code_command = models.ForeignKey(Command, on_delete=models.CASCADE)
    id_medecine = models.ForeignKey(Item, on_delete=models.CASCADE)
    id_modality = models.ForeignKey(Modality, on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.id)

    class Meta:
        verbose_name = "VENTE MEDICAMENT"
        verbose_name_plural = "VENTES MEDICAMENTS"


class FactureSale (models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    code_sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date_sale = models.DateTimeField(Sale, auto_now_add=True)


    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "BON DE FACTURE"
        verbose_name_plural = "BONS DE FACTURE"

