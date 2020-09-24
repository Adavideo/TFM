from django.urls import reverse
from django.test import Client


def get_response(page, arguments=[]):
    url = reverse(page, args=arguments)
    client = Client()
    response = client.get(url)
    return response

def post_response(page, parameters={}, arguments=[]):
    url = reverse(page, args=arguments)
    client = Client()
    response = client.post(url, parameters)
    return response
