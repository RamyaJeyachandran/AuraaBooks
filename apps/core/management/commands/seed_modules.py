import uuid
from django.core.management.base import BaseCommand
from django.db import connection
from apps.core.models import Module

class Command(BaseCommand):
    help = 'Seeds the database with initial modules'

    def handle(self, *args, **kwargs):
        # Fetch company code
        company_code = 'COMP'
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT code FROM public.tbl_company LIMIT 1")
                row = cursor.fetchone()
                if row and row[0]:
                    company_code = row[0]
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Could not fetch company code, defaulting to COMP. Error: {e}"))

        def get_module_code(suffix):
            unique_id = str(uuid.uuid4())[:8]
            return f"{company_code}_{suffix}_{unique_id}".upper()

        modules_data = [
            {
                'name': 'Dashboard',
                'type': 'menu',
                'route': '/',
                'icon': 'dashboard',
                'order': 10,
                'children': []
            },
            {
                'name': 'Masters',
                'type': 'menu',
                'route': None,
                'icon': 'masters',
                'order': 20,
                'children': [
                    {'name': 'Customer', 'route': '/customers/', 'order': 1},
                    {'name': 'Suppliers', 'route': '/suppliers/', 'order': 2},
                    {'name': 'Items', 'route': '/items/', 'order': 3},
                    {'name': 'Referred By', 'route': '/referrers/', 'order': 4},
                    {'name': 'Warehouse', 'route': '/warehouse/', 'order': 5},
                    {'name': 'Branch', 'route': '/branch/', 'order': 6},
                    {'name': 'Franchisee', 'route': '/franchisee/', 'order': 7},
                    {'name': 'Sales Rep', 'route': '/sales-rep/', 'order': 8},
                    {'name': 'Rate Sheet', 'route': '/rate-sheet/', 'order': 9},
                    {'name': 'Stock Journal', 'route': '/stock-journal/', 'order': 10},
                ]
            },
            {
                'name': 'Sales',
                'type': 'menu',
                'route': None,
                'icon': 'sales',
                'order': 30,
                'children': [
                    {'name': 'Quotes', 'route': '/sales/quotes/', 'order': 1},
                    {'name': 'Sales Order', 'route': '/sales/orders/', 'order': 2},
                    {'name': 'Invoice', 'route': '/sales/invoices/', 'order': 3},
                    {'name': 'Delivery challan', 'route': '/sales/delivery-challan/', 'order': 4},
                    {'name': 'Credit Note', 'route': '/sales/credit-note/', 'order': 5},
                    {'name': 'Receipt', 'route': '/sales/receipt/', 'order': 6},
                ]
            },
            {
                'name': 'Purchase',
                'type': 'menu',
                'route': None,
                'icon': 'purchase',
                'order': 40,
                'children': [
                    {'name': 'Purchase Quote', 'route': '/purchase/quotes/', 'order': 1},
                    {'name': 'Purchase Order', 'route': '/purchase/orders/', 'order': 2},
                    {'name': 'Goods Receipt', 'route': '/purchase/goods-receipt/', 'order': 3},
                    {'name': 'Purchase Bill', 'route': '/purchase/bills/', 'order': 4},
                    {'name': 'Payment', 'route': '/purchase/payments/', 'order': 5},
                    {'name': 'Supplier Credit Note', 'route': '/purchase/credit-note/', 'order': 6},
                ]
            },
            {
                'name': 'Expenses',
                'type': 'menu',
                'route': None,
                'icon': 'expenses',
                'order': 50,
                'children': [
                    {'name': 'Credit Expenses', 'route': '/expenses/credit/', 'order': 1},
                    {'name': 'Asset Expenses', 'route': '/expenses/asset/', 'order': 2},
                    {'name': 'Cash Expenses', 'route': '/expenses/cash/', 'order': 3},
                    {'name': 'Reclaim Expenses', 'route': '/expenses/reclaim/', 'order': 4},
                ]
            },
            {
                'name': 'Accounting',
                'type': 'menu',
                'route': None,
                'icon': 'accounting',
                'order': 60,
                'children': [
                    {'name': 'Accounts', 'route': '/accounting/accounts/', 'order': 1},
                    {'name': 'Opening Balance', 'route': '/accounting/opening-balance/', 'order': 2},
                ]
            },
            {
                'name': 'Bank / Cash',
                'type': 'menu',
                'route': '/bank-cash/',
                'icon': 'bank',
                'order': 70,
                'children': []
            },
            {
                'name': 'Project',
                'type': 'menu',
                'route': '/projects/',
                'icon': 'project',
                'order': 80,
                'children': []
            },
            {
                'name': 'Settings',
                'type': 'menu',
                'route': '/settings/',
                'icon': 'settings',
                'order': 90,
                'children': []
            },
            {
                'name': 'E-Commerce',
                'type': 'menu',
                'route': '/e-commerce/',
                'icon': 'project',
                'order': 100,
                'children': []
            },
            {
                'name': 'Enhanced Export/Import',
                'type': 'menu',
                'route': '/export-import/',
                'icon': 'settings',
                'order': 110,
                'children': []
            }
        ]

        Module.objects.all().delete()
        self.stdout.write("Cleared existing modules.")

        for p_data in modules_data:
            parent = Module.objects.create(
                module_name=p_data['name'],
                module_code=get_module_code(p_data['name'][:3].replace(' ', '').upper()),
                menu_type=p_data['type'],
                route_path=p_data['route'],
                icon_name=p_data['icon'],
                display_order=p_data['order'],
                is_active=True
            )
            for c_data in p_data['children']:
                Module.objects.create(
                    module_name=c_data['name'],
                    module_code=get_module_code(c_data['name'][:3].replace(' ', '').upper()),
                    parent=parent,
                    menu_type='submenu',
                    route_path=c_data['route'],
                    display_order=c_data['order'],
                    is_active=True
                )
        self.stdout.write(self.style.SUCCESS('Successfully seeded modules!'))
