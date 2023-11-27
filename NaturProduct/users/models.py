from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    userId = models.IntegerField(primary_key=True)

class Employee(models.Model):
    EMPLOYEE_JOB_TITLE_CHOICES = [
        ("АД", "Администратор"),
        ("МД", "Менеджер доставок"),
    ]
    user = models.OneToOneField(User, models.CASCADE)
    employeeJobTitle = models.TextField(choices=EMPLOYEE_JOB_TITLE_CHOICES)

