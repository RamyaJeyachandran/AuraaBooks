import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modal Body
old_body = 'class="flex-1 overflow-auto bg-slate-50 p-6 flex flex-col"'
new_body = 'class="flex-1 overflow-auto bg-slate-50 p-6 flex flex-col custom-scrollbar"'
content = content.replace(old_body, new_body)

# 2. Table Rows
old_rows = '<!-- Table Rows -->\n                        <div class="flex-1 overflow-y-auto">'
new_rows = '<!-- Table Rows -->\n                        <div class="flex-1 overflow-y-auto custom-scrollbar">'
content = content.replace(old_rows, new_rows)

# 3. Table Settings Popover
old_settings = '<div class="max-h-[400px] overflow-y-auto px-2 py-1 space-y-2">'
new_settings = '<div class="max-h-[400px] overflow-y-auto px-2 py-1 space-y-2 custom-scrollbar">'
content = content.replace(old_settings, new_settings)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Custom scrollbar added")
