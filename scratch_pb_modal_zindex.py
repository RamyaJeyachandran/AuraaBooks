import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Modal container overflow issue which clips tooltips
old_modal_container = """<div class="relative bg-white w-full max-w-[1400px] max-h-[95vh] rounded-xl shadow-2xl flex flex-col overflow-hidden" onclick="event.stopPropagation()">"""
new_modal_container = """<div class="relative bg-white w-full max-w-[1400px] max-h-[95vh] rounded-xl shadow-2xl flex flex-col" onclick="event.stopPropagation()">"""
content = content.replace(old_modal_container, new_modal_container)

old_header = """<div class="flex items-center justify-between px-6 py-4 bg-[var(--accent)] text-white border-b border-white/20">"""
new_header = """<div class="flex items-center justify-between px-6 py-4 bg-[var(--accent)] text-white border-b border-white/20 rounded-t-xl">"""
content = content.replace(old_header, new_header)

old_body = """<div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar">"""
new_body = """<div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar rounded-b-xl">"""
content = content.replace(old_body, new_body)

# Replace the "i" icon path with the "?" icon path
old_path = """M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"""
new_path = """M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"""

content = content.replace(old_path, new_path)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied z-index fix and icon replacement successfully!")
