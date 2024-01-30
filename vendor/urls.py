from django.urls import path
from .views import CreateVendorProfileView

urlpatterns = [
    path('cvp', CreateVendorProfileView.as_view(), name='create-vendor-profile')
]