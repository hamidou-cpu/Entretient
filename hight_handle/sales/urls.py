from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('delete/<str:id>', views.edit, name='delete'),
    path('see_more/<str:id>', views.see_more, name='see_more'),
    path('statistics/', views.statistics_view, name='statistics_view'),
    path('statistics_salers/', views.statistics_salers, name='statistics_salers'),
]