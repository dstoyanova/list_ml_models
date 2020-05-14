import requests
import json


def get_auth_token(domain_name, username, password):
    url = "http://{}/api/api-token-auth".format(domain_name)
    body = {
        "username": username,
        "password": password,
    }
    r = requests.post(url, data=body)

    if r.status_code == 200:
        return json.loads(r.text)["token"]

    return ""


def get_models(domain_name, auth_token):
    url = "http://{}/api/models/".format(domain_name)
    headers = {
        "Authorization": "Token {}".format(auth_token),
    }
    r = requests.get(url, headers=headers)

    models = []
    if r.status_code == 200:
        models = json.loads(r.text)

    return models
