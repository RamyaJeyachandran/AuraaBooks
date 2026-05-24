import os

file_path = r"d:\AuraaZenAIProject\abproject\templates\supplier_credit_note.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Combine the two 4-column grids into a single 6-column grid
old_grid = """            <!-- Top Info Grid -->
            <div class="grid grid-cols-4 gap-6 mb-8">
                <!-- Trans No -->
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Trans No
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-56 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Unique number for each transaction</div>
                    </label>
                    <div class="text-[22px] font-black text-slate-800">1</div>
                </div>
                <!-- Date -->
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Credit Note Date
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-52 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Date on which the credit note is issued</div>
                    </label>
                    <div class="relative">
                        <input type="text" value="24/05/2026" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
                <!-- Supplier Invoice No # + Gear -->
                <div class="flex items-end gap-3 relative z-[400]">
                    <div class="flex-1">
                        <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                            Supplier Invoice No #
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-60 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Supplier Invoice number</div>
                        </label>
                        <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    </div>
                    <div class="relative pb-2">
                        <button onclick="toggleActionMenu(event, 'scnRefSettingsMenu')" class="text-slate-400 hover:text-slate-600 transition-all">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                        </button>
                        <div id="scnRefSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl p-4 z-[1100] border-2 border-[var(--accent)] text-slate-800 text-left">
                            <div class="space-y-3">
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Show Reverse Charge</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Customs Duty Payable</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">TCS Receivable</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Tax Round Off</span></label>
                                <div class="text-[12px] pt-1">Initial Focus <a href="#" class="text-blue-500 hover:underline">Date</a></div>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Ignore Auto Select if multiple Attributes</span></label>
                                <a href="#" class="block text-[12px] text-blue-500 hover:underline pt-1">Manage Custom Fields...</a>
                                <button class="mt-2 px-6 py-2.5 bg-[var(--accent)] text-white rounded-lg font-bold text-[12px] hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Save</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div></div>
            </div>

            <!-- Supplier Row -->
            <div class="grid grid-cols-4 gap-6 mb-8">
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2">
                        Supplier / Vendor <span class="text-red-500 ml-1">*</span>
                    </label>
                    <div class="relative">
                        <input type="text" placeholder="Select Contact (F9)" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner placeholder-slate-300">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </div>
                </div>
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Credit Note No</label>
                    <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                </div>
                <div>
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Credit Note Date</label>
                    <div class="relative">
                        <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold placeholder-slate-300 outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
            </div>"""

new_grid = """            <!-- Top Info Grid -->
            <div class="grid grid-cols-6 gap-4 mb-8">
                <!-- Trans No -->
                <div>
                    <label class="flex items-center gap-1 text-[9px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Trans No
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-56 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Unique number for each transaction</div>
                    </label>
                    <div class="text-[22px] font-black text-slate-800">1</div>
                </div>
                <!-- Date -->
                <div>
                    <label class="flex items-center gap-1 text-[9px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Credit Note Date
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-52 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Date on which the credit note is issued</div>
                    </label>
                    <div class="relative">
                        <input type="text" value="24/05/2026" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[12px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
                <!-- Supplier Invoice No # + Gear -->
                <div class="flex items-end gap-1 relative z-[400]">
                    <div class="flex-1">
                        <label class="flex items-center gap-1 text-[9px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                            Supplier Inv#
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-60 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Supplier Invoice number</div>
                        </label>
                        <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[12px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    </div>
                    <div class="relative pb-2">
                        <button onclick="toggleActionMenu(event, 'scnRefSettingsMenu')" class="text-slate-400 hover:text-slate-600 transition-all flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                        </button>
                        <div id="scnRefSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl p-4 z-[1100] border-2 border-[var(--accent)] text-slate-800 text-left">
                            <div class="space-y-3">
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Show Reverse Charge</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Customs Duty Payable</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">TCS Receivable</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Tax Round Off</span></label>
                                <div class="text-[12px] pt-1">Initial Focus <a href="#" class="text-blue-500 hover:underline">Date</a></div>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded border-slate-300"><span class="text-[12px] font-semibold">Ignore Auto Select if multiple Attributes</span></label>
                                <a href="#" class="block text-[12px] text-blue-500 hover:underline pt-1">Manage Custom Fields...</a>
                                <button class="mt-2 px-6 py-2.5 bg-[var(--accent)] text-white rounded-lg font-bold text-[12px] hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Save</button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Supplier / Vendor -->
                <div>
                    <label class="flex items-center gap-1 text-[9px] font-black text-red-500 uppercase tracking-widest mb-2">
                        Supplier / Vendor <span class="text-red-500 ml-0.5">*</span>
                    </label>
                    <div class="relative">
                        <input type="text" placeholder="Select Contact" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[12px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner placeholder-slate-300">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </div>
                </div>
                <!-- Supplier Credit Note No -->
                <div>
                    <label class="block text-[9px] font-black text-slate-400 uppercase tracking-widest mb-2">Sup. CR Note No</label>
                    <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[12px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                </div>
                <!-- Supplier Credit Note Date -->
                <div>
                    <label class="block text-[9px] font-black text-slate-400 uppercase tracking-widest mb-2">Sup. CR Note Date</label>
                    <div class="relative">
                        <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[12px] font-bold placeholder-slate-300 outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
            </div>"""

content = content.replace(old_grid, new_grid)

# 2. Fix Z-index issue
# Change `overflow-hidden` to `overflow-visible` on the table container
# Also add rounded-tl-2xl to first th and rounded-tr-2xl to last th so corners aren't lost
old_table_container = '<div class="border border-slate-200 bg-white shadow-sm mb-6 pb-6 relative z-[300] rounded-2xl overflow-hidden">'
new_table_container = '<div class="border border-slate-200 bg-white shadow-sm mb-6 pb-6 relative z-[300] rounded-2xl overflow-visible">'
content = content.replace(old_table_container, new_table_container)

old_first_th = '<th class="px-4 py-3 text-[12px] font-bold w-12 border-r border-white/20">'
new_first_th = '<th class="px-4 py-3 text-[12px] font-bold w-12 border-r border-white/20 rounded-tl-xl">'
content = content.replace(old_first_th, new_first_th)

old_last_th = '<th class="px-3 py-3 w-12 text-center relative z-[400]">'
new_last_th = '<th class="px-3 py-3 w-12 text-center relative z-[400] rounded-tr-xl">'
content = content.replace(old_last_th, new_last_th)

# Optional: Add an explicit higher z-index to the table container and the header if needed, but relative z-[300] and z-[1100] for menu should work if overflow is visible.

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated supplier_credit_note.html")
