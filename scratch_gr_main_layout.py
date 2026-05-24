import os
import re

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the main page content layout (from {% block content %} to the start of the modal)
# with the exact layout used in purchase_quotes.html, adjusted for Goods Receipt fields.

new_main_content = """{% block content %}
<div class="p-8 stagger-in max-w-[1600px] mx-auto">
    <!-- Header Section -->
    <div class="flex items-center justify-between mb-8 relative z-[300]">
        <div class="flex items-center gap-4 flex-1 mr-6">
            <div>
                <h1 class="text-[32px] font-black text-slate-800 tracking-tight flex items-center gap-3">
                    Goods Receipt
                    <div class="relative group">
                        <svg class="w-6 h-6 text-slate-400 hover:text-slate-600 transition-colors cursor-pointer" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                        <!-- Title Dropdown Menu -->
                        <div id="grTitleDropdownMenu" class="hidden absolute top-full left-0 mt-2 w-64 bg-white rounded-xl shadow-2xl border border-slate-100 p-2 z-[500]">
                            <div class="px-3 py-2 text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1">Recent Receipts</div>
                            <a href="#" class="block px-3 py-2 hover:bg-slate-50 rounded-lg transition-colors">
                                <div class="flex items-center justify-between">
                                    <span class="text-[13px] font-bold text-slate-700">GR-2024-001</span>
                                    <span class="text-[11px] font-medium text-slate-400">2 mins ago</span>
                                </div>
                            </a>
                            <a href="#" class="block px-3 py-2 hover:bg-slate-50 rounded-lg transition-colors">
                                <div class="flex items-center justify-between">
                                    <span class="text-[13px] font-bold text-slate-700">GR-2024-002</span>
                                    <span class="text-[11px] font-medium text-slate-400">1 hr ago</span>
                                </div>
                            </a>
                            <div class="h-px bg-slate-100 my-2"></div>
                            <a href="#" class="block px-3 py-2 text-[12px] font-bold text-[var(--accent)] hover:bg-slate-50 rounded-lg transition-colors text-center">
                                View All Receipts
                            </a>
                        </div>
                    </div>
                </h1>
                <div class="flex items-center gap-3 mt-2 text-[13px] font-medium text-slate-500">
                    <a href="#" class="hover:text-[var(--accent)] transition-colors">Purchase</a>
                    <span class="w-1.5 h-1.5 rounded-full bg-slate-300"></span>
                    <span class="text-slate-700 font-bold">Goods Receipt</span>
                </div>
            </div>

            <!-- Compact Count Pills (like purchase_quotes.html) -->
            <div class="flex-1 flex items-center justify-around bg-white border border-slate-200 rounded-2xl px-8 py-4 shadow-sm max-w-[800px] ml-6">
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Total</span>
                    <span class="text-[30px] font-black text-slate-700 leading-none">0</span>
                </div>
                <div class="w-px h-12 bg-slate-200"></div>
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Active</span>
                    <span class="text-[30px] font-black text-emerald-500 leading-none">0</span>
                </div>
                <div class="w-px h-12 bg-slate-200"></div>
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Void</span>
                    <span class="text-[30px] font-black text-amber-500 leading-none">0</span>
                </div>
            </div>
        </div>
        <div class="flex items-center gap-3">
            <!-- Recent Navigator (like purchase_quotes.html) -->
            <div class="relative">
                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-[var(--accent)] z-10 border-2 border-white"></div>
                <div class="flex items-center bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden h-[52px]">
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-r border-slate-200">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <div class="px-5 flex flex-col items-center min-w-[80px]">
                        <span class="text-[9px] font-black text-slate-400 uppercase tracking-widest leading-none mb-1">Recent</span>
                        <span class="text-[14px] font-black text-slate-700 leading-none">-</span>
                    </div>
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-l border-slate-200">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                </div>
            </div>

            <!-- New Button -->
            <button type="button" onclick="toggleModal('newGoodsReceiptModal')" class="px-8 py-3.5 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Goods Receipt
            </button>
        </div>
    </div>

    <!-- Actions Section (like purchase_quotes.html) -->
    <div class="flex items-center justify-end mb-6 relative z-[200]">
        <div class="flex items-center gap-4">
            <!-- Export Split Button -->
            <div class="relative group/export">
                <div class="flex items-center rounded-xl overflow-hidden shadow-sm h-10">
                    <button onclick="toggleActionMenu(event, 'grExportFormMenu')" class="px-4 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all border-r border-white/20 flex items-center justify-center">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                    </button>
                    <button onclick="toggleActionMenu(event, 'grExportMenu')" class="px-3 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all flex items-center justify-center">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </button>
                </div>
                <!-- Left Click Export Form -->
                <div id="grExportFormMenu" class="hidden absolute top-full right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-slate-100 p-5 z-[500]">
                    <div class="absolute -top-1.5 right-10 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Method</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>List</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Type</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 pl-8 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>PDF</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute left-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 pt-1">
                            <div class="relative w-1/2">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] font-medium text-slate-700 outline-none appearance-none">
                                    <option>This Fiscal Year</option>
                                </select>
                                <svg class="w-3.5 h-3.5 text-slate-500 absolute right-2 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                            <div class="flex items-center gap-1">
                                <span class="text-[12px] font-medium text-slate-600">Apr 1, 2026 - Mar 31, 2027</span>
                                <div class="flex flex-col">
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 14l5-5 5 5z"/></svg>
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-center gap-2 pt-4">
                            <button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>
                            <button class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all">Cancel</button>
                        </div>
                    </div>
                </div>
                <!-- Export Menu (Right Click) -->
                <div id="grExportMenu" class="hidden absolute top-full right-0 mt-2 w-48 bg-white rounded-2xl shadow-2xl border border-slate-100 py-2 z-[500]">
                    <button class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all">Import XLS</button>
                    <button class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all">Export XLS</button>
                </div>
            </div>

            <!-- Filter Button -->
            <div class="relative group/filter">
                <button onclick="toggleActionMenu(event, 'grFilterMenu')" class="w-10 h-10 flex items-center justify-center bg-[var(--accent)] text-white hover:brightness-110 rounded-xl transition-all shadow-sm">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
                </button>
                <div id="grFilterMenu" class="hidden absolute top-full right-0 mt-2 w-[350px] bg-white rounded-[32px] shadow-2xl border border-slate-100 p-8 z-[500]">
                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-2">
                            <h4 class="text-[13px] font-black text-slate-800">Accounts</h4>
                            <input type="text" class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold outline-none focus:border-[var(--accent)]">
                        </div>
                        <div class="flex gap-3 justify-end pt-2">
                            <button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold hover:brightness-110 transition-all">Search</button>
                            <button class="px-6 py-3 bg-slate-700 text-white rounded-xl text-[13px] font-bold hover:bg-slate-800 transition-all">Clear</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Settings Button -->
            <div class="relative group/settings">
                <button onclick="toggleActionMenu(event, 'grSettingsMenu')" class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>
                </button>
                <div id="grSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded-2xl shadow-2xl border border-slate-100 p-4 z-[500]">
                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-3">
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Ref.No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Due Days</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-[var(--accent)] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-100 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Status</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-[var(--accent)] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-100 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Due Amount</span>
                        </label>
                        
                        <div class="h-px bg-slate-100 my-3"></div>
                        
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Supplier Delivery Chalan No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Supplier Delivery Chalan Date</span>
                        </label>
                        
                        <button class="w-full mt-2 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Table Section (like purchase_quotes.html) -->
    <div class="bg-white rounded-3xl border border-slate-100 shadow-sm overflow-hidden mb-6">
        <div class="overflow-x-auto custom-scrollbar">
            <table class="w-full text-left border-collapse">
                <thead class="bg-[var(--accent)] border-b border-slate-200">
                    <tr>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Date</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Receipt No</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Contact</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Status</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Amount</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                    <tr>
                        <td colspan="6" class="px-6 py-4 text-center text-[13px] font-bold text-slate-700">
                            No Records Found
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>"""

# Replace the block from `{% block content %}` to `<!-- New Goods Receipt Modal -->`
new_content = re.sub(
    r'\{\%\s*block content\s*\%\}.*?(?=<!-- New Goods Receipt Modal -->)',
    new_main_content + "\n\n    ",
    content,
    flags=re.DOTALL
)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated main Goods Receipt layout to perfectly mirror Purchase Quotes.")
