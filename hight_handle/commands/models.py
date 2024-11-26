from django.db import models
from django.contrib.auth.models import User
from items.models import Item, Modality

# Create your models here.

class Command (models.Model):
    sum_command = models.IntegerField(null=False)
    code_pharmacian = models.ForeignKey(User, on_delete=models.CASCADE)
    item_length = models.IntegerField(null=False)
    quantity_stored = models.IntegerField(null=False)
    date_livraison = models.DateTimeField(null=False, auto_now_add=True)
    code_pharmacian = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.id)

    class Meta:
        verbose_name = "COMMANDE"
        verbose_name_plural = "COMMANDES"


class Fournisseur (models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    adress = models.CharField(max_length=100, null=False)
    contact = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(null=False, default=0)

    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "FOURNISSEUR"
        verbose_name_plural = "FOURNISSEURS"

class CommandItem (models.Model):
    code_command = models.ForeignKey(Command, on_delete=models.CASCADE)
    id_medecine = models.ForeignKey(Item, on_delete=models.CASCADE)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    quantity_stored = models.IntegerField(null=False)
    price_buy = models.IntegerField(null=False)
    price_sale = models.IntegerField(null=False)
    price_sale_per_item = models.IntegerField(null=False)
    quantity_in_item = models.IntegerField(null=False)
    date_expired = models.DateTimeField(null=False, auto_now_add=True)
    id_modality = models.ForeignKey(Modality, on_delete=models.CASCADE)


    def __str__ (self):
        return self.id_medecine.name.title ()

    class Meta:
        verbose_name = "COMMANDE ARTICLE"
        verbose_name_plural = "COMMANDES ARTICLES"


class FactureCommand (models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    code_command = models.ForeignKey(Command, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(null=False, auto_now_add=True)

   
    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "FACTURE COMMANDE"
        verbose_name_plural = "FACTURES COMMANDES"


class Bon (models.Model):
    date_facture = models.DateTimeField(null=False, auto_now_add=True)
    id_medecine = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)


    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "BON"
        verbose_name_plural = "BONS"


class FactureBon (models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)
    id_bon = models.ForeignKey(Bon, on_delete=models.CASCADE)
    id_fournisseur = models.ForeignKey(Fournisseur, models.CASCADE)


    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "BON DE FACTURE"
        verbose_name_plural = "BONS DE FACTURE"
