from django.urls import path
from .views import CreateVendorProfileView, CreateProductView

urlpatterns = [
    path('cvp', CreateVendorProfileView.as_view(), name='create-vendor-profile'),
    path('cp', CreateProductView.as_view(), name='create-vendor-product'),
]