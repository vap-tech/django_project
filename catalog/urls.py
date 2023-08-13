from django.urls import path
from catalog.views import home, contacts, messages

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('messages/', messages, name='messages'),
    path('contacts/', contacts, name='contacts'),
]
