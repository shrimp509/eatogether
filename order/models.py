from django.db import models

from account.models import User

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
class Order(models.Model):
    creator = models.fields.CharField()
    title = models.fields.CharField()
    content = models.fields.CharField()
    menu_url = models.fields.URLField()
    max_followers = models.fields.PositiveIntegerField()
    deadline = models.fields.DateTimeField()

    current_followers = models.ForeignKey(User, on_delete=models.CASCADE)
