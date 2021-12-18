from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket
import os


def index(request):
    products_in_main = Product.objects.all()
    content = {
        'title': 'Главная',
        'menu': menu,
        'products': products_in_main
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    products_menu = ProductCategory.objects.all()
    if pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__pk=pk)
    content = {
        'title': 'Продукты',
        'menu': menu,
        'products_menu': products_menu,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'menu': menu,
    }
    return render(request, 'mainapp/contact.html', content)


module_dir = os.path.dirname(__file__)

menu = [
    {'href': 'main:index', 'url': 'index', 'name': 'домой'},
    {'href': 'main:products', 'url': 'products', 'name': 'продукты'},
    {'href': 'main:contact', 'url': 'contact', 'name': 'контакты'},
]
