import re
import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the normal view content div ID
content = content.replace(
    '        <!-- Body (Scrollable) -->\n        <div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar rounded-b-xl">',
    '        <!-- Body (Scrollable) -->\n        <div id="pbNormalViewContent" class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar rounded-b-xl">'
)

# 2. Add Quick View Content right after pbNormalViewContent closes
# pbNormalViewContent closes right before:
#     </div>
# </div>
# <!-- End New Purchase Modal -->

quick_view_html = """
        <!-- Quick View Section -->
        <div id="pbQuickViewContent" class="hidden flex-1 flex-col h-full overflow-hidden rounded-b-xl">
            <div class="px-8 py-6 shrink-0 flex justify-between items-start border-b border-slate-200 bg-white">
                <div class="flex flex-col gap-4">
                    <div>
                        <h2 id="quickPbTitle" class="text-[24px] font-black text-slate-800 leading-none">1</h2>
                        <span class="text-[13px] font-bold text-slate-500">24/05/2026</span>
                    </div>
                    <div class="w-80">
                        <div class="flex items-center gap-1 mb-1 text-[15px] text-slate-800 relative group/enterItem">
                            Enter 
                            <button onclick="toggleModalMenu(event, 'pbEnterItemMenu')" class="text-[#1e78b9] font-bold flex items-center gap-1 hover:underline outline-none" id="pbEnterItemLabel">
                                Item <span class="text-[10px]">▼</span>
                            </button>
                            <!-- Dropdown -->
                            <div id="pbEnterItemMenu" class="hidden absolute top-full left-10 mt-1 w-48 bg-white shadow-xl border border-slate-200 rounded py-1 z-[600]">
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Invoice No</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Date</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Contact/Item</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Supplier Invoice No</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Supplier Invoice Date</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-white bg-[#1e78b9] font-bold">Item</button>
                            </div>
                        </div>
                        <input type="text" id="pbItemSearch" placeholder="Search" class="w-full h-10 border border-slate-300 rounded px-3 text-[14px] font-bold text-slate-700 outline-none focus:border-[#1e78b9]">
                    </div>
                </div>

                <div class="flex flex-col items-end gap-6">
                    <!-- Cash / Credit Toggle -->
                    <div class="flex items-center rounded border border-[#1e78b9] overflow-hidden shadow-sm">
                        <button type="button" id="btnPbCashToggle" onclick="setPbInvoiceType('Cash')" class="px-4 py-1.5 text-[13px] font-bold bg-white text-[#1e78b9] transition-colors w-16 text-center">Cash</button>
                        <button type="button" id="btnPbCreditToggle" onclick="setPbInvoiceType('Credit')" class="px-4 py-1.5 text-[13px] font-bold bg-[#1e78b9] text-white transition-colors w-16 text-center">Credit</button>
                    </div>
                    
                    <div class="flex items-center gap-3 relative group/settings">
                        <span class="text-[28px] font-black text-slate-800">₹0.00</span>
                        <button type="button" onclick="toggleModalMenu(event, 'pbQuickSettingsMenu')" class="text-slate-500 hover:text-slate-700 outline-none">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287-.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path></svg>
                        </button>
                        <!-- Settings Popover -->
                        <div id="pbQuickSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded shadow-2xl border border-slate-200 py-3 z-[600]">
                            <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t border-l border-slate-200 rotate-45"></div>
                            <div class="space-y-1">
                                <button class="w-full text-left px-5 py-1.5 text-[13px] text-slate-700 hover:bg-slate-50">Skip Rate if defined in Item</button>
                                <button class="w-full text-left px-5 py-1.5 text-[13px] text-slate-700 hover:bg-slate-50">Skip Quantity with value as 1</button>
                                <button class="w-full text-left px-5 py-1.5 text-[13px] text-slate-700 hover:bg-slate-50">Skip / Hide Discount if defined in Item</button>
                                <div class="h-px bg-slate-200 mx-5 my-1"></div>
                                <button class="w-full text-left px-5 py-1.5 text-[13px] text-slate-700 hover:bg-slate-50 flex items-center gap-2">
                                    <span class="text-green-500 font-bold">✓</span> Discount Overall
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quick View Table -->
            <div class="flex-1 overflow-y-auto bg-white p-6 custom-scrollbar">
                <div class="border border-slate-200 rounded-lg overflow-hidden">
                    <table class="w-full text-left border-collapse">
                        <thead class="bg-slate-50 border-b border-slate-200">
                            <tr>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200">
                                    <div class="flex items-center justify-between">
                                        Item
                                        <div class="flex items-center gap-1 text-slate-400">
                                            <svg class="w-4 h-4 cursor-pointer hover:text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 11h2v2h-2v-2zm-4 0h2v2H8v-2zm8 0h2v2h-2v-2zm-8-4h2v2H8V7zm4 0h2v2h-2V7zm4 0h2v2h-2V7zm-8 8h2v2H8v-2zm4 0h2v2h-2v-2zm4 0h2v2h-2v-2zM4 3h16a1 1 0 011 1v16a1 1 0 01-1 1H4a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg>
                                            <div class="relative group/help">
                                                <svg class="w-4 h-4 cursor-pointer hover:text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                                                <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-[220px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/help:opacity-100 group-hover/help:visible transition-all z-[1000] text-center normal-case">
                                                    Click it to enter Detailed information about the item
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-24">Qty</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-32">Rate ₹</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-28">Discount</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 w-32">Amount</th>
                                <th class="w-10"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-slate-100 h-10">
                                <td class="border-r border-slate-200"></td>
                                <td class="border-r border-slate-200"></td>
                                <td class="border-r border-slate-200"></td>
                                <td class="border-r border-slate-200"></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                        <tfoot class="border-t border-slate-200">
                            <tr class="border-b border-slate-100">
                                <td colspan="4" class="px-4 py-2 text-right text-[12px] font-bold text-slate-600 border-r border-slate-200">Sub Total</td>
                                <td class="px-4 py-2 text-right text-[12px] text-slate-600 border-r border-slate-200"></td>
                                <td></td>
                            </tr>
                            <tr class="border-b border-slate-100">
                                <td colspan="4" class="px-4 py-2 text-right text-[12px] text-slate-600 border-r border-slate-200">
                                    <span class="italic text-slate-400 mr-1">less</span> Discount
                                </td>
                                <td class="px-4 py-2 text-right text-[12px] border-r border-slate-200">
                                    <input type="text" value="0" class="w-full text-right outline-none">
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td colspan="4" class="px-4 py-3 text-right text-[13px] font-black text-slate-800 border-r border-slate-200">Total</td>
                                <td class="px-4 py-3 text-right text-[13px] font-black text-slate-800 border-r border-slate-200">₹0.00</td>
                                <td></td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        </div>
"""

content = content.replace(
    '        </div>\n    </div>\n</div>\n<!-- End New Purchase Modal -->',
    '        </div>\n' + quick_view_html + '\n    </div>\n</div>\n<!-- End New Purchase Modal -->'
)

# 3. Update the view dropdown
view_dropdown_old = """                    <!-- View Dropdown -->
                    <div id="pbViewMenu" class="hidden absolute top-full left-0 mt-1 w-40 bg-white rounded-lg shadow-xl border border-slate-100 py-1 z-[600] text-slate-800">
                        <button class="w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg>
                            Normal View
                        </button>
                        <button class="w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                            Quick View
                        </button>
                    </div>"""

view_dropdown_new = """                    <!-- View Dropdown -->
                    <div id="pbViewMenu" class="hidden absolute top-full left-0 mt-1 w-40 bg-white rounded-lg shadow-xl border border-slate-100 py-1 z-[600] text-slate-800">
                        <button onclick="switchPbView('Normal View')" id="pbViewNormalBtn" class="w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg>
                            Normal View
                        </button>
                        <button onclick="switchPbView('Quick View')" id="pbViewQuickBtn" class="w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                            Quick View
                        </button>
                        <button onclick="switchPbView('POS View')" id="pbViewPOSBtn" class="w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M6 5h12l1 6H5l1-6zm0 0v12c0 1.105.895 2 2 2h8c1.105 0 2-.895 2-2V5M9 5v4m6-4v4"></path></svg>
                            POS View
                        </button>
                    </div>"""

content = content.replace(view_dropdown_old, view_dropdown_new)

# 4. Add the switchPbView and setPbInvoiceType script at the bottom inside the <script> block
script_insert = """
    function switchPbView(viewType) {
        document.getElementById('pbViewMenu').classList.add('hidden');
        
        const normalView = document.getElementById('pbNormalViewContent');
        const quickView = document.getElementById('pbQuickViewContent');
        
        const normalBtn = document.getElementById('pbViewNormalBtn');
        const quickBtn = document.getElementById('pbViewQuickBtn');
        const posBtn = document.getElementById('pbViewPOSBtn');
        
        // Reset buttons
        [normalBtn, quickBtn, posBtn].forEach(btn => {
            if(btn) {
                btn.classList.remove('bg-[var(--accent)]', 'text-white');
                btn.classList.add('text-slate-600');
            }
        });
        
        if (viewType === 'Normal View') {
            if(normalView) {
                normalView.classList.remove('hidden');
                normalView.classList.add('flex-1');
            }
            if(quickView) {
                quickView.classList.add('hidden');
                quickView.classList.remove('flex-1');
            }
            if(normalBtn) {
                normalBtn.classList.add('bg-[var(--accent)]', 'text-white');
                normalBtn.classList.remove('text-slate-600');
            }
        } else if (viewType === 'Quick View') {
            if(normalView) {
                normalView.classList.add('hidden');
                normalView.classList.remove('flex-1');
            }
            if(quickView) {
                quickView.classList.remove('hidden');
                quickView.classList.add('flex-1');
            }
            if(quickBtn) {
                quickBtn.classList.add('bg-[var(--accent)]', 'text-white');
                quickBtn.classList.remove('text-slate-600');
            }
        } else if (viewType === 'POS View') {
            if(posBtn) {
                posBtn.classList.add('bg-[var(--accent)]', 'text-white');
                posBtn.classList.remove('text-slate-600');
            }
        }
    }
    
    function setPbInvoiceType(type) {
        const cashBtn = document.getElementById('btnPbCashToggle');
        const creditBtn = document.getElementById('btnPbCreditToggle');
        
        if (type === 'Cash') {
            cashBtn.classList.add('bg-[#1e78b9]', 'text-white');
            cashBtn.classList.remove('bg-white', 'text-[#1e78b9]');
            
            creditBtn.classList.add('bg-white', 'text-[#1e78b9]');
            creditBtn.classList.remove('bg-[#1e78b9]', 'text-white');
        } else {
            creditBtn.classList.add('bg-[#1e78b9]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[#1e78b9]');
            
            cashBtn.classList.add('bg-white', 'text-[#1e78b9]');
            cashBtn.classList.remove('bg-[#1e78b9]', 'text-white');
        }
    }
"""

content = content.replace(
    '    function openNewPurchaseModal() {',
    script_insert + '\n    function openNewPurchaseModal() {'
)

# Also ensure menus get closed properly for the new menus
# The menus to add are 'pbEnterItemMenu', 'pbQuickSettingsMenu'
content = content.replace(
    "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu'];",
    "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu'];"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
