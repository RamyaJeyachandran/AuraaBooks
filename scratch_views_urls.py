import re

views_path = r'd:\AuraaZenAIProject\abproject\apps\core\views.py'
with open(views_path, 'r', encoding='utf-8') as f:
    views_content = f.read()

new_view = """
class PurchaseQuotesListView(TemplateView):
    template_name = 'purchase_quotes.html'
"""

if "PurchaseQuotesListView" not in views_content:
    views_content += new_view
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views_content)
    print("Added PurchaseQuotesListView to views.py")
else:
    print("PurchaseQuotesListView already exists")

urls_path = r'd:\AuraaZenAIProject\abproject\apps\core\urls.py'
with open(urls_path, 'r', encoding='utf-8') as f:
    urls_content = f.read()

# Replace GenericMasterView for purchase quotes
old_url = "path('purchase/quotes/', views.GenericMasterView.as_view(title='Purchase Quotes', parent_name='Purchase'), name='purchase-quotes')"
new_url = "path('purchase/quotes/', views.PurchaseQuotesListView.as_view(), name='purchase-quotes')"

if old_url in urls_content:
    urls_content = urls_content.replace(old_url, new_url)
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls_content)
    print("Updated urls.py")
else:
    print("Could not find the target URL in urls.py (or already updated)")
