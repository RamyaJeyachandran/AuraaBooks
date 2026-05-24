import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Change 1: View Toggle Split Button Background to white with primary color text
# Search for the view toggle structure
old_view_toggle = """<div class="flex items-center rounded-lg overflow-hidden border border-white/20 shadow-sm h-9">
                        <button class="px-3 h-full bg-white/10 hover:bg-white/20 text-white transition-all border-r border-white/20 flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbViewMenu')" class="px-2 h-full bg-white/10 hover:bg-white/20 text-white transition-all flex items-center justify-center">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </button>
                    </div>"""

new_view_toggle = """<div class="flex items-center rounded-lg overflow-hidden border border-white shadow-sm h-9 bg-white">
                        <button class="px-3 h-full hover:bg-slate-50 text-[var(--accent)] transition-all border-r border-slate-200 flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbViewMenu')" class="px-2 h-full hover:bg-slate-50 text-[var(--accent)] transition-all flex items-center justify-center">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </button>
                    </div>"""
content = content.replace(old_view_toggle, new_view_toggle)


# Change 2: Move the Supplier Invoice No and Supplier Invoice Date
old_supplier_section = """            <!-- Supplier Section -->
            <div class="mb-8 w-1/3">
                <label class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2 group/tooltip relative">
                    Supplier / Vendor <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> <span class="text-red-500">*</span>
                </label>
                <div class="relative mb-4">
                    <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                        <option>Select Contact (F9)</option>
                    </select>
                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
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

new_supplier_section = """            <!-- Supplier Section -->
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
content = content.replace(old_supplier_section, new_supplier_section)

# Change 3: Make the table border rounded corner
old_th_1 = '<th class="px-4 py-3 text-[12px] font-bold w-12 border-b border-r border-white/20 text-center">'
new_th_1 = '<th class="px-4 py-3 text-[12px] font-bold w-12 border-b border-r border-white/20 text-center rounded-tl-2xl">'
content = content.replace(old_th_1, new_th_1)

old_th_last = '<th class="px-3 py-3 w-12 border-b border-white/20 text-center relative z-[400]">'
new_th_last = '<th class="px-3 py-3 w-12 border-b border-white/20 text-center relative z-[400] rounded-tr-2xl">'
content = content.replace(old_th_last, new_th_last)

# Change 4: Change settings icon background to primary color
old_settings_icon = """<button onclick="toggleModalMenu(event, 'pbPoSettingsMenu')" class="absolute top-8 -right-8 w-6 h-6 flex items-center justify-center text-slate-400 hover:text-[var(--accent)] transition-colors">"""
new_settings_icon = """<button onclick="toggleModalMenu(event, 'pbPoSettingsMenu')" class="absolute top-8 -right-9 w-7 h-7 flex items-center justify-center bg-[var(--accent)] text-white hover:brightness-110 rounded transition-colors shadow-sm">"""
content = content.replace(old_settings_icon, new_settings_icon)

# Change 5: Dropdown buttons (pbPoSettingsMenu)
old_po_save = """<button class="mt-2 px-6 py-2 bg-white text-[var(--accent)] border border-[var(--accent)] rounded font-bold text-[12px] hover:bg-slate-50">Save</button>"""
new_po_save = """<div class="flex gap-2 mt-3 pt-3 border-t border-slate-100">
                                <button class="flex-1 py-1.5 bg-[var(--accent)] text-white rounded font-bold text-[12px] hover:brightness-110 transition-all">Save</button>
                                <button onclick="toggleModalMenu(event, 'pbPoSettingsMenu')" type="button" class="flex-1 py-1.5 bg-slate-700 text-white rounded font-bold text-[12px] hover:bg-slate-800 transition-all">Cancel</button>
                            </div>"""
content = content.replace(old_po_save, new_po_save)

# Change 5b: Dropdown buttons (pbTableSettingsMenu)
old_table_buttons = """<div class="flex gap-2 mt-3 pt-3 border-t border-slate-100">
                                            <button class="px-4 py-1.5 bg-white text-[var(--accent)] border border-[var(--accent)] rounded text-[12px] font-bold hover:bg-slate-50 transition-all">Save</button>
                                            <button class="px-4 py-1.5 bg-slate-100 text-slate-700 rounded text-[12px] font-bold hover:bg-slate-200 transition-all">Cancel</button>
                                        </div>"""
new_table_buttons = """<div class="flex gap-2 mt-3 pt-3 border-t border-slate-100">
                                            <button class="px-4 py-1.5 bg-[var(--accent)] text-white rounded text-[12px] font-bold hover:brightness-110 transition-all">Save</button>
                                            <button onclick="toggleModalMenu(event, 'pbTableSettingsMenu')" type="button" class="px-4 py-1.5 bg-slate-700 text-white rounded text-[12px] font-bold hover:bg-slate-800 transition-all">Cancel</button>
                                        </div>"""
content = content.replace(old_table_buttons, new_table_buttons)


with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied styling fixes successfully!")
