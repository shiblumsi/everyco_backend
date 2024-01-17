from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('r', UserRegistrationView.as_view(), name='register'),
    path('l', UserLoginView.as_view(), name='login')
]