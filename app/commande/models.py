from django.db import models
from client.models import Client
from produit.models import Produit
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Commande(models.Model):
    STATUS = (
        ('en instance', 'en instance'),
        ('non livré', 'non livré'),
        ('livré', 'livré')
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produits = models.ManyToManyField(Produit, through='CommandeProduit')
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation = models.DateField(auto_now_add=True)


class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_commandee = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.produit.nom} ({self.quantite_commandee})"


class CommandeHistorique(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produits = models.TextField()  # Champ pour stocker les produits et leurs quantités
    statut = models.CharField(max_length=200, null=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_creation = models.DateField(auto_now_add=True)

    @receiver(pre_delete, sender=Commande)
    def sauvegarder_historique_commande(sender, instance, **kwargs):
        produits_liste = [
            f"{commande_produit.produit.nom} ({commande_produit.quantite_commandee})"
            for commande_produit in instance.commandeproduit_set.all()
            if commande_produit.quantite_commandee > 0
        ]
        produits_texte = ', '.join(produits_liste)
        prix_total = sum(
            cp.produit.prix * cp.quantite_commandee
            for cp in instance.commandeproduit_set.all()
        )
        CommandeHistorique.objects.create(
            client=instance.client,
            produits=produits_texte,
            statut=instance.status,
            prix_total=prix_total,
            date_creation=instance.date_creation
        )

