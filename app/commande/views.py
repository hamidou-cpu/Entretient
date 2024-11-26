from django.http import HttpResponse
from .forms import CommandeForm
from django.db.models import Q
from .models import Commande, CommandeProduit, CommandeHistorique
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit



def commande(request):
    return render(request, 'commande/commande.html')


from django.contrib import messages

def ajout_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save()
            produits = form.cleaned_data['produits']
            for produit in produits:
                quantite_commandee = request.POST.get(f'quantite_{produit.id}', 0)
                if produit.quantite_en_stock >= int(quantite_commandee):
                    CommandeProduit.objects.create(
                        commande=commande,
                        produit=produit,
                        quantite_commandee=quantite_commandee
                    )
                    produit.quantite_en_stock -= int(quantite_commandee)
                    produit.save()
                    messages.success(request,'commande ajouter avec succeès')
                else:
                    messages.error(request, f'Quantité insuffisante pour {produit.nom}')
                    commande.delete()  # Annuler la création de la commande si erreur
                    return render(request, 'commande/ajout_commande.html', {'form': form})
            return redirect('/')  # Déplacer cette ligne ici
    else:
        form = CommandeForm()
    return render(request, 'commande/ajout_commande.html', {'form': form})



    
def modification_commande(request, commande_id):
    commande = Commande.objects.get(id=commande_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            # Supprimer les produits associés à la commande existante
            CommandeProduit.objects.filter(commande=commande).delete()
            produits = form.cleaned_data['produits']
            for produit in produits:
                quantite_commandee = request.POST.get(f'quantite_{produit.id}', 0)
                if produit.quantite_en_stock >= int(quantite_commandee):
                    CommandeProduit.objects.create(
                        commande=commande,
                        produit=produit,
                        quantite_commandee=quantite_commandee
                    )
                    produit.quantite_en_stock -= int(quantite_commandee)
                    produit.save()
                else:
                    messages.error(request, f'Quantité insuffisante pour {produit.nom}')
                    return render(request, 'commande/modification_commande.html', {'form': form, 'commande': commande})
            return redirect('/')  # Déplacer cette ligne ici
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'commande/modification_commande.html', {'form': form, 'commande': commande})


    
def supprimer_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    commande.delete()
    return redirect("/")


def vider_historique(request):
    CommandeHistorique.objects.all().delete()
    messages.success(request, 'commande vider avec succeès')
    return redirect('historique_commandes')


from django.shortcuts import render
from .models import CommandeHistorique

def historique_commandes(request):
    # Récupérer toutes les entrées dans CommandeHistorique
    historique_filtre = CommandeHistorique.objects.all()

    # Filtres
    nom_client_query = request.GET.get('nom_client', '')
    statut_commande_query = request.GET.get('statut_commande', '')
    date_creation_debut = request.GET.get('date_creation_debut', '')
    date_creation_fin = request.GET.get('date_creation_fin', '')

    if nom_client_query:
        historique_filtre = historique_filtre.filter(client__nom__icontains=nom_client_query)
    if statut_commande_query:
        historique_filtre = historique_filtre.filter(statut__icontains=statut_commande_query)
    if date_creation_debut and date_creation_fin:
        historique_filtre = historique_filtre.filter(date_creation__range=[date_creation_debut, date_creation_fin])

    # Exclure les produits avec quantité zéro dans le rendu du template
    for entry in historique_filtre:
        produits_filtered = []
        produits_list = entry.produits.split(', ')
        for produit in produits_list:
            # Vérifier si la chaîne peut être décomposée en deux parties
            if ' ' in produit:
                nom, quantite = produit.rsplit(' ', 1)
                try:
                    if int(quantite.strip('()')) > 0:
                        produits_filtered.append(produit)
                except ValueError:
                    # Gérer le cas où la quantité n'est pas un nombre valide
                    pass
            else:
                # Gérer le cas où la chaîne ne peut pas être décomposée
                pass
        entry.produits = ', '.join(produits_filtered)

    # Rendre le template avec les données
    return render(request, 'commande/historique_commandes.html', {'historique': historique_filtre})


def rapport_commandes(request):
    commandes_en_instance = Commande.objects.filter(status='en instance').count()
    commandes_non_livrees = Commande.objects.filter(status='non livré').count()
    commandes_livrees = Commande.objects.filter(status='livré').count()

    context = {
        'commandes_en_instance': commandes_en_instance,
        'commandes_non_livrees': commandes_non_livrees,
        'commandes_livrees': commandes_livrees,
    }

    return render(request, 'commande/rapport_commandes.html', context)


def modifier_statut_commande(request, commande_id):
    if request.method == 'POST':
        commande = get_object_or_404(Commande, id=commande_id)
        nouveau_statut = request.POST.get('status')
        if nouveau_statut in dict(Commande.STATUS):
            commande.status = nouveau_statut
            commande.save()
            messages.success(request, 'Statut de la commande mis à jour avec succès.')
        else:
            messages.error(request, 'Statut invalide.')
    return redirect('/')






