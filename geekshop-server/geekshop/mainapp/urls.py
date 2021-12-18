from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.index, name='index'),
   path('products/category/<int:pk>', mainapp.products, name='products'),
   path('contact/', mainapp.contact, name='contact'),
]