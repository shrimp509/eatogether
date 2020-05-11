# Generated by Django 3.0.3 on 2020-05-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='content',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='menu_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]