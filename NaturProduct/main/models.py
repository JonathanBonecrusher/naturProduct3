from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from users.models import User, Employee

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("ОВ", "Овощи"),
        ("ФП", "Фрукты"),
        ("ГП", "готовая продукция"),
        ("ПР", "Прочее"),
    ]

    productId = models.IntegerField(primary_key=True)
    productName = models.TextField(max_length=50)
    productType = models.TextField(choices=PRODUCT_TYPE_CHOICES)
    productCost = models.IntegerField()
    productStatus = models.TextChoices("В наличии", "Не в начличии")
    productDescription = models.TextField()


class Request(models.Model):
    requestId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    userEmail = models.EmailField(max_length=30)
    requestText = models.TextField()

class Order(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ("ОН", "Онлайн оплата"),
        ("КП", "Картой при получении"),
        ("НП", "Наличными при получении"),
    ]
    STATUS_CHOICES = [
        ("ОП", "Оплачен"),
        ("СЗ", "Сбор заказа"),
        ("ДС", "Доставка курьером"),
        ("ДО", "Доставлен"),
    ]

    orderId = models.IntegerField(primary_key=True)
    orderDate = models.DateField(default=timezone.now)
    orderAddress = models.TextField(max_length=50)
    orderCost = models.IntegerField()
    orderPhoneNumber = models.IntegerField()
    orderPayment = models.TextField(choices=PAYMENT_TYPE_CHOICES)
    orderStatus = models.TextField(choices=STATUS_CHOICES)
    orderEmployee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    orderUser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class OrderProduct(models.Model):
    OPId = models.IntegerField(primary_key=True)
    OrderId = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    ProductAmount = models.IntegerField()


