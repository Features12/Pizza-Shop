# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-24 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='pizza_shop_app_logo/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_shop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]