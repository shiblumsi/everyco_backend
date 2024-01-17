from django.db import models
from everyco_backend.utils import BaseModel

class ProductCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name