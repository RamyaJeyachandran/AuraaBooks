import re

FILES = [
    r'd:\AuraaZenAIProject\abproject\templates\purchase_quotes.html',
    r'd:\AuraaZenAIProject\abproject\templates\purchase_orders.html',
]

# Label replacements for the "flex items-center gap-1" style labels 
# (the ones with tooltips on them) - keep the group/tooltip functionality
# but change the text style to match customer modal
LABEL_REPLACEMENTS = [
    # Purchase Quote labels with group/tooltip
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative"',
        'class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tooltip relative"'
    ),
    # Supplier label with group/tooltip (red)
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-[#b91c1c] mb-2 group/tooltip relative"',
        'class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2 group/tooltip relative"'
    ),
    # Purchase Orders labels with group/tip  
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tip relative"',
        'class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative"'
    ),
    # Supplier label in purchase orders (red)
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-red-600 mb-2"',
        'class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2"'
    ),
    # Notes/Terms labels (w-max variants)
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative w-max"',
        'class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tooltip relative w-max"'
    ),
    (
        'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tip relative w-max"',
        'class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative w-max"'
    ),
]

# Fix the Valid Till date input inside flex container (border-none variant)
VALIDTILL_OLD = 'class="w-full h-10 px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none border-none"'
VALIDTILL_NEW = 'class="w-full h-10 bg-transparent px-4 text-[13px] font-bold outline-none focus:bg-white"'

# Fix the Valid Till container to match
VALIDTILL_CONTAINER_OLD = 'class="flex border border-slate-200 rounded overflow-hidden"'
VALIDTILL_CONTAINER_NEW = 'class="flex bg-slate-50 border border-slate-100 rounded-xl overflow-hidden shadow-inner"'

# Fix the "on Receipt" dropdown part of Valid Till
VALIDTILL_BTN_OLD = 'class="flex items-center px-3 bg-slate-50 border-r border-slate-200 text-[12px] font-medium text-slate-600"'
VALIDTILL_BTN_NEW = 'class="flex items-center px-3 bg-slate-100 border-r border-slate-200 text-[12px] font-bold text-slate-600"'

# Fix the Supplier dropdown input (has placeholder)
SUPPLIER_SELECT_OLD = 'class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner"'

for filepath in FILES:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    for old, new in LABEL_REPLACEMENTS:
        content = content.replace(old, new)
    
    content = content.replace(VALIDTILL_OLD, VALIDTILL_NEW)
    content = content.replace(VALIDTILL_CONTAINER_OLD, VALIDTILL_CONTAINER_NEW)
    content = content.replace(VALIDTILL_BTN_OLD, VALIDTILL_BTN_NEW)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated labels/containers: {filepath}")
    else:
        print(f"No changes: {filepath}")

print("Done!")
