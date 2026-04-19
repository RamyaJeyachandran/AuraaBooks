import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_multitenant.models import TenantModel


class BaseModel(models.Model):
    """
    Abstract base model with UUID primary key and timestamps.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True


class TenantBaseModel(TenantModel, BaseModel):
    """
    Abstract base model for tenant-specific data.
    Uses django-multitenant for shared-schema isolation.
    """
    tenant = models.ForeignKey(
        'tenants.Tenant',
        on_delete=models.CASCADE,
        related_name="%(class)s_items"
    )
    tenant_id = 'tenant_id'

    class Meta:
        abstract = True
