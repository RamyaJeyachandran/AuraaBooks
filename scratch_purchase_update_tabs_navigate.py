import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tabs Container to hide by default
# Find pbQuickTabsContainer
tabs_old = """                <!-- Quick View Tabs -->
                <div id="pbQuickTabsContainer" class="flex items-center ml-8 gap-1">"""
tabs_new = """                <!-- Quick View Tabs (Hidden by default, shown only for Cash) -->
                <div id="pbQuickTabsContainer" class="hidden items-center ml-8 gap-1.5">"""
if tabs_old in content:
    content = content.replace(tabs_old, tabs_new)

# 2. Update Tabs List HTML structure
list_old = """                    <div id="pbQuickTabsList" class="flex items-center gap-1">
                        <button class="px-4 h-9 bg-slate-100 text-slate-700 text-[13px] font-bold rounded-lg border border-slate-200 relative pbQuickTabBtn">
                            Tab 1
                            <div class="absolute -bottom-[5px] left-1/2 -translate-x-1/2 w-2.5 h-2.5 bg-slate-100 border-b border-r border-slate-200 rotate-45 pbQuickTabIndicator"></div>
                        </button>
                    </div>
                    <button onclick="addPbQuickTab()" class="w-9 h-9 flex items-center justify-center bg-white hover:bg-slate-50 text-slate-600 rounded-lg border border-slate-200 transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
                    </button>"""

list_new = """                    <div id="pbQuickTabsList" class="flex items-center gap-1.5">
                        <button onclick="selectPbQuickTab(this)" class="pbQuickTabBtn px-4 h-8 bg-[#f8fafc] text-[var(--accent)] text-[13px] font-black rounded-md relative shadow-sm transition-all pbQuickTabActive">
                            Tab 1
                            <div class="absolute -bottom-[4px] left-1/2 -translate-x-1/2 w-2 h-2 bg-[#f8fafc] rotate-45 pbQuickTabIndicator pointer-events-none"></div>
                        </button>
                    </div>
                    <button onclick="addPbQuickTab()" class="w-8 h-8 flex items-center justify-center bg-white hover:bg-slate-50 text-[var(--accent)] rounded-md shadow-sm transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
                    </button>"""

if list_old in content:
    content = content.replace(list_old, list_new)

# 3. Update Javascript setPbInvoiceType to toggle the tabs visibility again
js_old = """            if(modalTitle) modalTitle.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(packingRow) packingRow.classList.remove('hidden');
            
        } else {
            creditBtn.classList.add('bg-[var(--accent)]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            cashBtn.classList.add('bg-white', 'text-[var(--accent)]');
            cashBtn.classList.remove('bg-[var(--accent)]', 'text-white');
            
            if(modalTitle) modalTitle.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(packingRow) packingRow.classList.add('hidden');
        }"""

js_new = """            if(modalTitle) modalTitle.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
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
        }"""

if js_old in content:
    content = content.replace(js_old, js_new)

# 4. Update the Javascript addPbQuickTab and add selectPbQuickTab
js_tabs_old = """    let pbTabCount = 1;
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

js_tabs_new = """    let pbTabCount = 1;
    
    function selectPbQuickTab(selectedTab) {
        const tabsList = document.getElementById('pbQuickTabsList');
        const allTabs = tabsList.querySelectorAll('.pbQuickTabBtn');
        
        // Remove active state from all tabs
        allTabs.forEach(tab => {
            tab.className = 'pbQuickTabBtn px-4 h-8 bg-white hover:bg-slate-50 text-[var(--accent)] text-[13px] font-medium rounded-md transition-colors';
            const indicator = tab.querySelector('.pbQuickTabIndicator');
            if(indicator) indicator.remove();
        });
        
        // Set selected tab to active state
        selectedTab.className = 'pbQuickTabBtn px-4 h-8 bg-[#f8fafc] text-[var(--accent)] text-[13px] font-black rounded-md relative shadow-sm transition-all pbQuickTabActive';
        
        const indicator = document.createElement('div');
        indicator.className = 'absolute -bottom-[4px] left-1/2 -translate-x-1/2 w-2 h-2 bg-[#f8fafc] rotate-45 pbQuickTabIndicator pointer-events-none';
        selectedTab.appendChild(indicator);
        
        // Trigger UI updates (e.g., clearing search or loading data could go here)
        const searchInput = document.getElementById('pbItemSearch');
        if(searchInput) {
            searchInput.style.backgroundColor = 'transparent'; // reset background color
        }
    }
    
    function addPbQuickTab() {
        pbTabCount++;
        const tabsList = document.getElementById('pbQuickTabsList');
        
        // Create the new tab in inactive state
        const newTab = document.createElement('button');
        newTab.onclick = function() { selectPbQuickTab(this); };
        newTab.innerText = `Tab ${pbTabCount}`;
        tabsList.appendChild(newTab);
        
        // Select the newly added tab
        selectPbQuickTab(newTab);
        
        // Focus the search input and make it yellow to simulate Image 4
        const searchInput = document.getElementById('pbItemSearch');
        if(searchInput) {
            searchInput.style.backgroundColor = '#fefce8'; // yellow-50
            searchInput.focus();
        }
    }"""

if js_tabs_old in content:
    content = content.replace(js_tabs_old, js_tabs_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
