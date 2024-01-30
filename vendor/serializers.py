from rest_framework import serializers
from .models import VendorProfile
from product.models import Product

class CreateVendorProfileSerializer(serializers.ModelSerializer):
    vendor_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = VendorProfile
        exclude = ['vendor_status']

    def create(self, validated_data):
        validated_data['vendor_user'] = self.context['request'].user
        return VendorProfile.objects.create(vendor_status='pending', **validated_data)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('product_category', 'vendor_id')

    def create(self, validated_data):
        validated_data['vendor_id'] = self.context['request'].user.vendor_user
        validated_data['product_category'] = self.context['request'].user.vendor_user.vendor_category
        return super().create(validated_data)


