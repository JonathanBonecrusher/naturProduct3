from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return render(request, 'mainContent.html')

def loginPageView(request):
    return render(request, 'login.html')
# Create your views here.
