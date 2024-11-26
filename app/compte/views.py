from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def compte(request):
    return render(request, 'compte/compte.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Vous pouvez ajouter ici une redirection vers la page de connexion ou la page d'accueil
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'compte/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Rediriger l'utilisateur vers la page de profil, par exemple
            return redirect('/')
        else:
            # Gérer les cas d'erreur d'authentification, comme afficher un message d'erreur
            return render(request, 'compte/login.html', {'error_message': 'Identifiants incorrects'})
    else:
        return render(request, 'compte/login.html')

def user_logout(request):
    logout(request)
    # Rediriger l'utilisateur vers la page d'accueil, par exemple
    return redirect('login')



