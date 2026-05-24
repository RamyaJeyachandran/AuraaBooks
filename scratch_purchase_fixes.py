import os
import re

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modify New Cash Purchase Modal
# Remove the button from Bill Date
bill_date_label_old = """                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center justify-between">
                                <span class="flex items-center gap-1">Bill Date <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>
                                <button onclick="toggleActionMenu(event, 'pbCashBillDateSettings')" class="text-slate-400 hover:text-[var(--accent)]" title="Bill Date Settings">
                                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                </button>
                            </label>"""
                            
bill_date_label_new = """                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Bill Date <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>"""

content = content.replace(bill_date_label_old, bill_date_label_new)

# We need to extract the pbCashBillDateSettings div and move it to Supplier Invoice Date section.
settings_div_old = """                            <!-- Popover: Bill Date Settings -->
                            <div id="pbCashBillDateSettings" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl border border-slate-100 p-4 z-[500]">
                                <div class="absolute -top-1.5 right-6 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                <div class="space-y-4">
                                    <label class="flex items-center gap-3 cursor-pointer">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                        <span class="text-[13px] text-slate-700">Show Reverse Charge</span>
                                    </label>
                                    <label class="flex items-center gap-3 cursor-pointer opacity-50">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300" disabled>
                                        <span class="text-[13px] text-slate-700">Tax Round Off</span>
                                    </label>
                                    <div class="text-[13px] text-slate-700 pt-1">
                                        Initial Focus <a href="#" class="text-blue-500 hover:underline ml-1 font-medium">Date</a>
                                    </div>
                                    <label class="flex items-center gap-3 cursor-pointer">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                        <span class="text-[13px] text-slate-700">Ignore Auto Select if multiple Attributes</span>
                                    </label>
                                    <div class="pt-1">
                                        <a href="#" class="text-blue-500 hover:underline text-[13px]">Manage Custom Fields...</a>
                                    </div>
                                    <div class="pt-2">
                                        <button class="px-5 py-2 bg-[#22c55e] text-white rounded font-bold text-[13px] hover:bg-green-600 transition-all">Save</button>
                                    </div>
                                </div>
                            </div>"""

content = content.replace(settings_div_old, "")

supplier_invoice_date_old = """                        <!-- Supplier Invoice Date -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier Invoice Date</label>
                            <div class="relative">
                                <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none focus:border-[var(--accent)]" title="Supplier Invoice Date">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                            </div>
                        </div>"""

supplier_invoice_date_new = """                        <!-- Supplier Invoice Date -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier Invoice Date</label>
                            <div class="flex items-center gap-2">
                                <div class="relative flex-1">
                                    <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none focus:border-[var(--accent)]" title="Supplier Invoice Date">
                                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                                </div>
                                <div class="relative shrink-0">
                                    <button onclick="toggleActionMenu(event, 'pbCashBillDateSettings')" class="w-10 h-10 bg-[var(--accent)] text-white rounded flex items-center justify-center hover:brightness-110 transition-all shadow-sm" title="Settings">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                    </button>
                                    
                                    <!-- Popover: Settings -->
                                    <div id="pbCashBillDateSettings" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl border border-slate-100 p-4 z-[500]">
                                        <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                        <div class="space-y-4">
                                            <label class="flex items-center gap-3 cursor-pointer">
                                                <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[13px] text-slate-700">Show Reverse Charge</span>
                                            </label>
                                            <label class="flex items-center gap-3 cursor-pointer opacity-50">
                                                <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300" disabled>
                                                <span class="text-[13px] text-slate-700">Tax Round Off</span>
                                            </label>
                                            <div class="text-[13px] text-slate-700 pt-1">
                                                Initial Focus <a href="#" class="text-blue-500 hover:underline ml-1 font-medium">Date</a>
                                            </div>
                                            <label class="flex items-center gap-3 cursor-pointer">
                                                <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[13px] text-slate-700">Ignore Auto Select if multiple Attributes</span>
                                            </label>
                                            <div class="pt-1">
                                                <a href="#" class="text-blue-500 hover:underline text-[13px]">Manage Custom Fields...</a>
                                            </div>
                                            <div class="pt-2">
                                                <button class="px-5 py-2 bg-[#22c55e] text-white rounded font-bold text-[13px] hover:bg-green-600 transition-all">Save</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>"""

content = content.replace(supplier_invoice_date_old, supplier_invoice_date_new)

# 2. Add tooltips to the original New Purchase Modal
# For Original Modal (which starts around line 430: "New Purchase Modal")
# Purchase Bill No input
content = content.replace(
    '<input type="text" value="PB-001" class="w-24 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold text-center outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">',
    '<input type="text" value="PB-001" class="w-24 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold text-center outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner" title="Purchase Bill No">'
)
# Bill Date input
content = content.replace(
    '<input type="text" value="24/05/2026" class="w-32 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">',
    '<input type="text" value="24/05/2026" class="w-32 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner" title="Bill Date">'
)
# Purchase Order No input
content = content.replace(
    '<input type="text" placeholder="Optional" class="w-32 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">',
    '<input type="text" placeholder="Optional" class="w-32 h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner" title="Purchase Order No">'
)

# Supplier / Vendor dropdown
content = content.replace(
    '<select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">',
    '<select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none" title="Supplier / Vendor">'
)

# Supplier Invoice No
content = content.replace(
    '<input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">',
    '<input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner" title="Supplier Invoice No">'
)

# Supplier Invoice Date
content = content.replace(
    '<input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">',
    '<input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner" title="Supplier Invoice Date">'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifications successful")
