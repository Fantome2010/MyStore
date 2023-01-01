from django.shortcuts import render

def index(request):
    context = {
        'title': 'Mystore',
        'is_promo': True
    }
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Store - Каталог'
    }
    return render(request, "products/products.html", context)
