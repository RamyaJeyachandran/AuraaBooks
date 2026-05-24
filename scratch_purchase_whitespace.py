import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace h-[360px] with max-h-[360px] in the table container of New Cash Purchase Modal
old_str = 'class="border border-slate-200 rounded-xl flex flex-col h-[360px] shadow-sm"'
new_str = 'class="border border-slate-200 rounded-xl flex flex-col max-h-[360px] shadow-sm"'
content = content.replace(old_str, new_str)

# The parent Table Section has flex-1. This flex-1 doesn't do much if the parent container shrinks to fit, but if the parent DOES stretch, flex-1 forces the table section to take up space. I'll remove flex-1 from the table section just in case, to prevent any artificial stretching.
old_parent = 'class="flex-1 overflow-hidden flex flex-col p-6"'
new_parent = 'class="overflow-hidden flex flex-col p-6"'
# Wait, let's only replace it where it occurs right above the table container.
# I'll just do a targeted replacement
content = content.replace(
    '<!-- Table Section -->\n                <div class="flex-1 overflow-hidden flex flex-col p-6">',
    '<!-- Table Section -->\n                <div class="flex flex-col p-6">'
)
# Note: I also removed overflow-hidden from the parent to ensure no clipping, though it might not matter if there's no fixed height.

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("White space fixed")
