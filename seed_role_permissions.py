from apps.core.models import Module

roles = [
    'Transactions Sales Entry',
    'Transactions Sales & Purchase Entry',
    'Sales Rep',
    'Franchisee',
    'Accountant',
    'Administrator',
    'Stock Keeper'
]

# Base dict for default False
def default_perms():
    return {
        'view': False, 'add': False, 'edit': False, 'delete': False,
        'block_discount': False, 'block_freeqty': False, 'block_ratesheet': False,
        'block_edit_rate': False, 'only_draft_status': False,
        'block_rate_amount': False, 'display_rate_internal_transfer': False
    }

def grant_perms():
    return {
        'view': True, 'add': True, 'edit': True, 'delete': True,
        'block_discount': False, 'block_freeqty': False, 'block_ratesheet': False,
        'block_edit_rate': False, 'only_draft_status': False,
        'block_rate_amount': False, 'display_rate_internal_transfer': False
    }

def assign(perms, role, grant=False):
    if role not in perms:
        perms[role] = default_perms()
    if grant:
        perms[role]['view'] = True
        perms[role]['add'] = True
        perms[role]['edit'] = True
        perms[role]['delete'] = True

for m in Module.objects.all():
    name = m.module_name
    perms = m.template_permissions or {}
    
    # Initialize all roles with default_perms if not present
    for role in roles:
        if role not in perms:
            perms[role] = default_perms()
            
    # Reset all to false first for these specific roles to avoid lingering true values
    for role in roles:
        if role != 'Administrator':
            perms[role] = default_perms()
        else:
            perms[role] = grant_perms()

    # 1. Transaction sales entry
    if name in ['Customer', 'Items', 'Rate Sheet']:
        assign(perms, 'Transactions Sales Entry', True)
    if m.parent and m.parent.module_name == 'Sales':
        assign(perms, 'Transactions Sales Entry', True)
        
    # 2. Transaction sales & purchase entry
    if name in ['Customer', 'Supplier', 'Suppliers', 'Items', 'Rate Sheet']:
        assign(perms, 'Transactions Sales & Purchase Entry', True)
    if m.parent and m.parent.module_name in ['Sales', 'Purchase', 'Expense', 'Expenses']:
        assign(perms, 'Transactions Sales & Purchase Entry', True)

    # 3. Sales Rep
    if name in ['Customer', 'Items', 'Rate Sheet']:
        assign(perms, 'Sales Rep', True)
    if m.parent and m.parent.module_name == 'Sales':
        assign(perms, 'Sales Rep', True)
    if name in ['Goods Receipt', 'Goods Receipt Note']:
        assign(perms, 'Sales Rep', True)

    # 4. Franchisee
    if name in ['Customer', 'Supplier', 'Suppliers', 'Items', 'Rate Sheet']:
        assign(perms, 'Franchisee', True)
    if m.parent and m.parent.module_name in ['Sales', 'Purchase', 'Expense', 'Expenses']:
        assign(perms, 'Franchisee', True)

    # 5. Accountant
    if name in ['Dashboard', 'Customer', 'Supplier', 'Suppliers', 'Items', 'Rate Sheet', 'Stock Journal', 'Sales Rep', 'Referred By', 'Refered By', 'Bank/Cash', 'Bank / Cash', 'Project', 'E-Commerce']:
        assign(perms, 'Accountant', True)
    if m.parent and m.parent.module_name in ['Sales', 'Purchase', 'Expense', 'Expenses']:
        assign(perms, 'Accountant', True)

    # 7. Stock Keeper
    if name in ['Items', 'Rate Sheet', 'Stock Journal']:
        assign(perms, 'Stock Keeper', True)
    if name in ['Delivery Challan', 'Delivery challan']:
        assign(perms, 'Stock Keeper', True)
    if name in ['Goods Receipt', 'Goods Receipt Note']:
        assign(perms, 'Stock Keeper', True)

    m.template_permissions = perms
    m.save()

print("Role permissions seeded successfully.")
