from django.contrib import admin
from django.urls import path
from . import views
from .views import ajouter_produit_et_tag

urlpatterns = [
   path('', views.home, name='accueil'),
   path('liste_produit', views.liste_produits, name='liste_produit'),
   path('produit/<int:id>/', views.detail_produit, name='detail_produit'),
   path('ajouter_produit/', views.ajouter_produit_et_tag, name='ajouter_produit'),
  
   path('access-denied/', views.access_denied, name='access_denied'),
]
