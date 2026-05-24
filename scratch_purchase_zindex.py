import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove overflow-hidden from the table container
container_old = """<div class="border border-slate-200 rounded-xl overflow-hidden flex flex-col h-[360px] shadow-sm">"""
container_new = """<div class="border border-slate-200 rounded-xl flex flex-col h-[360px] shadow-sm">"""
content = content.replace(container_old, container_new)

# 2. Add rounded-t-xl to Table Header
header_old = """<div class="flex items-center h-12 bg-[var(--accent)] text-white border-b border-slate-200 shrink-0">"""
header_new = """<div class="flex items-center h-12 bg-[var(--accent)] text-white border-b border-slate-200 shrink-0 rounded-t-xl">"""
content = content.replace(header_old, header_new)

# 3. Add rounded-b-xl to Table Footer
footer_old = """<!-- Table Footer / Summary -->
                        <div class="bg-slate-50 border-t border-slate-200">"""
footer_new = """<!-- Table Footer / Summary -->
                        <div class="bg-slate-50 border-t border-slate-200 rounded-b-xl">"""
content = content.replace(footer_old, footer_new)

# Also the inner bg-white needs rounded-b-xl to not overflow the parent's rounded corners
total_row_old = """<div class="flex items-center h-12 bg-white">
                                <div class="flex-1 text-right px-4 text-[13px] font-black text-slate-800">Total</div>"""
total_row_new = """<div class="flex items-center h-12 bg-white rounded-b-xl">
                                <div class="flex-1 text-right px-4 text-[13px] font-black text-slate-800">Total</div>"""
content = content.replace(total_row_old, total_row_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Z-index and overflow fixed")
