import os

urls_path = r"d:\AuraaZenAIProject\abproject\config\urls.py"
with open(urls_path, "r", encoding="utf-8") as f:
    urls_content = f.read()

if "PurchaseBillView" not in urls_content:
    urls_content = urls_content.replace(
        "from apps.core.views import",
        "from apps.core.views import PurchaseBillView,"
    )
    urls_content = urls_content.replace(
        "path('purchase_quotes/', PurchaseQuotesView.as_view(), name='purchase_quotes'),",
        "path('purchase_quotes/', PurchaseQuotesView.as_view(), name='purchase_quotes'),\n    path('purchase_bill/', PurchaseBillView.as_view(), name='purchase_bill'),"
    )
    with open(urls_path, "w", encoding="utf-8") as f:
        f.write(urls_content)
    print("Added route to config/urls.py")
else:
    print("Route already exists.")
