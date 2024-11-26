from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Vérifie si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            # Vérifie si l'utilisateur tente d'accéder à une page autre que la page de connexion ou d'inscription
            if request.path not in [reverse('login'), reverse('signup_url')]:
                # Redirection vers la page de connexion si l'utilisateur n'est pas authentifié
                return redirect('login')  # Redirection vers la page de connexion

        return response
