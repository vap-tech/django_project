from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from catalog.models import Product, Category, Feedback

# Create your views here.


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class FeedbackListView(ListView):
    model = Feedback


class ProductDetailView(DetailView):
    model = Product


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('catalog:category')


class ProductCreateView(CreateView):
    model = Product
    fields = (
        'name', 'description', 'preview', 'category', 'price', 'created_date', 'last_modified_date',
    )
    success_url = reverse_lazy('catalog:product')


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('name', 'phone', 'email', 'message')
    success_url = reverse_lazy('catalog:category')
