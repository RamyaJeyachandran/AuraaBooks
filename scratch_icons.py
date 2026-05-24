import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Normal View "Item" column text color (it was [var(--accent)], should be white)
content = content.replace(
    '<th class="px-4 py-3 text-[13px] font-bold text-[var(--accent)] border-r border-slate-200 relative">',
    '<th class="px-4 py-3 text-[13px] font-bold text-white border-r border-slate-200 relative">'
)

# Fix Normal View Icons
content = content.replace(
    '<div class="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1.5 text-slate-400">',
    '<div class="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1.5 text-white/80">'
)
content = content.replace(
    '<svg class="w-4 h-4 cursor-pointer hover:text-[#1e78b9]"',
    '<svg class="w-4 h-4 cursor-pointer hover:text-white"'
)

# Fix Quick View Icons
content = content.replace(
    '<button class="w-6 h-6 flex items-center justify-center text-slate-400 hover:text-slate-600 rounded bg-slate-50">',
    '<button class="w-6 h-6 flex items-center justify-center text-white/80 hover:text-white rounded bg-transparent">'
)
content = content.replace(
    '<span class="text-[12px] font-bold text-slate-800">Item</span>',
    '<span class="text-[12px] font-bold text-white">Item</span>'
)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons color fixed")
