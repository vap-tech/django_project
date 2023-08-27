from django.urls import path

from catalog.views import CategoryListView, CategoryCreateView, ProductListView, \
    ProductCreateView, ProductDetailView, FeedbackCreateView, FeedbackListView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('product/', ProductListView.as_view(), name='product'),
    path('messages/', FeedbackListView.as_view(), name='messages'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('feedback-create/', FeedbackCreateView.as_view(), name='feedback-create'),
]
