from django.db import models

# Create your models here.

class Modality (models.Model):
    modalities = (
        ("Détail", "Détail"), 
        ("Paquet", "Paquet"), 
        ("Détail & Entier", "Détail & Entier")
    )
    title = models.CharField(max_length=100, null=False, unique=True, choices=modalities)

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = "MODALITE"
        verbose_name_plural = "MODALITES"


class Category (models.Model):
    description = models.CharField(max_length=100, null=False)

    def __str__ (self):
        return self.description.title()

    class Meta:
        verbose_name = "CATEGORIE"
        verbose_name_plural = "CATEGORIES"


class ShapeItem (models.Model):
    shape = models.CharField (max_length=100, null=False)

    def __str__ (self):
        return self.shape.title()

    class Meta:
        verbose_name = "FORME ARTICLE"
        verbose_name_plural = "FORME ARTICLES"


class Item (models.Model):
    name = models.CharField(max_length=100, null=False)
    shape = models.ForeignKey (ShapeItem, on_delete=models.CASCADE)
    minimal_storage = models.IntegerField(null=False, default=5)
    storage_disponible = models.IntegerField(null=False, default=0)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    using = models.CharField(null=True, max_length=255)
    secondary_repercutions = models.CharField(null=True, max_length=255)
    id_modality = models.ForeignKey(Modality, on_delete=models.CASCADE)


    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "ARTICLE"
        verbose_name_plural = "ARTICLES"

