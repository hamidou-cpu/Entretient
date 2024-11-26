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
            # Vérifie si l'utilisateur tente d'accéder à une page autre que la page de connexion, de déconnexion ou d'inscription
            if request.path not in [reverse('login'), reverse('logout'), reverse('signup_url')]:
                # Si l'utilisateur n'est pas authentifié, redirige vers la page d'inscription s'il n'a pas de compte
                if not self.user_has_account(request):
                    return redirect('signup_url')  # Redirection vers la page d'inscription
                else:
                    return redirect('login')  # Redirection vers la page de connexion

        return response

    def user_has_account(self, request):
        # Vérifie si l'utilisateur existe dans la base de données
        # En supposant que vous utilisez l'email comme identifiant
        user = User.objects.filter(email=request.POST.get('email')).first()
        return user is not None
