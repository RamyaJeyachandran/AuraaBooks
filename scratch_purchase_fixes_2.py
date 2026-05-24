import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tooltips for Purchase Bill No, Bill Date, Supplier / Vendor in the New Cash Purchase Modal

pb_no_old = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Purchase Bill No <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>"""
pb_no_new = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1 group/tooltip relative cursor-pointer w-max">
                                Purchase Bill No 
                                <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                                <div class="absolute left-0 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal text-left">
                                    Number of the invoice generated while purchasing from supplier can be entered
                                    <div class="absolute -top-1.5 left-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                </div>
                            </label>"""
content = content.replace(pb_no_old, pb_no_new)

bill_date_old = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Bill Date <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>"""
bill_date_new = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1 group/tooltip relative cursor-pointer w-max">
                                Bill Date 
                                <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                                <div class="absolute left-0 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal text-left">
                                    Date in which the invoice is prepared
                                    <div class="absolute -top-1.5 left-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                </div>
                            </label>"""
content = content.replace(bill_date_old, bill_date_new)

sup_ven_old = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier / Vendor <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>"""
sup_ven_new = """<label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1 group/tooltip relative cursor-pointer w-max">
                                Supplier / Vendor 
                                <svg class="w-3.5 h-3.5 text-slate-400 group-hover/tooltip:text-[var(--accent)] transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                                <div class="absolute left-0 top-full mt-2 w-max max-w-[250px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/tooltip:opacity-100 group-hover/tooltip:visible transition-all z-[1000] normal-case tracking-normal text-left">
                                    Select existing Contact. Also option to save as a New Contact
                                    <div class="absolute -top-1.5 left-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                </div>
                            </label>"""
content = content.replace(sup_ven_old, sup_ven_new)


# 2. Change + icon button background color to primary color
plus_btn_old = """<button type="button" onclick="addPbCashPaymentRow()" class="w-10 h-10 bg-slate-200 hover:bg-slate-300 rounded flex items-center justify-center transition-all text-slate-500" title="Add Row">"""
plus_btn_new = """<button type="button" onclick="addPbCashPaymentRow()" class="w-10 h-10 bg-[var(--accent)] hover:brightness-110 text-white rounded flex items-center justify-center transition-all shadow-sm" title="Add Row">"""
content = content.replace(plus_btn_old, plus_btn_new)


# 3. Change table search textbox background color to white
search_old = """<input type="text" placeholder="Search..." class="w-full h-8 bg-white/10 border border-white/20 rounded px-3 text-[12px] text-white placeholder-white/50 outline-none focus:border-white transition-all" title="Search Items">"""
search_new = """<input type="text" placeholder="Search..." class="w-full h-8 bg-white border border-transparent rounded px-3 text-[12px] text-slate-700 placeholder-slate-400 outline-none focus:border-white/50 transition-all shadow-inner" title="Search Items">"""
content = content.replace(search_old, search_new)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates successful")
