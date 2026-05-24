import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the save button classes
old_btn = 'class="px-5 py-2 bg-[#22c55e] text-white rounded font-bold text-[13px] hover:bg-green-600 transition-all">Save</button>'
new_btn = 'class="px-5 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all shadow-sm">Save</button>'
content = content.replace(old_btn, new_btn)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Save button colors updated")
