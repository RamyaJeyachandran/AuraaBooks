from rest_framework import serializers
from .models import Customer, Supplier, Item, Referrer, PremiumQuote, PremiumQuoteItem, Warehouse, EntityBankDetail, EntityShippingAddress

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

class EntityBankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityBankDetail
        exclude = ('entity_type', 'entity_id')

class EntityShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityShippingAddress
        exclude = ('entity_type', 'entity_id')

class WarehouseSerializer(serializers.ModelSerializer):
    bank_details = serializers.SerializerMethodField()
    shipping_addresses = serializers.SerializerMethodField()

    class Meta:
        model = Warehouse
        fields = '__all__'

    def get_bank_details(self, obj):
        banks = EntityBankDetail.objects.filter(entity_type='Warehouse', entity_id=obj.id)
        return EntityBankDetailSerializer(banks, many=True).data

    def get_shipping_addresses(self, obj):
        ships = EntityShippingAddress.objects.filter(entity_type='Warehouse', entity_id=obj.id)
        return EntityShippingAddressSerializer(ships, many=True).data

    def create(self, validated_data):
        request = self.context.get('request')
        bank_details_data = []
        shipping_addresses_data = []
        
        if request and hasattr(request, 'data'):
            bank_details_data = request.data.get('bank_details', [])
            shipping_addresses_data = request.data.get('shipping_addresses', [])
            
        warehouse = super().create(validated_data)
        
        for bank_data in bank_details_data:
            EntityBankDetail.objects.create(entity_type='Warehouse', entity_id=warehouse.id, **bank_data)
            
        for ship_data in shipping_addresses_data:
            EntityShippingAddress.objects.create(entity_type='Warehouse', entity_id=warehouse.id, **ship_data)
            
        return warehouse

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'data'):
            if 'bank_details' in request.data:
                EntityBankDetail.objects.filter(entity_type='Warehouse', entity_id=instance.id).delete()
                for bank_data in request.data.get('bank_details', []):
                    # Remove 'id' if it's there, as we recreate them
                    bank_data.pop('id', None)
                    EntityBankDetail.objects.create(entity_type='Warehouse', entity_id=instance.id, **bank_data)
                    
            if 'shipping_addresses' in request.data:
                EntityShippingAddress.objects.filter(entity_type='Warehouse', entity_id=instance.id).delete()
                for ship_data in request.data.get('shipping_addresses', []):
                    ship_data.pop('id', None)
                    EntityShippingAddress.objects.create(entity_type='Warehouse', entity_id=instance.id, **ship_data)
                    
        return super().update(instance, validated_data)
