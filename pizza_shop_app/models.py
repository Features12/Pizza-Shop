from django.db import models
from django.contrib.auth.models import User

class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizza_shop', verbose_name='Владелец')
    name = models.CharField(max_length=100, verbose_name='Имя пиццерии')
    phone = models.CharField(max_length=100, verbose_name='Телефон пиццерии')
    address = models.CharField(max_length=100, verbose_name='Адрес пиццерии')
    logo = models.ImageField(upload_to='pizza_shop_app_logo/', blank=False, verbose_name='Логотип пиццерии')

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_shop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pizza_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name