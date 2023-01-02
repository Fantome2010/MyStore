from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'Mystore',
        'is_promo': True
    }
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categorys': ProductCategory.objects.all()
    }

    return render(request, "products/products.html", context)

