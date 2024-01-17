from django.contrib import admin
from .models import CustomUser

class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_superuser','is_staff','is_vendor','is_customer']
    list_filter = ['is_vendor', 'is_customer']
    
admin.site.register(CustomUser, CustomUserModelAdmin)