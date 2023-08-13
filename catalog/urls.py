from django.urls import path
from catalog.views import index, sidebar_css, sidebar_js, home, contacts, messages

urlpatterns = [
    path('', home),
    path('messages/', messages),
    path('contacts/', contacts),
]
