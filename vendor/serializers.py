from rest_framework import serializers
from .models import VendorProfile


class CreateVendorProfileSerializer(serializers.ModelSerializer):
    vendor_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = VendorProfile
        exclude = ['vendor_status']
        
    def create(self, validated_data):
        validated_data['vendor_user'] = self.context['request'].user
        return VendorProfile.objects.create(vendor_status='pending',**validated_data)