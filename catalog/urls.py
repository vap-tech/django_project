from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import CategoryListView, CategoryCreateView, ProductListView, \
    ProductCreateView, ProductDetailView, FeedbackCreateView, FeedbackListView, BlogListView, \
    BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, ProductDeleteView, ProductUpdateView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('product/', ProductListView.as_view(), name='product'),
    path('messages/', FeedbackListView.as_view(), name='messages'),
    path('blog/', BlogListView.as_view(), name='blog'),

    path('product/<int:pk>/', cache_page(30)(ProductDetailView.as_view()), name='product-detail'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog-detail'),

    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('blog/<str:slug>/update/', BlogUpdateView.as_view(), name='blog-update'),

    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('blog/<str:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),

    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('feedback-create/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('blog-create/', BlogCreateView.as_view(), name='blog-create'),
]
