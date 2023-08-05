from django.urls import path
from catalog.views import index, sidebar_css, sidebar_js, home, contacts, messages

urlpatterns = [
    path('index.html', index),
    path('', home),
    path('messages.html', messages),
    path('contacts.html', contacts),
    path('sidebars.css', sidebar_css),
    path('sidebars.js', sidebar_js)
]
