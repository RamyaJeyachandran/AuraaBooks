import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Module
from django.db import connection

company_code = 'COMP'
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT code FROM public.tbl_company LIMIT 1")
        row = cursor.fetchone()
        if row and row[0]:
            company_code = row[0]
except Exception as e:
    pass

def get_module_code(suffix):
    unique_id = str(uuid.uuid4())[:8]
    return f"{company_code}_{suffix}_{unique_id}".upper()

max_order = Module.objects.filter(parent__isnull=True).order_by('-display_order').first()
max_order_val = max_order.display_order if max_order else 90

modules_to_add = [
    {'name': 'E-Commerce', 'route': '/e-commerce/', 'icon': 'project'},
    {'name': 'Enhanced Export/Import', 'route': '/export-import/', 'icon': 'settings'},
]

for m in modules_to_add:
    if not Module.objects.filter(module_name=m['name']).exists():
        max_order_val += 10
        Module.objects.create(
            module_name=m['name'],
            module_code=get_module_code(m['name'][:3].replace(' ', '').upper()),
            menu_type='menu',
            route_path=m['route'],
            icon_name=m['icon'],
            display_order=max_order_val,
            is_active=True
        )
        print(f"Added {m['name']}")
    else:
        print(f"{m['name']} already exists")
