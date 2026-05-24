import os

file_path = r"d:\AuraaZenAIProject\abproject\templates\supplier_credit_note.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Change Title
content = content.replace(
    '<h2 class="text-[18px] font-black tracking-tight">New Supplier Credit Note</h2>',
    '<h2 class="text-[18px] font-black tracking-tight">New Purchase Credit Note</h2>'
)

# Replace "Reason" block and "Reference #" block with the new layout
# In the original, the first row had SCN No, Date, Reason, Reference # + Gear
# We want: Trans No, Credit Note Date, Supplier Invoice No # + Gear

old_top_grid = """            <!-- Top Info Grid -->
            <div class="grid grid-cols-4 gap-6 mb-8">
                <!-- SCN No -->
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Supplier Credit Note No
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-56 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Unique number for each supplier credit note</div>
                    </label>
                    <div class="text-[22px] font-black text-slate-800">SCN1</div>
                </div>
                <!-- Date -->
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Credit Note Date
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-52 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Date on which the credit note is issued</div>
                    </label>
                    <div class="relative">
                        <input type="text" value="23/05/2026" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
                <!-- Reason -->
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                        Reason
                        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-52 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Reason for issuing the supplier credit note</div>
                    </label>
                    <div class="relative">
                        <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] appearance-none shadow-inner">
                            <option>Goods Returned</option>
                            <option>Price Difference</option>
                            <option>Quality Issue</option>
                            <option>Other</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </div>
                </div>
                <!-- Reference # + Gear -->
                <div class="flex items-end gap-3 relative z-[400]">
                    <div class="flex-1">
                        <label class="flex items-center gap-1 text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 group/tip relative">
                            Reference #
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tip:block absolute top-full left-0 mt-1 w-60 bg-white border border-slate-200 shadow-xl p-3 text-[11px] text-slate-600 rounded z-[2000]">Transaction number can be entered for reference</div>
                        </label>
                        <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    </div>
                    <div class="relative pb-2">
                        <button onclick="toggleActionMenu(event, 'scnRefSettingsMenu')" class="text-slate-400 hover:text-slate-600 transition-all">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                        </button>
                        <div id="scnRefSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-72 bg-[var(--accent)] rounded-lg shadow-2xl p-4 z-[1100] border border-white/20 text-white">
                            <div class="space-y-3">
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Show Reverse Charge</span></label>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Tax Round Off</span></label>
                                <div class="text-[12px] pt-1">Initial Focus <a href="#" class="text-blue-200 hover:underline">Date</a></div>
                                <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Ignore Auto Select if multiple Attributes</span></label>
                                <a href="#" class="block text-[12px] text-blue-200 hover:underline pt-1">Manage Custom Fields...</a>
                                <button class="mt-2 px-6 py-2 bg-white text-[var(--accent)] rounded font-bold text-[12px] hover:bg-slate-100 transition-all">Save</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

new_top_grid = """            <!-- Top Info Grid -->
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
            </div>"""

content = content.replace(old_top_grid, new_top_grid)

# Change Supplier Label
content = content.replace(
    '''Supplier <span class="text-red-500 ml-1">*</span>''',
    '''Supplier / Vendor <span class="text-red-500 ml-1">*</span>'''
)

# Table headers - remove Tax %
old_th_tax = '<th class="px-4 py-3 text-[12px] font-bold w-32 text-right border-r border-white/20">Tax %</th>'
content = content.replace(old_th_tax, '')

# Table body - remove Tax % cell
old_td_tax = '<td class="p-0 border-r border-slate-100"></td>\n                            <td class="p-0 border-r border-slate-100"></td>\n                            <td class="p-0"></td>'
new_td_tax = '<td class="p-0 border-r border-slate-100"></td>\n                            <td class="p-0"></td>'
content = content.replace(old_td_tax, new_td_tax)

# Table Settings Menu - add missing fields based on image
old_table_settings = """                                    <div class="space-y-2 max-h-[260px] overflow-y-auto pr-1">
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Description (Below Item)</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">SKU</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">HSN / SAC</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded"><span class="text-[12px]">Unit</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Net Rate</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">MRP</span></label>
                                        <a href="#" class="block text-[12px] text-blue-600 hover:underline pt-1">Manage Custom Fields...</a>
                                        <label class="flex items-center gap-2 cursor-pointer mt-1"><input type="checkbox" class="rounded"><span class="text-[12px]">Item Details in Popup</span></label>
                                        <div class="flex gap-2 pt-2">"""

new_table_settings = """                                    <div class="space-y-2 max-h-[260px] overflow-y-auto pr-1">
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Description (Below Item)</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">SKU</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">HSN / SAC</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Account</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Tax</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Location</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Qty</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Rate</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded"><span class="text-[12px]">Unit</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Net Rate</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">MRP</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Discount Per Item</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Group Similar Item</span></label>
                                        <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded"><span class="text-[12px]">Charges Amount</span></label>
                                        <a href="#" class="block text-[12px] text-blue-600 hover:underline pt-1">Manage Custom Fields...</a>
                                        <label class="flex items-center gap-2 cursor-pointer mt-1"><input type="checkbox" class="rounded"><span class="text-[12px]">Item Details in Popup</span></label>
                                        <div class="flex gap-2 pt-2">"""

content = content.replace(old_table_settings, new_table_settings)

# Remove Tax Amount from Subtotals
old_tax_amount = """                    <div class="flex items-center w-72 justify-between">
                        <span class="text-[12px] font-medium text-slate-600">Tax Amount</span>
                        <span class="text-[12px] text-slate-300">0.00</span>
                    </div>"""
content = content.replace(old_tax_amount, '')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated supplier_credit_note.html")
