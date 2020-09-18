from django.urls import reverse
from django.test import Client, RequestFactory


def get_response(page, arguments=[]):
    if arguments:
        url = reverse(page, args=arguments)
    else:
        url = reverse(page)
    client = Client()
    response = client.get(url)
    return response

def post_response(page, parameters={}):
    url = reverse(page)
    client = Client()
    response = client.post(url, parameters)
    return response

def post_request(page, parameters={}):
    url = reverse(page)
    factory = RequestFactory()
    request = factory.post(url, parameters)
    return request
