from django.shortcuts import render
from .models import VendorProfile
from rest_framework.generics import CreateAPIView
from .serializers import CreateVendorProfileSerializer
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