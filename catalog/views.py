from slugify import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Category, Feedback, Blog

# Create your views here.


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class FeedbackListView(ListView):
    model = Feedback


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'created_date', 'is_public', 'views_count',)
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'created_date', 'is_public', 'views_count',)
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        new_url = super().get_success_url()
        new_url += self.object.slug
        return new_url


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')

