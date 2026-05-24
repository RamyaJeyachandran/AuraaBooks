import os

urls_path = r"d:\AuraaZenAIProject\abproject\apps\core\urls.py"
with open(urls_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace GenericMasterView with PurchaseBillView for purchase-bills route
content = content.replace(
    "path('purchase/bills/', views.GenericMasterView.as_view(title='Purchase Bills', parent_name='Purchase'), name='purchase-bills'),",
    "path('purchase/bills/', views.PurchaseBillView.as_view(), name='purchase-bills'),"
)

with open(urls_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated core/urls.py")
