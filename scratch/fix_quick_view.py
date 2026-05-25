import re

with open('templates/purchase_bill.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The original switchPbView is around line 1848
old_func_pattern = re.compile(r'    function switchPbView\(viewType\) \{.*?\n    \}\n', re.DOTALL)
match = old_func_pattern.search(content)

if match:
    content = content[:match.start()] + content[match.end():]
    print('Old function removed.')

script_html = """
<script>
    function switchPbView(viewName) {
        if (viewName === 'Normal View') {
            document.getElementById('pbNormalViewContent').classList.remove('hidden');
            document.getElementById('pbNormalViewContent').classList.add('flex');
            document.getElementById('pbQuickViewContent').classList.add('hidden');
            document.getElementById('pbQuickViewContent').classList.remove('flex');
            
            const tabsContainer = document.getElementById('pbQuickTabsContainer');
            if (tabsContainer) {
                tabsContainer.classList.add('hidden');
                tabsContainer.classList.remove('flex');
            }
            
            // update toggle buttons
            document.getElementById('pbViewNormalBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2";
            document.getElementById('pbViewQuickBtn').className = "w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2";
        } else {
            document.getElementById('pbNormalViewContent').classList.add('hidden');
            document.getElementById('pbNormalViewContent').classList.remove('flex');
            document.getElementById('pbQuickViewContent').classList.remove('hidden');
            document.getElementById('pbQuickViewContent').classList.add('flex', 'flex-1'); // Make sure it fills height
            
            // show tabs only if cash mode is selected
            const cashBtn = document.getElementById('btnPbCashToggle');
            const tabsContainer = document.getElementById('pbQuickTabsContainer');
            if (cashBtn && cashBtn.classList.contains('bg-[#1e73be]') && tabsContainer) {
                tabsContainer.classList.remove('hidden');
                tabsContainer.classList.add('flex');
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
            
            if(tabsContainer) {
                tabsContainer.classList.remove('hidden');
                tabsContainer.classList.add('flex');
            }
            
            if(chargesRow) {
                chargesRow.classList.remove('hidden');
                chargesRow.classList.add('flex');
            }
            
            const numTabs = document.querySelectorAll('.pbQuickTabBtn').length;
            if(quickPbTitle) quickPbTitle.innerText = 'INV' + (numTabs > 0 ? numTabs : 1);
        } else {
            creditBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-[#1e73be] text-white transition-colors w-20 text-center";
            cashBtn.className = "px-5 py-1.5 text-[13px] font-bold bg-white text-[#1e73be] transition-colors w-20 text-center border-r border-[#1e73be]";
            
            titleLabel.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            
            if(tabsContainer) {
                tabsContainer.classList.add('hidden');
                tabsContainer.classList.remove('flex');
            }
            
            if(chargesRow) {
                chargesRow.classList.add('hidden');
                chargesRow.classList.remove('flex');
            }
            
            if(quickPbTitle) quickPbTitle.innerText = '1';
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
        const cashBtn = document.getElementById('btnPbCashToggle');
        if(cashBtn && cashBtn.classList.contains('bg-[#1e73be]')) {
            document.getElementById('quickPbTitle').innerText = 'INV' + pbTabCount;
        }
    }

    function selectPbQuickTab(selectedBtn) {
        const btns = document.querySelectorAll('.pbQuickTabBtn');
        btns.forEach(btn => {
            btn.className = "pbQuickTabBtn px-4 h-8 bg-white/10 hover:bg-white/20 text-white text-[13px] font-black rounded-md relative shadow-sm transition-all";
            const ind = btn.querySelector('.pbQuickTabIndicator');
            if(ind) ind.classList.add('hidden');
        });
        
        selectedBtn.className = "pbQuickTabBtn px-4 h-8 bg-white text-[var(--accent)] text-[13px] font-black rounded-md relative shadow-sm transition-all pbQuickTabActive";
        const selectedInd = selectedBtn.querySelector('.pbQuickTabIndicator');
        if(selectedInd) selectedInd.classList.remove('hidden');
    }
</script>
"""

content += '\n' + script_html

with open('templates/purchase_bill.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Script appended.')
