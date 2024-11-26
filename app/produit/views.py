from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from produit.forms import ProduitForm, TagForm
from produit.models import Produit


# Create your views here.

def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    statut = request.GET.get('status')
    client_filter = request.GET.get('client')

    for commande in commandes:
        commande.prix_total = 0
        for cp in commande.commandeproduit_set.all():
            if cp.quantite_commandee > 0:
                commande.prix_total += cp.quantite_commandee * cp.produit.prix

    if statut:
        commandes = commandes.filter(status=statut)
    if client_filter:
        commandes = commandes.filter(client__nom=client_filter)

    context = {'commandes': commandes, 'clients': clients}
    return render(request, 'produit/acceuil.html', context)


def liste_produits(request):
    query = request.GET.get('q')  # Récupère la requête de recherche
    if query:
        produits = Produit.objects.filter(nom__icontains=query)  # Filtre les produits par nom
    else:
        produits = Produit.objects.all()  # Récupère tous les produits si aucune requête
    return render(request, 'produit/liste_produit.html', {'produits': produits})

def detail_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    return render(request, 'produit/detail_produit.html', {'produit': produit})

def ajouter_produit_et_tag(request):
    # Vérification du statut d'équipe
    if not request.user.is_staff:
        return redirect('access_denied')

    if request.method == 'POST':
        produit_form = ProduitForm(request.POST, request.FILES, prefix="produit")
        tag_form = TagForm(request.POST, prefix="tag")

        if 'submit_tag' in request.POST:
            if tag_form.is_valid():
                tag_form.save()
                return redirect('ajouter_produit')  # Pour revenir à la même page après ajout du tag
        elif 'submit_produit' in request.POST:
            if produit_form.is_valid():
                produit_form.save()
                return redirect('liste_produit')  # Remplacez 'liste_produit' par l'URL de redirection appropriée

    else:
        produit_form = ProduitForm(prefix="produit")
        tag_form = TagForm(prefix="tag")

    return render(request, 'produit/ajouter_produit.html', {'produit_form': produit_form, 'tag_form': tag_form})

def access_denied(request):
    return render(request, 'produit/erreur.html', {'message': "Accès interdit"})
