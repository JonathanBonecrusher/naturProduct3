from django.shortcuts import render
from .models import Product

def Products_home(request):
    cat = Product.cat_names
    product = Product.objects.all()
    context = {
        'product': product,
        'category': cat
    }
    return render(request, 'mainContent.html', context)
