from django.shortcuts import render


def main(request):
    content = {
        'title': 'Домой',
        'menu': menu,
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'Продукты',
        'menu': menu,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
        'menu': menu,
    }
    return render(request, 'mainapp/contact.html', content)


menu = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'}
]
