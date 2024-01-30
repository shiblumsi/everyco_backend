from django.shortcuts import render

from product.models import Product
from .models import VendorProfile
from rest_framework.generics import CreateAPIView
from .serializers import CreateVendorProfileSerializer, CreateProductSerializer


# Create your views here.

class CreateVendorProfileView(CreateAPIView):
    queryset = VendorProfile.objects.filter()
    serializer_class = CreateVendorProfileSerializer
    
class UpdateVendorProfileView():
    pass

class VendorProfileView():
    pass

class DeleteVendorProfileView():
    pass


#product
class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    # def perform_create(self, serializer):
    #     # print('----------->', self.request.data)
    #     return serializer.save()
