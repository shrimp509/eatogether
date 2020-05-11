from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import Order, Item
from account.models import User
import json
import datetime


@csrf_exempt
def new_order(request: WSGIRequest):
    """
        request_body:
        {
            "creator": "Sam",
            "title": "青子菁吃起來",
            "content": "雞排/炸物",
            "menu_url": "google.com",
            "max_followers": 0,
            "deadline_in_min": 20
        }

        response_body:
        {
            "status": "success",
            "order_id": 1
        }
    """
    if request.method == 'POST':
        data_in = json.loads(request.body)
        try:
            order = Order()
            order.creator = User.objects.get(name=data_in['creator'])
            order.title = data_in['title']
            order.content = data_in['content']
            order.menu_url = data_in['menu_url']
            order.max_followers = data_in['max_followers']
            order.deadline = datetime.datetime.now() + \
                             datetime.timedelta(minutes=data_in['deadline_in_min'])
            order.save()
        except Exception as e:
            return _json(status='Failed to create order', exception=str(e))
        return _json(status='Create order', post_id=order.id, data_in=data_in)
    return _json(status='No such method')


@csrf_exempt
def new_order(request: WSGIRequest):
    if request.method == 'POST':
        data_in = json.loads(request.body)
        return _json(status='Yes, I got your POST method request', data_in=data_in)
    return _json(status='No such method')


def _json(**kwargs):
    return JsonResponse({k: v for k, v in kwargs.items()})
