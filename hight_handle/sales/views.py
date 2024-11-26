from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from .models import Sale, SaleItem
from items.models import Item
from .forms import SaleAddForm
from clients.models import Client
from commands.models import CommandItem, Command
from django.db.models import Sum
from datetime import datetime, timedelta

# Create your views here.

# Implementation of all functionnalies of sales

def add_panier(request, produit_id):
    item = get_object_or_404(Sale, id=produit_id)
    quantity = request.POST.get('quantity_sale', 1)
    panier = request.session.get('panier', {})

    if produit_id in panier:
        panier[produit_id] += int(quantity)
    else:
        panier[produit_id] = int(quantity)

    request.session['panier'] = panier
    return redirect('sales:add')

def show_panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0

    for produit_id, quantity in panier.items():
        item = get_object_or_404(CommandItem, id=produit_id)
        montant_sale = item.price_sale * quantity
        produits.append({
            'item': item,
            'quantity': quantity,
            'montant_sale': montant_sale,
        })
        total += montant_sale

    return render(request, 'sales/add.html', {'produits': produits, 'total': total})

def confirm_sale(request):
    panier = request.session.get('panier', {})
    client_id = request.POST.get('client_id')
    client = get_object_or_404(Client, id=client_id)

    sale = Sale.objects.create(id_client=client, sum_sale=sum, quantity_sale=quantity) # Code_pharmacian ajouté

    for produit_id, quantity in panier.items():
        item = get_object_or_404(Item, id=produit_id)
        command = get_object_or_404(CommandItem, id=produit_id)
        SaleItem.objects.create(remise=sale, quantity_sale=quantity, id_medecine=item, code_sale=sale, code_command=command, id_modality=item)

        # Mettre à jour le stock
        item.storage_disponible -= quantity
        item.save()

    # Vider le panier après avoir confirmé la vente
    del request.session['panier']

    return redirect('sales:index')

# ___________________________________________________________

def index (request):
    sales = Sale.objects.all ()

    context = { 
        'sales': sales
    }

    return render (request, 'sales/index.html', context)


def add (request):
    # Initialiser le formulaire personnalisé
    sale_form = SaleAddForm ()

    # Récupérer tous les produits
    items = Item.objects.all()

    # Récupérer le panier de la session
    panier = request.session.get('panier', {})

    # Calculer le contenu du panier
    items_panier = []
    total = 0

    # Si c'est une requête POST, on ajoute un produit au panier
    if request.method == 'POST':
        for item_id, quantity in panier.items():
            sale_form = SaleAddForm (request.POST)
            item_id = request.POST.get('item')
            quantity = int(request.POST.get('quantity_sale', 1))

            item = get_object_or_404(Item, id=item_id)
            command_item = get_object_or_404(CommandItem, id_medecine=item_id, quantity_stored__gt = 0)

            total_item = command_item.price_sale * quantity
            items_panier.append({
                'item': item.id,
                'quantity': quantity,
                'price_sale_item': command_item.price_sale,
                'total_item': total_item,
            })
            total += total_item
            print (item_id, quantity, total_item, len(panier))

            # Mettre à jour le panier dans la session
            if item_id in panier:
                panier[item_id] += quantity
            else:
                panier[item_id] = quantity
        
        request.session['panier'] = panier

        # Répondre avec une mise à jour du panier sous forme de JSON
        return JsonResponse({
            'items_panier': items_panier,
            'total': total,
        })

    context = { 
        'form': sale_form,
        'items': items,
        'items_panier': items_panier,
        'panier': True
    }

    return render (request, 'sales/add.html', context)


def edit (request, id):

    context = { 

    }

    return render (request, 'sales/edit.html', context)


def delete (request, id):
    sale = SaleItem.objects.get (pk=id)
    sale.delete ()
    
    return redirect ('sales:index')


def see_more (request, id):
    sales = SaleItem.objects.filter (code_sale=id)

    context = { 
        'sales': sales
    }

    return render (request, 'sales/see_more.html', context)


def statistics_view(request):
    # Récupérer les ventes groupées par jour
    today = datetime.now().date()
    start_date = today - timedelta(days=30)  # Par exemple, les 30 derniers jours

    sales = Sale.objects.filter(date_sale__date__gte=start_date, date_sale__date__lte=today)\
        .values('date_sale__date')\
        .annotate(total_sales=Sum('sum_sale'))\
        .order_by('date_sale__date')

    # Préparer les données pour Chart.js
    dates = [sale['date_sale__date'].strftime('%d %b') for sale in sales]
    sales_data = [sale['total_sales'] for sale in sales]

    context = {
        'dates': dates,
        'sales_data': sales_data,
        'sales': sales
    }
    return render(request, 'sales/statistics.html', context)


def statistics_salers (request):

    context = {

    }

    return render (request, 'sales/statistics_salers.html', context)


