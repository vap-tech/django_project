from django.urls import path

from users.views import CountryCreateView, CountryListView, CountryUpdateView, CountryDetailView, CountryDeleteView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('country/create/', CountryCreateView.as_view(), name='country-create'),
    path('country/<int:pk>/update/', CountryUpdateView.as_view(), name='country-update'),
    path('country/<int:pk>/delete/', CountryDeleteView.as_view(), name='country-delete'),
    path('country/list/', CountryListView.as_view(), name='country-list'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
]
