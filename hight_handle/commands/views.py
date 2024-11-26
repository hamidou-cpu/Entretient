from django.shortcuts import render, redirect
from .models import Fournisseur, Command, CommandItem, Fournisseur
from items.models import Item
from .forms import FournisseurForm
from django.db.models import Sum
from datetime import datetime, timedelta


# Create your views here.

def index (request):
    commands = Command.objects.all ()

    context = {
        'commands': commands
    }

    return render (request, 'commands/index.html', context)


def fournisseur (request):
    fournisseurs = Fournisseur.objects.all ()

    context = {
        'fournisseurs': fournisseurs
    }

    return render (request, 'commands/fournisseur.html', context)


def fournisseur_add (request):
    form = FournisseurForm ()

    if request.method == 'POST':
        form = FournisseurForm (request.POST)
        if form.is_valid ():
            form.save ()
            return redirect ('commands:fournisseur')
    context = {
        'form': form
    }

    return render (request, 'commands/fournisseur_add.html', context)


def fournisseur_edit (request, id):
    fournisseur = Fournisseur.objects.get (pk=id)

    form = FournisseurForm (instance=fournisseur)
    if request.method == 'POST':
        form = FournisseurForm (request.POST, instance=fournisseur)
        if form.is_valid ():
            form.save ()
            return redirect ('commands:fournisseur')
    context = {
        'form': form
    }

    return render (request, 'commands/fournisseur_edit.html', context)


def fournisseur_delete (request, id):
    fournisseur = Fournisseur.objects.get (pk=id)
    fournisseur.delete ()
    return redirect ('commands:fournisseur')


def statistics_view(request):
    # Récupérer les commandes groupées par jour
    today = datetime.now().date()
    start_date = today - timedelta(days=30)  # Par exemple, les 30 derniers jours

    commands = Command.objects.filter(date_livraison__date__gte=start_date, date_livraison__date__lte=today)\
        .values('date_livraison__date')\
        .annotate(total_sum_command=Sum('sum_command'))\
        .order_by('date_livraison__date')

    # Préparer les données pour Chart.js
    dates = [command['date_livraison__date'].strftime('%d %b') for command in commands]
    commands_data = [command['total_sum_command'] for command in commands]

    context = {
        'dates': dates,
        'commands_data': commands_data,
        'commands': commands,
    }
    return render(request, 'commands/statistics.html', context)

def see_more (request, id):
    commands_items = CommandItem.objects.filter (code_command = id)

    context = {
        'commands_items': commands_items
    }

    return render (request, 'commands/see_more.html', context)


def add (request):
    items = Item.objects.all ()
    fournisseurs = Fournisseur.objects.all ()

    context = {
        'items': items,
        'fournisseurs': fournisseurs
    }

    return render (request, 'commands/add.html', context)


def edit (request, id):
    context = {

    }

    return render (request, 'commands/edit.html', context)