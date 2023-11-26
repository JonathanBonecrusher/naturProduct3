from django.contrib import admin
from django.contrib.auth import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Product, Employee, User, Request, Order, OrderProduct
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['employeeName']
    model = Employee


admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(Request)
admin.site.register(Order)
admin.site.register(OrderProduct)

