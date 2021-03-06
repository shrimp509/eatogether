from django.db import models

from account.models import User
from django.utils import timezone


class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.fields.CharField(default="", max_length=50)
    content = models.fields.CharField(default="", max_length=100, blank=True, null=True)
    menu_url = models.fields.URLField(default="", blank=True, null=True)
    max_followers = models.fields.PositiveSmallIntegerField(default=0)
    deadline = models.fields.DateTimeField(default=timezone.now)
    created = models.fields.DateTimeField(default=timezone.now)

    def is_expired(self):
        print("in is_expired: {}, deadline: {}, now: {}".format(
            timezone.now() >= self.deadline, self.deadline, timezone.now())
        )
        return timezone.now() >= self.deadline

    def __str__(self):
        if not self.is_expired():
            return "由{}發起`{}`, {:.1f}分鐘後收單".format(
                self.creator.name,
                self.title,
                (self.deadline - timezone.now()).seconds / 60
            )
        else:
            return "由{}發起`{}`, 已截單, {}發起, {}截止".format(
                self.creator.name,
                self.title,
                self.created.strftime('%Y-%m-%d %H:%M'),
                self.deadline.strftime('%Y-%m-%d %H:%M')
            )


class Item(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.fields.CharField(max_length=50)
    remarks = models.fields.CharField(max_length=100)
    count = models.fields.PositiveSmallIntegerField(default=1)
    created = models.fields.DateTimeField(default=timezone.now)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return "{}點了{}個{}，備註:{}".format(
            self.creator,
            self.count,
            self.product,
            self.remarks
        )
