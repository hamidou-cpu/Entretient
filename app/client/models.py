from django.db import models
class Client(models.Model):
    CATEGORIES = [
        ('Regular', 'Regular'),
        ('VIP', 'VIP'),
        ('Entreprise', 'Entreprise'),
    ]
    
    nom = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    date_creation = models.DateField(auto_now_add=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='Regular')
    notes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nom
