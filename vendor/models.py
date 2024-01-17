from django.db import models
from everyco_backend.utils import BaseModel
from everyco.models import ProductCategory
from account.models import CustomUser


class VendorProfile(BaseModel):
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    )
    vendor_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=255)
    vendor_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    vendor_status = models.CharField(max_length=20, choices=STATUS)
    
    #vendor_logo = models.ImageField(upload_to='vendor_logos/', null=True, blank=True)
    #contact_person = models.CharField(max_length=255)
    #email = models.EmailField()
    #phone_number = models.CharField(max_length=20)
    #business_address = models.TextField()
    
    
    # website = models.URLField(null=True, blank=True)
    # business_description = models.TextField()
    # social_media_links = models.TextField(null=True, blank=True)
    # payment_details = models.TextField()
    # shipping_information = models.TextField()
    # return_policy = models.TextField()
    # product_categories = models.TextField()
    # accepted_payment_methods = models.TextField()
    # tax_id_number = models.CharField(max_length=20)
    # vendor_status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending Approval')])
    # average_rating = models.FloatField(default=0.0)
    # reviews = models.TextField(null=True, blank=True)
    # joining_date = models.DateField(auto_now_add=True)
    # subscription_plan = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.vendor_name