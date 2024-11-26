from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('remove<str:id>', views.remove, name='remove'),
    path('category/', views.category, name='category'),
    path('category_edit/<str:id>', views.category_edit, name='category_edit'),
    path('category_add/', views.category_add, name='category_add'),
    path('category_delete/<str:id>', views.category_delete, name='category_delete'),
    path('category_details/', views.category_details, name='category_details'),
    path('statistics/', views.statistics, name='statistics'),
]