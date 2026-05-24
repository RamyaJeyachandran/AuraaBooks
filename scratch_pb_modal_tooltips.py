import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Purchase Bill No label
old_pb_no = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Purchase Bill No <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>"""
new_pb_no = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2 group/tooltip relative cursor-pointer w-max">
                        Purchase Bill No 
                        <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal">
                            Number of the invoice generated while purchasing from supplier can be entered
                            <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        </div>
                    </label>"""
content = content.replace(old_pb_no, new_pb_no)

# Replace Bill Date label
old_bill_date = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Bill Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>"""
new_bill_date = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2 group/tooltip relative cursor-pointer w-max">
                        Bill Date 
                        <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal">
                            Date in which the invoice is prepared
                            <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        </div>
                    </label>"""
content = content.replace(old_bill_date, new_bill_date)

# Replace Due Date label
old_due_date = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Due Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>"""
new_due_date = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2 group/tooltip relative cursor-pointer w-max">
                        Due Date 
                        <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal">
                            Due Date is date before which the invoice has to be paid
                            <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        </div>
                    </label>"""
content = content.replace(old_due_date, new_due_date)

# Replace Purchase Order # label
old_po_no = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Purchase Order # <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>"""
new_po_no = """<label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2 group/tooltip relative cursor-pointer w-max">
                        Purchase Order # 
                        <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal z-[2000]">
                            Transaction number can be entered for reference
                            <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        </div>
                    </label>"""
content = content.replace(old_po_no, new_po_no)

# Replace Supplier section to match their exact request
# Ensure it's in a single block if they wanted it packed tighter
old_supplier_area = """            <!-- Supplier Section -->
            <div class="mb-4 w-1/3">
                <label class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2 group/tooltip relative">
                    Supplier / Vendor <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> <span class="text-red-500">*</span>
                </label>
                <div class="relative">
                    <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                        <option>Select Contact (F9)</option>
                    </select>
                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                </div>
            </div>
            
            <div class="flex items-center gap-4 mb-8 w-1/3">
                <div class="space-y-1 flex-1">
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice No</label>
                    <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                </div>
                <div class="space-y-1 flex-1">
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice Date</label>
                    <div class="relative">
                        <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                </div>
            </div>"""

new_supplier_area = """            <!-- Supplier Section -->
            <div class="mb-8 w-1/3 flex flex-col gap-4">
                <div>
                    <label class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2 group/tooltip relative cursor-pointer w-max">
                        Supplier / Vendor 
                        <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                        <span class="text-red-500">*</span>
                        <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal">
                            Select existing Contact. Also option to save as a New Contact
                            <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        </div>
                    </label>
                    <div class="relative">
                        <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                            <option>Select Contact (F9)</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
                
                <div class="flex items-center gap-4">
                    <div class="space-y-1 flex-1">
                        <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice No</label>
                        <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    </div>
                    <div class="space-y-1 flex-1">
                        <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice Date</label>
                        <div class="relative">
                            <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                        </div>
                    </div>
                </div>
            </div>"""
content = content.replace(old_supplier_area, new_supplier_area)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied tooltips successfully!")
