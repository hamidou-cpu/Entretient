from django.db import models

# Create your models here.

class Pharmacy (models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    contact = models.CharField(max_length=100, null=False, unique=True)
    adress = models.CharField(max_length=100, null=False)
    logo = models.CharField(max_length=100, null=False)
    product_key = models.CharField(max_length=100, null=False, unique=True, default="GRAPHIKART_FORMATION_2023")

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "PHARMACIE"
        verbose_name_plural = "PHARMACIES"


# class Pharmacian (models.Model):
#     firstname = models.CharField(max_length=100, null=False)
#     lastname = models.CharField(max_length=100, null=False)
#     pseudo = models.CharField(max_length=100, null=False, unique=True)
#     password = models.CharField(max_length=100, null=False)
#     rule_pharmacian = models.CharField(max_length=100, null=False)
#     mail_pharmacian = models.CharField(max_length=100, null=False, unique=True)
#     photo_pharmacian = models.CharField(max_length=100, null=False)

# #     def __str__ (self):
# #         return self.pseudo.title()

# #     class Meta:
# #         verbose_name = "PHARMACIEN"
# #         verbose_name_plural = "PHARMACIENS"