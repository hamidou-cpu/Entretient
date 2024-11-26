from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('<str:pk>', views.client, name='client'),
    path('creer_client/', views.creer_client, name='creer_client'),
    path('modifier_client/<int:client_id>/', views.modifier_client, name='modifier_client'),
     path('supprimer_client/<int:pk>', views.supprimer_client, name='supprimer_client'),
]