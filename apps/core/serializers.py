from rest_framework import serializers
from .models import Customer, Supplier, Item, Referrer, PremiumQuote, PremiumQuoteItem

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

class PremiumQuoteItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = PremiumQuoteItem
        fields = ['id', 'item_name', 'description', 'sku', 'hsn', 'qty', 'unit', 'rate', 'discount_type', 'discount_value', 'mrp', 'cost_price', 'amount']

class PremiumQuoteSerializer(serializers.ModelSerializer):
    items = PremiumQuoteItemSerializer(many=True)

    class Meta:
        model = PremiumQuote
        fields = [
            'id', 'estimate_no', 'estimate_type', 'estimate_date', 'valid_till', 
            'reference_no', 'customer', 'buyer_order_no', 'buyer_order_date', 
            'section_name', 'sub_total', 'freight', 'packing', 'insurance', 
            'tcs', 'round_off', 'total_amount', 'notes', 'terms', 'bank', 
            'sales_rep', 'project', 'items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        quote = PremiumQuote.objects.create(**validated_data)
        for item_data in items_data:
            PremiumQuoteItem.objects.create(quote=quote, **item_data)
        return quote
