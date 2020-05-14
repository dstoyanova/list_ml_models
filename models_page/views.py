from django.shortcuts import render

from .helpers import get_auth_token, get_models


def index(request):
    domain = ""
    username = ""
    password = ""

    auth_token = get_auth_token(domain, username, password)
    models = get_models(domain, auth_token)

    return render(request, 'index.html', locals())
