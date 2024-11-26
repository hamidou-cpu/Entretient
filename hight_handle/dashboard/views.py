from django.shortcuts import render
from sales.models import SaleItem
from items.models import Item

# Create your views here.

def index (request):
    # Récuperation de la Dernière Vente
    last_sale = SaleItem.objects.last ()
    
    # Récuperation de tous les articles
    items = Item.objects.all ()
    
    
    # Partie Déboggage 
    dump = dir(SaleItem.objects)

    context = {
        'last_sale': last_sale,
        'items': items,
        'dump': dump
    }

    return render(request, 'dashboard/dashboard.html', context)


# views.py

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    is_staff = user.is_staff
    username = user.username
    # telephone = user.telephone
    email = user.email

    context = {
        'is_staff': is_staff,
        'username': username,
        # 'telephone': telephone,
        'email'    : email,
    }

    return render(request, 'dashboard/profile.html', context)