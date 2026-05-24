
views_path = r'd:\AuraaZenAIProject\abproject\apps\core\views.py'
urls_path  = r'd:\AuraaZenAIProject\abproject\apps\core\urls.py'

# ── views.py ──────────────────────────────────────────────────────────────
with open(views_path, 'r', encoding='utf-8') as f:
    views = f.read()

new_view = """
class PurchaseOrdersListView(TemplateView):
    template_name = 'purchase_orders.html'
"""
if 'PurchaseOrdersListView' not in views:
    views += new_view
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views)
    print("Added PurchaseOrdersListView to views.py")
else:
    print("PurchaseOrdersListView already exists")

# ── urls.py ───────────────────────────────────────────────────────────────
with open(urls_path, 'r', encoding='utf-8') as f:
    urls = f.read()

old = "path('purchase/orders/', views.GenericMasterView.as_view(title='Purchase Orders', parent_name='Purchase'), name='purchase-orders')"
new = "path('purchase/orders/', views.PurchaseOrdersListView.as_view(), name='purchase-orders')"

if old in urls:
    urls = urls.replace(old, new)
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls)
    print("Updated urls.py")
elif 'PurchaseOrdersListView' in urls:
    print("urls.py already updated")
else:
    print("WARNING: old url pattern not found in urls.py")
