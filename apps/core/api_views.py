from rest_framework import viewsets
from .models import Customer, Supplier, Item, Referrer, PremiumQuote
from .serializers import (
    CustomerSerializer, SupplierSerializer, ItemSerializer, ReferrerSerializer,
    PremiumQuoteSerializer
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
