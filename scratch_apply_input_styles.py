import re

# ── Style constants ────────────────────────────────────────────────────────
INPUT_OLD = [
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] focus:border-accent outline-none"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-400 focus:border-accent outline-none"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-300 focus:border-accent outline-none"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none bg-white"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] focus:border-accent outline-none bg-white"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-400 focus:border-accent outline-none bg-white"',
    'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-300 focus:border-accent outline-none bg-white"',
    # Date input inside Valid Till flex container
    'class="w-full h-10 px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none border-none"',
]
INPUT_NEW = 'class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner"'

# Labels inside the top-inputs and supplier blocks
LABEL_OLD = [
    'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative"',
    'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tip relative"',
    'class="block text-[11px] font-bold text-slate-600 mb-2"',
    'class="flex items-center gap-1 text-[13px] font-bold text-red-600 mb-2"',
    'class="flex items-center gap-1 text-[13px] font-bold text-[#b91c1c] mb-2 group/tooltip relative"',
    'class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tip relative"',
]
# We'll keep the tooltip/group logic in labels but add the uppercase tracking style
# For simple block labels → straightforward replacement
LABEL_BLOCK_OLD = 'class="block text-[11px] font-bold text-slate-600 mb-2"'
LABEL_BLOCK_NEW = 'class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2"'

# textarea
TEXTAREA_OLD = 'class="w-full h-24 border border-slate-200 rounded p-3 text-[13px] focus:border-accent outline-none resize-none mb-2"'
TEXTAREA_NEW = 'class="w-full h-24 bg-slate-50 border border-slate-100 rounded-xl px-4 py-3 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner resize-none mb-2"'

TEXTAREA_OLD2 = 'class="w-full h-24 border border-slate-200 rounded p-3 text-[13px] focus:border-accent outline-none resize-none bg-white"'
TEXTAREA_NEW2 = 'class="w-full h-24 bg-slate-50 border border-slate-100 rounded-xl px-4 py-3 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner resize-none"'

TEXTAREA_OLD3 = 'class="w-full h-24 border border-slate-200 rounded p-3 text-[13px] focus:border-accent outline-none resize-none"'
TEXTAREA_NEW3 = 'class="w-full h-24 bg-slate-50 border border-slate-100 rounded-xl px-4 py-3 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner resize-none"'

# Supplier dropdown
SUPPLIER_OLD = 'class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-400 focus:border-accent outline-none"'
SUPPLIER_NEW = 'class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner"'

# Select in purchase orders filter
SELECT_OLD = 'class="w-full h-10 bg-white border border-slate-200 rounded-lg px-3 text-[13px] text-slate-500 outline-none focus:border-accent appearance-none"'
SELECT_NEW = 'class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] appearance-none"'

FILES = [
    r'd:\AuraaZenAIProject\abproject\templates\purchase_quotes.html',
    r'd:\AuraaZenAIProject\abproject\templates\purchase_orders.html',
]

for filepath in FILES:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # Replace all input variants
    for old in INPUT_OLD:
        content = content.replace(old, INPUT_NEW)

    # Replace block labels
    content = content.replace(LABEL_BLOCK_OLD, LABEL_BLOCK_NEW)
    
    # Replace textareas
    content = content.replace(TEXTAREA_OLD, TEXTAREA_NEW)
    content = content.replace(TEXTAREA_OLD2, TEXTAREA_NEW2)
    content = content.replace(TEXTAREA_OLD3, TEXTAREA_NEW3)
    
    # Replace select
    content = content.replace(SELECT_OLD, SELECT_NEW)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed in: {filepath}")

print("Done!")
