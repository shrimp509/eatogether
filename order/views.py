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
def follow(request: WSGIRequest):
    """
        request_body:
        {
            "order_id": 1,
            "creator": "Sam",
            "product": "雞排",
            "count": 1,
            "remarks": "胡椒、不要辣"
        }

        response_body:
        {
            "status": "success"
        }
    """
    if request.method == 'POST':
        data_in = json.loads(request.body)

        # check expired
        order = Order.objects.filter(id=data_in['order_id']).first()
        if order is None:
            return _json(status='Failed to follow order', exception='order id not found')
        if order.is_expired():
            return _json(status='Failed to follow order', exception='order expired')

        try:
            item = Item()
            item.order = order
            user = User.objects.filter(name=data_in['creator']).first()
            if user is None:
                user = User()
                user.name = data_in['creator']
            item.creator = user
            item.product = data_in['product']
            item.remarks = data_in['remarks']
            item.count = data_in['count']
            item.save()
        except Exception as e:
            return _json(status='Failed to follow order', exception=str(e), data_in=data_in)
        return _json(status='Create follow item', item_id=item.id, data_in=data_in)
    return _json(status='No such method')


def _json(**kwargs):
    return JsonResponse({k: v for k, v in kwargs.items()})
