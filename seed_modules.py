from apps.core.models import Module

modules_data = {
    'Customer': {
        'Transactions Sales Entry': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Transactions Sales & Purchase Entry': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Sales Rep': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Franchisee': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Stock Keeper': {'view': False, 'add': False, 'edit': False, 'delete': False},
    },
    'Items': {
        'Transactions Sales Entry': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Transactions Sales & Purchase Entry': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Sales Rep': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Franchisee': {'view': True, 'add': False, 'edit': False, 'delete': False},
        'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Stock Keeper': {'view': True, 'add': True, 'edit': True, 'delete': True},
    },
    'Rate Sheet': {
        'Transactions Sales Entry': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Transactions Sales & Purchase Entry': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Sales Rep': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Franchisee': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Stock Keeper': {'view': False, 'add': False, 'edit': False, 'delete': False},
    },
    'Quotes': {
        'Transactions Sales Entry': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Transactions Sales & Purchase Entry': {'view': False, 'add': False, 'edit': False, 'delete': False},
        'Sales Rep': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Franchisee': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Stock Keeper': {'view': False, 'add': False, 'edit': False, 'delete': False},
    },
    'Sales Order': {
        'Transactions Sales Entry': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Transactions Sales & Purchase Entry': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Sales Rep': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Franchisee': {'view': True, 'add': True, 'edit': False, 'delete': False},
        'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
        'Stock Keeper': {'view': False, 'add': False, 'edit': False, 'delete': False},
    }
}

for mod_name, perms in modules_data.items():
    mod, created = Module.objects.get_or_create(module_name=mod_name, defaults={'module_code': mod_name.upper()[:10], 'menu_type': 'menu'})
    mod.template_permissions = perms
    mod.save()
    print(f"Updated {mod_name}")
