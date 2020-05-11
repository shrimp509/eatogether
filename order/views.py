from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

'''
request_body:
{
    "creator": "Sam",
    "title": "青子菁吃起來",
    "content": "雞排/炸物",
    "menu_url": "google.com",
    "max_followers": 0,
    "deadline": 20
}
'''
@csrf_exempt
def new_order(request: WSGIRequest):
    if request.method == 'POST':
        data_in = json.loads(request.body)
        return _json(status='Yes, I got your POST method request', data_in=data_in)
    return _json(status='No such method')


def _json(**kwargs):
    return JsonResponse({k: v for k, v in kwargs.items()})
