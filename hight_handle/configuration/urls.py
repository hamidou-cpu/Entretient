from django.urls import path, include
from . import views

app_name = 'configuration'

urlpatterns = [
    path('register_user/', views.register_user, name="register"),
    path('register/', views.register, name="register_user"),
    path('', views.connexion, name="login")
]