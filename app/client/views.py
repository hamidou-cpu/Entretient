from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from .models import Client
from .forms import ClientForm
from django.contrib import messages

def client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    commande_total = commandes.count()
    montant_total = commandes.aggregate(Sum('prix_total'))['prix_total__sum'] or 0
    context = {'client': client, 'commandes': commandes, 'commande_total': commande_total, 'montant_total': montant_total}
    return render(request, 'client/client.html', context)

def creer_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le client a été créé avec succès !")
            return redirect('/')
        else:
            messages.error(request, "Erreur lors de la création du client. Veuillez corriger les erreurs dans le formulaire.")
    context = {'form': form}
    return render(request, 'client/creer_client.html', context)

def modifier_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    form = ClientForm(instance=client)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Les informations du client ont été modifiées avec succès !")
            return redirect('/')
        else:
            messages.error(request, "Erreur lors de la modification du client. Veuillez corriger les erreurs dans le formulaire.")
    
    context = {'form': form}
    return render(request, 'client/modifier_client.html', context)


def supprimer_client(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect("/")