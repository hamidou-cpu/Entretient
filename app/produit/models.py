from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    date_creation = models.DateField(auto_now_add=True)
    quantite_en_stock = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_("Image du produit"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description du produit"))

    def quantite_commandee(self, commande_id):
        from commande.models import Commande
        commande = Commande.objects.get(id=commande_id)
        return commande.produits.through.objects.get(produit_id=self.id, commande_id=commande.id).quantite_commandee

    def __str__(self):
        return self.nom
