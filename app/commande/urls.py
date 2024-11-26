from django.contrib import admin
from django.urls import path
from . import views
from .views import rapport_commandes, modifier_statut_commande

urlpatterns = [
   path('', views.commande),
   path('ajout_commande/', views.ajout_commande, name='ajout_commande'),
   path('modifier_commande/<int:commande_id>/', views.modification_commande, name='modifier_commande'),
   path('supprimer_commande/<int:pk>', views.supprimer_commande, name='supprimer_commande'),
   path('historique_commande/', views.historique_commandes, name='historique_commandes'),
   path('vider_historique/', views.vider_historique, name='vider_historique'),
   path('rapport_commandes/', views.rapport_commandes, name='rapport_commandes'),
   path('modifier_statut_commande/<int:commande_id>/', views.modifier_statut_commande, name='modifier_statut_commande'),

  
]

