from rest_framework import viewsets
from .models import Customer, Supplier, Item, Referrer, PremiumQuote, Warehouse
from .serializers import (
    CustomerSerializer, SupplierSerializer, ItemSerializer, ReferrerSerializer,
    PremiumQuoteSerializer, WarehouseSerializer
)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ReferrerViewSet(viewsets.ModelViewSet):
    queryset = Referrer.objects.all()
    serializer_class = ReferrerSerializer

class PremiumQuoteViewSet(viewsets.ModelViewSet):
    queryset = PremiumQuote.objects.all().order_by('-id')
    serializer_class = PremiumQuoteSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        queryset = Warehouse.objects.all().order_by('-id')
        status_filter = self.request.query_params.get('status', None)
        if status_filter == 'active':
            queryset = queryset.filter(is_active=True)
        elif status_filter == 'inactive':
            queryset = queryset.filter(is_active=False)
        return queryset
