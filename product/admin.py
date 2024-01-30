from django.contrib import admin
from .models import Product

# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'vendor_id', 'description']
    # list_filter = ['is_vendor', 'is_customer',]


admin.site.register(Product, ProductModelAdmin)