from django.db import models
from everyco_backend.utils import BaseModel
from vendor.models import VendorProfile
from everyco.models import ProductCategory


# Create your models here.

class Product(BaseModel):
    vendor_id = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
