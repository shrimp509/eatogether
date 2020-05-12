from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

from order.views import new_order


@csrf_exempt
def new_order_in(request: WSGIRequest):
    if request.method == 'POST':
        formatted_data = _format(request.body.decode('utf-8'))

        return _json(status='get POST method request', data_formatted=formatted_data)
    return _json(status='no such method')


def _json(**kwargs):
    return JsonResponse({k: v for k, v in kwargs.items()})


def _format(decoded_request_body: str):
    formatted_data = {}
    for item in decoded_request_body.split('&'):
        item = item.split('=')
        item[1] = urllib.parse.unquote(item[1])
        formatted_data[item[0]] = item[1]
    return formatted_data
