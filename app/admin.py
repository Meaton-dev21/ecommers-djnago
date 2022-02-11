from django.contrib import admin
from .models import Book, Product, Category

# Register your models here.

admin.site.register([Category, Book, Product])
