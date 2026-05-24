import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert header toggling in setInvoiceType
header_toggles_cash = """            if(header) {
                header.classList.remove('bg-[var(--accent)]', 'border-white/10');
                header.classList.add('bg-slate-50', 'border-slate-200');
            }
            if(backBtn) {
                backBtn.classList.remove('text-white', 'hover:text-white/80');
                backBtn.classList.add('text-slate-800', 'hover:text-slate-600');
            }"""

header_toggles_credit = """            if(header) {
                header.classList.add('bg-[var(--accent)]', 'border-white/10');
                header.classList.remove('bg-slate-50', 'border-slate-200');
            }
            if(backBtn) {
                backBtn.classList.add('text-white', 'hover:text-white/80');
                backBtn.classList.remove('text-slate-800', 'hover:text-slate-600');
            }"""

content = content.replace(header_toggles_cash, "")
content = content.replace(header_toggles_credit, "")

# 2. Revert Print and Save buttons to their original outline/white styling
print_btn_old = """<div class="relative group/print h-8 shadow-sm">
                            <div class="flex items-stretch h-full rounded overflow-hidden">
                                <button type="button" class="px-4 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white text-[13px] font-bold transition-colors outline-none">
                                    Print
                                </button>
                                <button type="button" onclick="toggleActionMenu(event, 'printSplitMenu')" class="px-2 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white border-l border-white/20 flex items-center justify-center transition-colors outline-none">
                                    <span class="text-[10px]">▼</span>
                                </button>
                            </div>"""
print_btn_new = """<div class="relative group/print h-8 shadow-sm">
                            <div class="flex items-stretch h-full rounded overflow-hidden border border-[var(--accent)]/10">
                                <button type="button" class="px-4 h-full bg-white hover:bg-slate-50 text-[var(--accent)] text-[13px] font-bold transition-colors outline-none uppercase tracking-widest">
                                    Print
                                </button>
                                <button type="button" onclick="toggleActionMenu(event, 'printSplitMenu')" class="px-2 h-full bg-white hover:bg-slate-50 text-[var(--accent)] border-l border-[var(--accent)]/10 flex items-center justify-center transition-colors outline-none">
                                    <span class="text-[10px]">▼</span>
                                </button>
                            </div>"""

save_btn_old = """<div class="relative group/save h-8 shadow-sm">
                            <div class="flex items-stretch h-full rounded overflow-hidden">
                                <button type="button" onclick="saveInvoice()" class="px-5 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white text-[13px] font-bold transition-colors outline-none">
                                    Save
                                </button>
                                <button type="button" onclick="toggleActionMenu(event, 'saveSplitMenu')" class="px-2 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white border-l border-white/20 flex items-center justify-center transition-colors outline-none">
                                    <span class="text-[10px]">▼</span>
                                </button>
                            </div>"""
save_btn_new = """<div class="relative group/save h-8 shadow-sm">
                            <div class="flex items-stretch h-full rounded overflow-hidden border border-[var(--accent)]/10">
                                <button type="button" onclick="saveInvoice()" class="px-5 h-full bg-white hover:bg-slate-50 text-[var(--accent)] text-[13px] font-bold transition-colors outline-none uppercase tracking-widest">
                                    Save
                                </button>
                                <button type="button" onclick="toggleActionMenu(event, 'saveSplitMenu')" class="px-2 h-full bg-white hover:bg-slate-50 text-[var(--accent)] border-l border-[var(--accent)]/10 flex items-center justify-center transition-colors outline-none">
                                    <span class="text-[10px]">▼</span>
                                </button>
                            </div>"""

content = content.replace(print_btn_old, print_btn_new)
content = content.replace(save_btn_old, save_btn_new)

# 3. Change Table headers to primary color
# First table (Normal View)
content = content.replace(
    '<tr class="bg-slate-50 border-b border-slate-200">',
    '<tr class="bg-[var(--accent)] border-b border-[var(--accent)]/20">'
)
# Revert inner th text colors
content = re.sub(r'class="px-4 py-3 text-\[13px\] font-bold text-slate-800', r'class="px-4 py-3 text-[13px] font-bold text-white', content)
content = re.sub(r'class="px-3 py-2 text-\[12px\] font-bold text-slate-800', r'class="px-3 py-2 text-[12px] font-bold text-white', content)
content = re.sub(r'class="px-3 py-2 text-\[11px\] font-bold text-slate-800', r'class="px-3 py-2 text-[11px] font-bold text-white', content)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Revert and table changes applied")
