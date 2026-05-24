import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1 & 2: Update Cash/Credit toggle to use var(--accent) instead of #1e78b9
content = content.replace(
    'border-[#1e78b9]', 'border-[var(--accent)]'
).replace(
    'text-[#1e78b9]', 'text-[var(--accent)]'
).replace(
    'bg-[#1e78b9]', 'bg-[var(--accent)]'
).replace(
    'focus:border-[#1e78b9]', 'focus:border-[var(--accent)]'
)

# 3: Add Tabs in the header. Find the View Dropdown and insert Tabs right after it.
view_dropdown_html = """                    <!-- View Dropdown -->
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
                    </div>
                </div>"""

tabs_html = """
                <!-- Quick View Tabs (Hidden by default) -->
                <div id="pbQuickTabsContainer" class="hidden items-center ml-8 gap-1">
                    <div id="pbQuickTabsList" class="flex items-center gap-1">
                        <button class="px-4 h-9 bg-slate-100 text-slate-700 text-[13px] font-bold rounded-lg border border-slate-200 relative pbQuickTabBtn">
                            Tab 1
                            <div class="absolute -bottom-[5px] left-1/2 -translate-x-1/2 w-2.5 h-2.5 bg-slate-100 border-b border-r border-slate-200 rotate-45 pbQuickTabIndicator"></div>
                        </button>
                    </div>
                    <button onclick="addPbQuickTab()" class="w-9 h-9 flex items-center justify-center bg-white hover:bg-slate-50 text-slate-600 rounded-lg border border-slate-200 transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
                    </button>
                </div>
"""
if tabs_html not in content:
    content = content.replace(view_dropdown_html, view_dropdown_html + tabs_html)

# 5. Table changes (Rounded corners and primary color header)
table_old = """            <!-- Quick View Table -->
            <div class="flex-1 overflow-y-auto bg-white p-6 custom-scrollbar">
                <div class="border border-slate-200 rounded-lg overflow-hidden">
                    <table class="w-full text-left border-collapse">
                        <thead class="bg-slate-50 border-b border-slate-200">
                            <tr>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200">"""

table_new = """            <!-- Quick View Table -->
            <div class="flex-1 overflow-y-auto bg-white p-6 custom-scrollbar">
                <div class="border border-[var(--accent)] rounded-xl overflow-hidden shadow-sm">
                    <table class="w-full text-left border-collapse">
                        <thead class="bg-[var(--accent)] text-white border-b border-[var(--accent)]">
                            <tr>
                                <th class="px-4 py-3 text-[12px] font-bold border-r border-white/20">"""

if table_old in content:
    content = content.replace(table_old, table_new)

# Fix remaining text colors in the Quick view table header
table_th_old = """<th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-24">Qty</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-32">Rate ₹</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 border-r border-slate-200 w-28">Discount</th>
                                <th class="px-4 py-3 text-[12px] font-bold text-slate-800 w-32">Amount</th>"""

table_th_new = """<th class="px-4 py-3 text-[12px] font-bold border-r border-white/20 w-24">Qty</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-r border-white/20 w-32">Rate ₹</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-r border-white/20 w-28">Discount</th>
                                <th class="px-4 py-3 text-[12px] font-bold w-32">Amount</th>"""

if table_th_old in content:
    content = content.replace(table_th_old, table_th_new)

# Fix SVG colors
content = content.replace('<div class="flex items-center gap-1 text-slate-400">', '<div class="flex items-center gap-1 text-white/80">')
content = content.replace('hover:text-blue-500', 'hover:text-white/100')

# In tfoot, add "Packing and Forwarding Charges"
tfoot_old = """                            <tr class="border-b border-slate-100">
                                <td colspan="4" class="px-4 py-2 text-right text-[12px] text-slate-600 border-r border-slate-200">
                                    <span class="italic text-slate-400 mr-1">less</span> Discount
                                </td>
                                <td class="px-4 py-2 text-right text-[12px] border-r border-slate-200">
                                    <input type="text" value="0" class="w-full text-right outline-none">
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td colspan="4" class="px-4 py-3 text-right text-[13px] font-black text-slate-800 border-r border-slate-200">Total</td>"""

tfoot_new = """                            <tr class="border-b border-slate-100">
                                <td colspan="4" class="px-4 py-2 text-right text-[12px] text-slate-600 border-r border-slate-200">
                                    <span class="italic text-slate-400 mr-1">less</span> Discount
                                </td>
                                <td class="px-4 py-2 text-right text-[12px] border-r border-slate-200">
                                    <input type="text" value="0" class="w-full text-right outline-none">
                                </td>
                                <td></td>
                            </tr>
                            <tr id="pbRowPacking" class="hidden border-b border-slate-100 bg-slate-50/50">
                                <td colspan="4" class="px-4 py-2 text-right text-[12px] text-slate-600 border-r border-slate-200">
                                    Packing and Forwarding Charges
                                </td>
                                <td class="px-4 py-2 text-right text-[12px] text-slate-400 border-r border-slate-200">
                                    0.00
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td colspan="4" class="px-4 py-3 text-right text-[13px] font-black text-slate-800 border-r border-slate-200">Total</td>"""

if tfoot_old in content:
    content = content.replace(tfoot_old, tfoot_new)

# Update Javascript
js_old = """    function setPbInvoiceType(type) {
        const cashBtn = document.getElementById('btnPbCashToggle');
        const creditBtn = document.getElementById('btnPbCreditToggle');
        
        if (type === 'Cash') {
            cashBtn.classList.add('bg-[var(--accent)]', 'text-white');
            cashBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            creditBtn.classList.add('bg-white', 'text-[var(--accent)]');
            creditBtn.classList.remove('bg-[var(--accent)]', 'text-white');
        } else {
            creditBtn.classList.add('bg-[var(--accent)]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            cashBtn.classList.add('bg-white', 'text-[var(--accent)]');
            cashBtn.classList.remove('bg-[var(--accent)]', 'text-white');
        }
    }"""

js_new = """    function setPbInvoiceType(type) {
        const cashBtn = document.getElementById('btnPbCashToggle');
        const creditBtn = document.getElementById('btnPbCreditToggle');
        const modalTitle = document.getElementById('modalMainTitle');
        const tabsContainer = document.getElementById('pbQuickTabsContainer');
        const packingRow = document.getElementById('pbRowPacking');
        
        if (type === 'Cash') {
            cashBtn.classList.add('bg-[var(--accent)]', 'text-white');
            cashBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            creditBtn.classList.add('bg-white', 'text-[var(--accent)]');
            creditBtn.classList.remove('bg-[var(--accent)]', 'text-white');
            
            if(modalTitle) modalTitle.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(tabsContainer) {
                tabsContainer.classList.remove('hidden');
                tabsContainer.classList.add('flex');
            }
            if(packingRow) packingRow.classList.remove('hidden');
            
        } else {
            creditBtn.classList.add('bg-[var(--accent)]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            cashBtn.classList.add('bg-white', 'text-[var(--accent)]');
            cashBtn.classList.remove('bg-[var(--accent)]', 'text-white');
            
            if(modalTitle) modalTitle.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(tabsContainer) {
                tabsContainer.classList.add('hidden');
                tabsContainer.classList.remove('flex');
            }
            if(packingRow) packingRow.classList.add('hidden');
        }
    }
    
    let pbTabCount = 1;
    function addPbQuickTab() {
        pbTabCount++;
        const tabsList = document.getElementById('pbQuickTabsList');
        
        // Remove active state from all tabs
        const allTabs = tabsList.querySelectorAll('.pbQuickTabBtn');
        allTabs.forEach(tab => {
            tab.className = 'pbQuickTabBtn px-4 h-9 bg-white text-slate-500 text-[13px] font-medium rounded-lg border border-slate-200 hover:bg-slate-50 transition-colors relative';
            const indicator = tab.querySelector('.pbQuickTabIndicator');
            if(indicator) indicator.remove();
        });
        
        // Add new active tab
        const newTab = document.createElement('button');
        newTab.className = 'pbQuickTabBtn px-4 h-9 bg-slate-100 text-slate-700 text-[13px] font-bold rounded-lg border border-slate-200 relative';
        newTab.innerHTML = `Tab ${pbTabCount} <div class="absolute -bottom-[5px] left-1/2 -translate-x-1/2 w-2.5 h-2.5 bg-slate-100 border-b border-r border-slate-200 rotate-45 pbQuickTabIndicator"></div>`;
        tabsList.appendChild(newTab);
        
        // Focus the search input and make it yellow to simulate Image 4
        const searchInput = document.getElementById('pbItemSearch');
        if(searchInput) {
            searchInput.style.backgroundColor = '#fefce8'; // yellow-50
            searchInput.focus();
        }
    }"""

if js_old in content:
    content = content.replace(js_old, js_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
