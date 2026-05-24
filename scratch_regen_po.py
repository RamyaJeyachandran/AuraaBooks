import os
import shutil

src = r"d:\AuraaZenAIProject\abproject\templates\sales_orders.html"
dst = r"d:\AuraaZenAIProject\abproject\templates\purchase_orders.html"

shutil.copyfile(src, dst)

with open(dst, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace texts
content = content.replace("Sales Order", "Purchase Order")
content = content.replace("Sales /", "Purchase /")
content = content.replace("Sales", "Purchase")
content = content.replace("Customer", "Supplier")

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated purchase_orders.html")
