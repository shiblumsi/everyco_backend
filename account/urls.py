from django.urls import path
from .views import CustomerRegistrationView, UserLoginView, VendorRegistrationView

urlpatterns = [
    path('cr', CustomerRegistrationView.as_view(), name='customer-register'),
    path('vr', VendorRegistrationView.as_view(), name='vendor-register'),
    path('l', UserLoginView.as_view(), name='login')
]