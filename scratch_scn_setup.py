views_path = r'd:\AuraaZenAIProject\abproject\apps\core\views.py'
urls_path  = r'd:\AuraaZenAIProject\abproject\apps\core\urls.py'

# ── views.py ──────────────────────────────────────────────────────────────
with open(views_path, 'r', encoding='utf-8') as f:
    views = f.read()

new_view = """
class SupplierCreditNoteListView(TemplateView):
    template_name = 'supplier_credit_note.html'
"""
if 'SupplierCreditNoteListView' not in views:
    views += new_view
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views)
    print("Added SupplierCreditNoteListView to views.py")
else:
    print("View already exists")

# ── urls.py ───────────────────────────────────────────────────────────────
with open(urls_path, 'r', encoding='utf-8') as f:
    urls = f.read()

old_url = "path('purchase/credit-note/', views.GenericMasterView.as_view(title='Supplier Credit Note', parent_name='Purchase'), name='supplier-credit-note')"
new_url = "path('purchase/credit-note/', views.SupplierCreditNoteListView.as_view(), name='supplier-credit-note')"

if old_url in urls:
    urls = urls.replace(old_url, new_url)
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls)
    print("Updated urls.py")
elif 'SupplierCreditNoteListView' in urls:
    print("URL already updated")
else:
    print("WARNING: old URL pattern not found")
