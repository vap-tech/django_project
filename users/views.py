from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from users.forms import CountryForm, UserRegisterForm, UserProfileForm
from users.models import Country, User


# Country


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('users:country-list')


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('users:country-list')


class CountryDeleteView(DeleteView):
    model = Country
    success_url = reverse_lazy('users:country-list')


class CountryDetailView(DetailView):
    model = Country


class CountryListView(ListView):
    model = Country


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
