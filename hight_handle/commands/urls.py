from django.urls import path
from . import views


app_name = 'commands'

urlpatterns = [
    path('', views.index, name='index'),
    path('fournisseur/', views.fournisseur, name='fournisseur'),
    path ('fournisseur_add/', views.fournisseur_add, name='fournisseur_add'),
    path ('fournisseur_edit/<str:id>', views.fournisseur_edit, name="fournisseur_edit"),
    path ('fournisseur_delete/<str:id>', views.fournisseur_delete, name="fournisseur_delete"),
    path ('statistics/', views.statistics_view, name="statistics"),
    path ('see_more/<str:id>', views.see_more, name="see_more"),
    path ('add/', views.add, name="add"),
    path ('edit/<str:id>', views.edit, name="edit"),
]