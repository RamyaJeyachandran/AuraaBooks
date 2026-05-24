import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("Supplier / Vendor", "Supplier")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement successful")
