from django.shortcuts import render

from catalog.function import construct_html, JsonC
from catalog.models import Product


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def product(request, product_pk):
    product_list = Product.objects.get(pk=product_pk)
    context = {
        'object': product_list
    }
    return render(request, 'catalog/product.html', context)


def messages(request):
    return render(request, 'catalog/messages.html')


def contacts(request):
    construct_html()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        message = request.POST.get('text')
        JsonC().to_file([{"name": name, "tel": tel, "email": email, "text": message}])
        construct_html()
    return render(request, 'catalog/contacts.html')
