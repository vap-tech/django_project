from django.shortcuts import render

from catalog.function import construct_html, JsonC

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')


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


def sidebar_css(request):
    return render(request, 'catalog/sidebars.css')


def sidebar_js(request):
    return render(request, 'catalog/sidebars.js')
