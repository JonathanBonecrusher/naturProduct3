from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def Products_home(request):
    cat = Product.cat_names
    product = Product.objects.all()
    context = {
        'product': product,
        'category': cat
    }
    return render(request, 'mainContent.html', context)
class ProductPageView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'productPage.html'

