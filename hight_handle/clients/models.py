from django.db import models

# Create your models here.

class Client (models.Model):
    name = models.CharField(max_length=100, null=True)
    adress = models.CharField(max_length=100, null=True)
    contact = models.CharField (max_length=50, null=True, default="622 76 87 10") 
    
    def __str__ (self):
        return self.name.title()

    class Meta:
        verbose_name = "CLIENT"
        verbose_name_plural = "CLIENTS"