from django.contrib import admin
from .models import ProductCategory

class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name','parent_category','description','image']
    #list_filter = ['is_vendor', 'is_customer']
    
admin.site.register(ProductCategory, ProductCategoryModelAdmin)