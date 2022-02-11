from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    BookListView,
    BookDetailView,
    ProductListView,
    ProductDetailView
)

urlpatterns = [
    path('categorys/', CategoryListView.as_view(), name='categorys'),
    path('categorys/<int:pk>/', CategoryDetailView.as_view(), name='single_category'),

    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='single_book'),

    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='single_product'),

]
