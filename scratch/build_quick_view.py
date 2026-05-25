import re

with open('templates/purchase_bill.html', 'r', encoding='utf-8') as f:
    content = f.read()

tabs_html = """
                <!-- Quick View Tabs (Hidden by default, shown only for Cash) -->
                <div id="pbQuickTabsContainer" class="hidden items-center ml-8 gap-1.5">
                    <div id="pbQuickTabsList" class="flex items-center gap-1.5">
                        <button onclick="selectPbQuickTab(this)" class="pbQuickTabBtn px-4 h-8 bg-white text-[var(--accent)] text-[13px] font-black rounded-md relative shadow-sm transition-all pbQuickTabActive">
                            Tab 1
                            <div class="absolute -bottom-[4px] left-1/2 -translate-x-1/2 w-2 h-2 bg-white rotate-45 pbQuickTabIndicator pointer-events-none"></div>
                        </button>
                    </div>
                    <button onclick="addPbQuickTab()" class="w-8 h-8 flex items-center justify-center bg-white/20 hover:bg-white/30 text-white rounded-md shadow-sm transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
                    </button>
                </div>
"""

# Insert tabs right after View Toggle Split Button
view_toggle_idx = content.find('<!-- View Dropdown -->')
if view_toggle_idx != -1:
    view_toggle_end = content.find('</div>\n                </div>', view_toggle_idx)
    if view_toggle_end != -1:
        insert_pos = view_toggle_end + len('</div>\n                </div>')
        content = content[:insert_pos] + "\n" + tabs_html + content[insert_pos:]

quick_view_html = """
        <!-- Quick View Section -->
        <div id="pbQuickViewContent" class="hidden flex-1 flex-col overflow-y-auto bg-slate-50 custom-scrollbar">
            <div class="px-8 py-6 shrink-0 flex justify-between items-start border-b border-slate-200 bg-white">
                <div class="flex flex-col gap-4">
                    <div>
                        <h2 id="quickPbTitle" class="text-[24px] font-black text-slate-800 leading-none">1</h2>
                        <span class="text-[13px] font-bold text-slate-500">25/05/2026</span>
                    </div>
                    <div class="w-80">
                        <div class="flex items-center gap-1 mb-1 text-[15px] text-slate-800 relative group/enterItem">
                            Enter 
                            <button onclick="toggleModalMenu(event, 'pbEnterItemMenu')" class="text-[var(--accent)] font-bold flex items-center gap-1 hover:underline outline-none" id="pbEnterItemLabel">
                                Item <span class="text-[10px]">▼</span>
                            </button>
                            <!-- Dropdown -->
                            <div id="pbEnterItemMenu" class="hidden absolute top-full left-10 mt-1 w-48 bg-white shadow-xl border border-slate-200 rounded py-1 z-[600]">
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Invoice No</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Date</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Contact/Item</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Supplier Invoice No</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Supplier Invoice Date</button>
                                <button class="w-full text-left px-4 py-2 text-[13px] text-white bg-[#1e73be] font-bold">Item</button>
                            </div>
                        </div>
                        <input type="text" id="pbItemSearch" placeholder="Search" class="w-full h-10 border border-slate-300 rounded px-3 text-[14px] font-bold text-slate-700 outline-none focus:border-[var(--accent)]">
                    </div>
                </div>

                <div class="flex flex-col items-end gap-6">
                    <!-- Cash / Credit Toggle -->
                    <div class="flex items-center rounded border border-[#1e73be] overflow-hidden shadow-sm">
                        <button type="button" id="btnPbCashToggle" onclick="setPbInvoiceType('Cash')" class="px-5 py-1.5 text-[13px] font-bold bg-white text-[#1e73be] transition-colors w-20 text-center border-r border-[#1e73be]">Cash</button>
                        <button type="button" id="btnPbCreditToggle" onclick="setPbInvoiceType('Credit')" class="px-5 py-1.5 text-[13px] font-bold bg-[#1e73be] text-white transition-colors w-20 text-center">Credit</button>
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
            <div class="p-6">
                <div class="border border-slate-200 bg-white rounded shadow-sm">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-slate-200 text-slate-800 bg-white">
                                    <div class="flex items-center justify-between">
                                        Item
                                        <div class="flex items-center gap-1 text-slate-400">
                                            <svg class="w-4 h-4 cursor-pointer hover:text-[var(--accent)]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 11h2v2h-2v-2zm-4 0h2v2H8v-2zm8 0h2v2h-2v-2zm-8-4h2v2H8V7zm4 0h2v2h-2V7zm4 0h2v2h-2V7zm-8 8h2v2H8v-2zm4 0h2v2h-2v-2zm4 0h2v2h-2v-2zM4 3h16a1 1 0 011 1v16a1 1 0 01-1 1H4a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg>
                                            <div class="relative group/help">
                                                <svg class="w-4 h-4 cursor-pointer hover:text-[var(--accent)]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                                                <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-[220px] bg-white text-slate-700 text-[11px] font-medium p-3 rounded shadow-xl border border-slate-100 opacity-0 invisible group-hover/help:opacity-100 group-hover/help:visible transition-all z-[1000] text-center normal-case">
                                                    Click it to enter Detailed information about the item
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </th>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-slate-200 text-slate-800 bg-slate-50 w-24 text-center">Qty</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-slate-200 text-slate-800 bg-slate-50 w-32 text-center">Rate ₹</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-slate-200 text-slate-800 bg-slate-50 w-28 text-center">Discount</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-slate-200 text-slate-800 bg-slate-50 w-32 text-center">Amount</th>
                                <th class="w-10 border-b border-slate-200 bg-slate-50"></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0"></td>
                            </tr>
                            <tr>
                                <td class="p-0 border-r border-slate-100"><div class="h-10"></div></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0"></td>
                            </tr>
                            <tr>
                                <td class="p-0 border-r border-slate-100"><div class="h-10"></div></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0 border-r border-slate-100"></td>
                                <td class="p-0"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Subtotals -->
                <div class="flex flex-col items-end pt-4 pr-16 space-y-3 pb-8">
                    <div class="flex items-center w-64 justify-between">
                        <span class="text-[13px] font-bold text-slate-800">Sub Total</span>
                        <span class="text-[13px] text-slate-700"></span>
                    </div>
                    <div class="flex items-center w-64 justify-between">
                        <span class="text-[13px] text-slate-600 italic">less <span class="not-italic font-bold text-slate-800">Discount</span></span>
                        <input type="text" value="0" class="w-24 h-8 border border-slate-200 rounded px-3 text-[13px] text-right outline-none focus:border-[var(--accent)] bg-white text-slate-700">
                    </div>
                    <div id="pbCashOnlyCharges" class="hidden items-center w-64 justify-between">
                        <span class="text-[13px] text-slate-600">Packing and Forwarding Charges</span>
                        <span class="text-[13px] text-slate-300">0.00</span>
                    </div>
                    <div class="flex items-center w-64 justify-between pt-3 border-t border-slate-200">
                        <span class="text-[14px] font-bold text-slate-800">Total</span>
                        <span class="text-[16px] font-bold text-slate-800">₹0.00</span>
                    </div>
                </div>
            </div>
        </div>
"""

normal_view_end = content.find('</div>\n\n    </div>\n</div>\n\n<!-- New Cash Purchase Modal -->')
if normal_view_end != -1:
    content = content[:normal_view_end] + "\n" + quick_view_html + content[normal_view_end:]

script_html = """
<script>
    function switchPbView(viewName) {
        if (viewName === 'Normal View') {
            document.getElementById('pbNormalViewContent').classList.remove('hidden');
            document.getElementById('pbNormalViewContent').classList.add('flex');
            document.getElementById('pbQuickViewContent').classList.add('hidden');
            document.getElementById('pbQuickViewContent').classList.remove('flex');
            document.getElementById('pbQuickTabsContainer').classList.add('hidden');
            document.getElementById('pbQuickTabsContainer').classList.remove('flex');
            
            // update toggle buttons
            document.getElementById('pbViewNormalBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2";
            document.getElementById('pbViewQuickBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2";
        } else {
            document.getElementById('pbNormalViewContent').classList.add('hidden');
            document.getElementById('pbNormalViewContent').classList.remove('flex');
            document.getElementById('pbQuickViewContent').classList.remove('hidden');
            document.getElementById('pbQuickViewContent').classList.add('flex');
            
            // show tabs only if cash mode is selected
            if (document.getElementById('btnPbCashToggle').classList.contains('bg-[#1e73be]')) {
                document.getElementById('pbQuickTabsContainer').classList.remove('hidden');
                document.getElementById('pbQuickTabsContainer').classList.add('flex');
            }
            
            document.getElementById('pbViewQuickBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2";
            document.getElementById('pbViewNormalBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2";
        }
        document.getElementById('pbViewMenu').classList.add('hidden');
    }

    function setPbInvoiceType(type) {
        const cashBtn = document.getElementById('btnPbCashToggle');
        const creditBtn = document.getElementById('btnPbCreditToggle');
        const titleLabel = document.querySelector('#newPurchaseModal h2');
        const tabsContainer = document.getElementById('pbQuickTabsContainer');
        const chargesRow = document.getElementById('pbCashOnlyCharges');
        const quickPbTitle = document.getElementById('quickPbTitle');

        if (type === 'Cash') {
            cashBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-[#1e73be] text-white transition-colors w-20 text-center border-r border-[#1e73be]";
            creditBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-white text-[#1e73be] transition-colors w-20 text-center";
            
            // Header text
            titleLabel.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            
            tabsContainer.classList.remove('hidden');
            tabsContainer.classList.add('flex');
            
            chargesRow.classList.remove('hidden');
            chargesRow.classList.add('flex');
            
            quickPbTitle.innerText = 'INV' + document.querySelectorAll('.pbQuickTabBtn').length;
        } else {
            creditBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-[#1e73be] text-white transition-colors w-20 text-center";
            cashBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-white text-[#1e73be] transition-colors w-20 text-center border-r border-[#1e73be]";
            
            titleLabel.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            
            tabsContainer.classList.add('hidden');
            tabsContainer.classList.remove('flex');
            
            chargesRow.classList.add('hidden');
            chargesRow.classList.remove('flex');
            
            quickPbTitle.innerText = '1';
        }
    }

    let pbTabCount = 1;
    function addPbQuickTab() {
        pbTabCount++;
        const tabsList = document.getElementById('pbQuickTabsList');
        
        // create new tab button
        const newTab = document.createElement('button');
        newTab.onclick = function() { selectPbQuickTab(this); };
        newTab.className = "pbQuickTabBtn px-4 h-8 bg-white/10 hover:bg-white/20 text-white text-[13px] font-black rounded-md relative shadow-sm transition-all";
        newTab.innerHTML = `Tab ${pbTabCount} <div class="absolute -bottom-[4px] left-1/2 -translate-x-1/2 w-2 h-2 bg-white rotate-45 pbQuickTabIndicator pointer-events-none hidden"></div>`;
        
        tabsList.appendChild(newTab);
        
        // select it
        selectPbQuickTab(newTab);
        
        // update invoice number to reflect tab
        if(document.getElementById('btnPbCashToggle').classList.contains('bg-[#1e73be]')) {
            document.getElementById('quickPbTitle').innerText = 'INV' + pbTabCount;
        }
    }

    function selectPbQuickTab(selectedBtn) {
        const btns = document.querySelectorAll('.pbQuickTabBtn');
        btns.forEach(btn => {
            btn.className = "pbQuickTabBtn px-4 h-8 bg-white/10 hover:bg-white/20 text-white text-[13px] font-black rounded-md relative shadow-sm transition-all";
            btn.querySelector('.pbQuickTabIndicator').classList.add('hidden');
        });
        
        selectedBtn.className = "pbQuickTabBtn px-4 h-8 bg-white text-[var(--accent)] text-[13px] font-black rounded-md relative shadow-sm transition-all pbQuickTabActive";
        selectedBtn.querySelector('.pbQuickTabIndicator').classList.remove('hidden');
    }
</script>
"""

script_insert_idx = content.rfind('</body>')
if script_insert_idx != -1:
    content = content[:script_insert_idx] + script_html + content[script_insert_idx:]

with open('templates/purchase_bill.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quick view injected.")
