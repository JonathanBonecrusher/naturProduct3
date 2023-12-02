from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from shop.models import Product, Request, Order, OrderProduct
from .models import User, Employee
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']
    model = Employee


admin.site.register(Product)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Request)
admin.site.register(Order)
admin.site.register(OrderProduct)

