import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove POS View HTML Block
start_marker = '        <!-- POS VIEW -->'
end_marker = '<!-- End New Purchase Modal -->'

if start_marker in content:
    idx_start = content.find(start_marker)
    # the modal ends right before the end marker, we need to carefully replace just the pos view
    # since we added it right before '        </div>\n    </div>\n</div>\n<!-- End New Purchase Modal -->'
    # Let's find pbPosViewContent block and remove it.
    pos_start = content.find(start_marker)
    # The end of the block is before '        </div>\n    </div>\n</div>\n<!-- End New Purchase Modal -->'
    insert_marker = '        </div>\n    </div>\n</div>\n<!-- End New Purchase Modal -->'
    pos_end = content.find(insert_marker, pos_start)
    if pos_end != -1:
        content = content[:pos_start] + content[pos_end:]

# 2. Remove POS button from view dropdown
pos_btn_html = """                        <button onclick="switchPbView('POS View')" id="pbViewPOSBtn" class="w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M6 5h12l1 6H5l1-6zm0 0v12c0 1.105.895 2 2 2h8c1.105 0 2-.895 2-2V5M9 5v4m6-4v4"></path></svg>
                            POS View
                        </button>\n"""
content = content.replace(pos_btn_html, "")

# 3. Revert switchPbView function
js_new = """    function switchPbView(viewType) {
        document.getElementById('pbViewMenu').classList.add('hidden');
        
        const normalView = document.getElementById('pbNormalViewContent');
        const quickView = document.getElementById('pbQuickViewContent');
        const posView = document.getElementById('pbPosViewContent');
        
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
            if(normalView) { normalView.classList.remove('hidden'); normalView.classList.add('flex-1'); }
            if(quickView) { quickView.classList.add('hidden'); quickView.classList.remove('flex-1'); }
            if(posView) { posView.classList.add('hidden'); posView.classList.remove('flex-1', 'flex'); }
            if(normalBtn) { normalBtn.classList.add('bg-[var(--accent)]', 'text-white'); normalBtn.classList.remove('text-slate-600'); }
        } else if (viewType === 'Quick View') {
            if(normalView) { normalView.classList.add('hidden'); normalView.classList.remove('flex-1'); }
            if(quickView) { quickView.classList.remove('hidden'); quickView.classList.add('flex-1'); }
            if(posView) { posView.classList.add('hidden'); posView.classList.remove('flex-1', 'flex'); }
            if(quickBtn) { quickBtn.classList.add('bg-[var(--accent)]', 'text-white'); quickBtn.classList.remove('text-slate-600'); }
        } else if (viewType === 'POS View') {
            if(normalView) { normalView.classList.add('hidden'); normalView.classList.remove('flex-1'); }
            if(quickView) { quickView.classList.add('hidden'); quickView.classList.remove('flex-1'); }
            if(posView) { posView.classList.remove('hidden'); posView.classList.add('flex-1', 'flex'); }
            if(posBtn) { posBtn.classList.add('bg-[var(--accent)]', 'text-white'); posBtn.classList.remove('text-slate-600'); }
        }
    }"""

js_old = """    function switchPbView(viewType) {
        document.getElementById('pbViewMenu').classList.add('hidden');
        
        const normalView = document.getElementById('pbNormalViewContent');
        const quickView = document.getElementById('pbQuickViewContent');
        
        const normalBtn = document.getElementById('pbViewNormalBtn');
        const quickBtn = document.getElementById('pbViewQuickBtn');
        
        // Reset buttons
        [normalBtn, quickBtn].forEach(btn => {
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
        }
    }"""

content = content.replace(js_new, js_old)

# 4. Remove POS specific Javascript functions
js_pos_functions = """
    // POS specific functions
    function togglePbPosOrders() {
        const panel = document.getElementById('pbPosOrdersPanel');
        if(panel) {
            panel.classList.toggle('-translate-x-full');
        }
    }
    
    function togglePbPosPin() {
        const icon = document.getElementById('pbPosPinIcon');
        const leftPanel = document.getElementById('pbPosLeftPanel');
        const panel = document.getElementById('pbPosOrdersPanel');
        if(icon) {
            icon.classList.toggle('text-slate-400');
            icon.classList.toggle('text-[#10b981]');
        }
        if(leftPanel && panel) {
            if(icon.classList.contains('text-[#10b981]')) {
                leftPanel.style.marginLeft = '20rem';
            } else {
                leftPanel.style.marginLeft = '0';
                panel.classList.add('-translate-x-full');
            }
        }
    }

    function showPbPosNewSupplierForm() {
        const defaultSection = document.getElementById('pbPosSupplierDefault');
        const newForm = document.getElementById('pbPosSupplierNewForm');
        if(defaultSection && newForm) {
            defaultSection.classList.add('hidden');
            newForm.classList.remove('hidden');
        }
    }

    function hidePbPosNewSupplierForm() {
        const defaultSection = document.getElementById('pbPosSupplierDefault');
        const newForm = document.getElementById('pbPosSupplierNewForm');
        if(defaultSection && newForm) {
            defaultSection.classList.remove('hidden');
            newForm.classList.add('hidden');
        }
    }

    function togglePbPosNewSupplierDetails() {
        const fields = document.getElementById('pbPosNewSupplierExpandedFields');
        const chevron = document.getElementById('pbPosMoreDetailsChevron');
        if(fields && chevron) {
            fields.classList.toggle('hidden');
            chevron.classList.toggle('rotate-180');
        }
    }

    function savePbPosNewSupplier() {
        hidePbPosNewSupplierForm();
    }
"""

content = content.replace(js_pos_functions, "")

# 5. Revert menus array
menus_new = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu', 'pbPosSearchSettings', 'pbPosBuyerRep', 'pbPosCartSettings'];"
menus_old = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu'];"

content = content.replace(menus_new, menus_old)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed POS View successfully")
