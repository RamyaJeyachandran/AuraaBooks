from django.db import models
from apps.core.models import BaseModel


class Tenant(BaseModel):
    """
    Tenant model to support multi-tenancy.
    Each tenant represents a separate organization/entity.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    domain = models.CharField(max_length=255, unique=True, null=True, blank=True)
    
    # Subscription / Plan info
    plan = models.CharField(
        max_length=50,
        choices=[('basic', 'Basic'), ('pro', 'Pro'), ('enterprise', 'Enterprise')],
        default='basic'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"
