from django.urls import path
from catalog.views import home, contacts, messages

urlpatterns = [
    path('', home),
    path('messages/', messages),
    path('contacts/', contacts),
]
