from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated', 'product_code']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'product_code']
    prepopulated_fields = {'slug': ('name',)}