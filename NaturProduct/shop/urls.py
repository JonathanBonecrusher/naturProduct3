from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products_home, name='home'),
    path('<int:pk>/', views.ProductPageView.as_view(), name='productPage'),
]

