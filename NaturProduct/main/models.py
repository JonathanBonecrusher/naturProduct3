from django.db import models
from datetime import datetime
from django.utils import timezone
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

class Employee(models.Model):
    EMPLOYEE_JOB_TITLE_CHOICES = [
        ("ОВ", "Овощи"),
        ("ФП", "Фрукты"),
        ("ГП", "готовая продукция"),
        ("ПР", "Прочее"),
    ]

    employeeId = models.IntegerField(primary_key=True)
    employeeName = models.TextField(max_length=50)
    employeeLogin = models.TextField(max_length=30)
    employeePassword = models.TextField(max_length=20)
    employeeJobTitle = models.TextField(choices=EMPLOYEE_JOB_TITLE_CHOICES)

class User(models.Model):
    EMPLOYEE_JOB_TITLE_CHOICES = [
        ("ОВ", "Овощи"),
        ("ФП", "Фрукты"),
        ("ГП", "готовая продукция"),
        ("ПР", "Прочее"),
    ]

    userId = models.IntegerField(primary_key=True)
    userName = models.TextField(max_length=50)
    userEmail = models.EmailField(max_length=30)
    userLogin = models.TextField(max_length=30)
    userPassword = models.TextField(max_length=20)

class Request(models.Model):
    requestId = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    userEmail = models.EmailField(max_length=30)
    requestText = models.TextField()
