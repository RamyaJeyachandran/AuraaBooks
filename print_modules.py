from apps.core.models import Module

print('| ID | Module Name | Parent Module | Menu Type |')
print('|---|---|---|---|')
for m in Module.objects.all().order_by('id'):
    parent_name = m.parent.module_name if m.parent else 'None'
    print(f'| {m.id} | {m.module_name} | {parent_name} | {m.menu_type} |')
