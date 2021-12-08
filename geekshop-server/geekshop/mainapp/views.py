from django.shortcuts import render
from .models import Product, ProductCategory
import os
import json


def main(request):
    products_in_main = Product.objects.all()
    content = {
        'title': 'Главная',
        'menu': menu,
        'products': products_in_main
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products_card = json.load(open(file_path, encoding='utf-8'))
    content = {
        'title': 'Продукты',
        'menu': menu,
        'products_menu': products_menu,
        'products_card': products_card
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
    {'url': 'main', 'name': 'домой'},
    {'url': 'products:index', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'}
]

products_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'}
]