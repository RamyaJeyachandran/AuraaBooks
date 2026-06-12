from apps.core.models import Module

# List of modules by group based on Outputbooks
grouped = {
    'Manage': ['Customer', 'Supplier', 'Items', 'Rate Sheet', 'Projects'],
    'Sales': ['Quotes', 'Sales Order', 'Delivery Challan', 'Invoice', 'Retail Invoice', 'Sales Return', 'Receipts'],
    'Purchase': ['Purchase Quotes', 'Purchase Order', 'Purchase Bill', 'Expense / Payment', 'Bill Payment', 'Sup.Credit Note', ' Sup.Debit Note', 'Goods Receipt Note'],
    'Accounting': ['Cash / Bank Book', 'Journal Entry', 'Cash Contra', 'Chart of Accounts', 'Opening Balances'],
    'Inventory': ['Stock Journal', 'Physical Stock', 'Manufacturing Journal', 'Bill of Material'],
}

# General permission for demonstration, similar to what we did earlier
default_perms = {
    'Transactions Sales Entry': {'view': True, 'add': False, 'edit': False, 'delete': False},
    'Accountant': {'view': True, 'add': True, 'edit': True, 'delete': True},
    'Administrator': {'view': True, 'add': True, 'edit': True, 'delete': True},
}

for group, mods in grouped.items():
    # We can use the 'parent' field to store the group, or just create a parent module for the group
    parent_mod, _ = Module.objects.get_or_create(module_name=group, defaults={'module_code': group.upper()[:10], 'menu_type': 'menu'})
    
    for mod_name in mods:
        mod, created = Module.objects.get_or_create(
            module_name=mod_name, 
            defaults={
                'module_code': mod_name.upper().replace(' ', '')[:10], 
                'menu_type': 'submenu',
                'parent': parent_mod
            }
        )
        # Update permissions
        mod.template_permissions = default_perms
        mod.save()
        print(f"Updated {mod_name} under {group}")

