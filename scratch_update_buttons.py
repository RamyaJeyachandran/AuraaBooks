import os

files = [
    r"d:\AuraaZenAIProject\abproject\templates\purchase_quotes.html",
    r"d:\AuraaZenAIProject\abproject\templates\purchase_orders.html",
    r"d:\AuraaZenAIProject\abproject\templates\supplier_credit_note.html"
]

replacements = [
    # Settings Button
    (
        'class="w-10 h-10 flex items-center justify-center text-slate-400 hover:text-slate-600 hover:bg-slate-50 rounded-xl transition-all shadow-sm"',
        'class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm"'
    ),
    (
        'class="w-10 h-10 flex items-center justify-center text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-xl transition-all"',
        'class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm"'
    ),
    # Apply Button in Purchase Quotes
    (
        'class="px-6 py-2 bg-slate-200 text-slate-600 rounded-md text-[13px] font-bold hover:bg-slate-300 transition-all mt-2">Apply<',
        'class="w-full mt-2 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply<'
    ),
    # Apply Button in Purchase Orders
    (
        'class="w-full mt-3 py-2 bg-slate-200 text-slate-600 rounded-lg text-[13px] font-bold hover:bg-slate-300 transition-all">Apply<',
        'class="w-full mt-3 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply<'
    ),
    # Apply Button in Supplier Credit Note
    (
        'class="w-full mt-2 py-2 bg-slate-200 text-slate-600 rounded-lg text-[13px] font-bold hover:bg-slate-300 transition-all">Apply<',
        'class="w-full mt-3 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply<'
    )
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes in {file_path}")
