# Generated by Django 3.0.3 on 2020-05-11 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200511_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
