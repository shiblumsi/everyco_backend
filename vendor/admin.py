from django.contrib import admin
from .models import VendorProfile

class VendorProfileModelAdmin(admin.ModelAdmin):
    list_display = ['vendor_user','vendor_name','vendor_category','vendor_status']
    #list_filter = ['is_vendor', 'is_customer']
    
admin.site.register(VendorProfile, VendorProfileModelAdmin)