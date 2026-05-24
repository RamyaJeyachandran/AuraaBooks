import os

filepath = 'd:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_button = """            <button type="button" onclick="openModal('Delivery Challan')" class="px-8 h-[52px] bg-[var(--accent)] text-white rounded-2xl shadow-xl shadow-[var(--accent)]/20 text-[14px] font-black uppercase tracking-widest hover:brightness-110 transition-all cursor-pointer">
                New Delivery Challan
            </button>"""

new_button = """            <div class="relative group/new z-[50]">
                <div class="flex items-center bg-[var(--accent)] text-white rounded-2xl shadow-xl shadow-[var(--accent)]/20 overflow-hidden h-[52px]">
                    <button type="button" onclick="openModal('Delivery Challan')" class="px-8 h-full text-[14px] font-black uppercase tracking-widest hover:brightness-110 transition-all border-r border-white/20">
                        New Delivery Challan
                    </button>
                    <button onclick="toggleActionMenu(event, 'newSplitMenu')" class="px-4 h-full hover:brightness-110 transition-all flex items-center justify-center">
                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </button>
                </div>
                <!-- New Split Dropdown -->
                <div id="newSplitMenu" class="hidden absolute top-full right-0 mt-2 w-56 bg-white rounded-2xl shadow-2xl border border-slate-100 py-2 z-[500]">
                    <button onclick="openModal('Delivery Challan')" class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all cursor-pointer border-none bg-transparent">New Delivery Challan</button>
                    <button onclick="openModal('Counter Delivery')" class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all cursor-pointer border-none bg-transparent">Counter Delivery Challan</button>
                </div>
            </div>"""

if old_button in content:
    content = content.replace(old_button, new_button)
    print("Button replaced successfully!")
else:
    print("Old button not found.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
