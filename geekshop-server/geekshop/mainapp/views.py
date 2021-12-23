from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket
import os


def get_product_category():
    return ProductCategory.objects.all()


def get_basket(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user)


def index(request):
    products_in_main = Product.objects.all()
    content = {
        'title': 'Главная',
        'menu': menu,
        'basket': get_basket(request),
        'products': products_in_main
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk):
    if pk == 0:
        all_products = Product.objects.all()
    else:
        all_products = Product.objects.filter(category__pk=pk)
    content = {
        'title': 'Продукты',
        'menu': menu,
        'products_menu': get_product_category(),
        'products': all_products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукт'
    content = {
        'title': title,
        'menu': menu,
        'products_menu': get_product_category(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'menu': menu,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contact.html', content)


module_dir = os.path.dirname(__file__)

menu = [
    {'href': 'main:index', 'url': 'index', 'name': 'домой'},
    {'href': 'main:products', 'url': 'products', 'name': 'продукты'},
    {'href': 'main:contact', 'url': 'contact', 'name': 'контакты'},
]
