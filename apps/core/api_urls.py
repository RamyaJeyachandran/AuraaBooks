from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CustomerViewSet, SupplierViewSet, ItemViewSet, ReferrerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'items', ItemViewSet)
router.register(r'referrers', ReferrerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
