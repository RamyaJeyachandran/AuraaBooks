from rest_framework import serializers
from .models import Customer, Supplier, Item, Referrer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ReferrerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referrer
        fields = '__all__'
