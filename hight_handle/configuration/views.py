from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import resolve
from .forms import PharmacianRegisterForm, PharmacyForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Pharmacy
# Create your views here.

def register (request):
    entity_description = Pharmacy.objects.all ()
    form = PharmacyForm()

    if entity_description.count () == 0:
        if request.method == 'POST':
            form = PharmacyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('configuration:register_user')
    else:
        messages.info(request, "Identifiant ou mot de pass invalide")
    
    context = {
        'form': form
    }
    return render(request, 'configuration/register.html', context)

def register_user (request):
    form = PharmacianRegisterForm()
    if request.method == 'POST':
        form = PharmacianRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('configuration:login')

    context = {
        'title': "PERSONNALISATION DU COMPTE ADMINISTRATEUR",
        'form': form
    }
    return render(request, 'configuration/register_pharmacian.html', context)

 
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard:index")
        else:
            messages.error(request, "Identifiant ou mot de passe invalide")

    # Vous pouvez également passer le formulaire de connexion s'il est nécessaire pour votre template
    return render(request, 'configuration/login.html')