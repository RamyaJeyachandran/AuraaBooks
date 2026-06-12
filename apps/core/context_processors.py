from apps.core.models import Module
from django.db.utils import OperationalError, ProgrammingError

def sidebar_modules(request):
    try:
        all_modules = Module.objects.filter(is_active=True).exclude(
            module_name__in=['E-Commerce', 'Enhanced Export/Import']
        ).order_by('display_order')
        parents = [m for m in all_modules if m.parent_id is None]
        for parent in parents:
            parent.children = [m for m in all_modules if m.parent_id == parent.id]
        return {'sidebar_modules': parents}
    except (OperationalError, ProgrammingError):
        return {'sidebar_modules': []}
