import os

sales_filepath = r"d:\AuraaZenAIProject\abproject\templates\sales_invoices.html"
purchase_filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

# Extract POS View from sales_invoices.html
with open(sales_filepath, 'r', encoding='utf-8') as f:
    sales_content = f.read()

start_tag = '<!-- POS VIEW -->'
end_tag = '        </div>\n</div>\n\n    </div>\n</div>\n{% endblock %}'
pos_view_raw = ""
if start_tag in sales_content:
    start_idx = sales_content.find(start_tag)
    # The end of the pos view div is line 1384, just before the end of the modal.
    # Let's do a robust extraction by reading lines
    lines = sales_content.splitlines()
    pos_lines = []
    in_pos = False
    for line in lines:
        if line.strip() == '<!-- POS VIEW -->':
            in_pos = True
        if in_pos:
            pos_lines.append(line)
        if in_pos and line.strip() == '</div>' and pos_lines.count('        <div id="posViewContent"') == 1:
            # We need to trace the divs carefully, let's just use string slicing
            pass

# Instead of parsing, I will just extract using exact known strings:
start_str = '        <!-- POS VIEW -->'
end_str = '        </div>\n</div>\n\n    </div>\n</div>'
start_idx = sales_content.find(start_str)
end_idx = sales_content.find(end_str)
pos_html = sales_content[start_idx:end_idx]
pos_html = pos_html.rsplit('        </div>', 1)[0] # remove the extra closing div of the modal body

# Replace IDs and texts for Purchase Bill context
pos_html = pos_html.replace('posViewContent', 'pbPosViewContent')
pos_html = pos_html.replace('posOrdersPanel', 'pbPosOrdersPanel')
pos_html = pos_html.replace('togglePin()', 'togglePbPosPin()')
pos_html = pos_html.replace('pinIcon', 'pbPosPinIcon')
pos_html = pos_html.replace('togglePosOrders()', 'togglePbPosOrders()')
pos_html = pos_html.replace('posSearchSettings', 'pbPosSearchSettings')
pos_html = pos_html.replace('posLeftPanel', 'pbPosLeftPanel')
pos_html = pos_html.replace('posCartTotalAmount', 'pbPosCartTotalAmount')
pos_html = pos_html.replace('posCustomerSection', 'pbPosSupplierSection')
pos_html = pos_html.replace('posCustomerDefault', 'pbPosSupplierDefault')
pos_html = pos_html.replace('showPosNewCustomerForm()', 'showPbPosNewSupplierForm()')
pos_html = pos_html.replace('posCustomerSelect', 'pbPosSupplierSelect')
pos_html = pos_html.replace('Walk-in Customer', 'Walk-in Supplier')
pos_html = pos_html.replace('Sample Customer', 'Sample Supplier')
pos_html = pos_html.replace('posSalesRep', 'pbPosBuyerRep')
pos_html = pos_html.replace('Sales Representative', 'Buyer Representative')
pos_html = pos_html.replace('Sales.Rep', 'Buyer.Rep')
pos_html = pos_html.replace('posCartSettings', 'pbPosCartSettings')
pos_html = pos_html.replace('posCustomerNewForm', 'pbPosSupplierNewForm')
pos_html = pos_html.replace('hidePosNewCustomerForm()', 'hidePbPosNewSupplierForm()')
pos_html = pos_html.replace('posNewCustName', 'pbPosNewSuppName')
pos_html = pos_html.replace('posNewCustMobile', 'pbPosNewSuppMobile')
pos_html = pos_html.replace('togglePosNewCustomerDetails()', 'togglePbPosNewSupplierDetails()')
pos_html = pos_html.replace('posMoreDetailsChevron', 'pbPosMoreDetailsChevron')
pos_html = pos_html.replace('posNewCustomerExpandedFields', 'pbPosNewSupplierExpandedFields')
pos_html = pos_html.replace('savePosNewCustomer()', 'savePbPosNewSupplier()')
pos_html = pos_html.replace('posCartGrid', 'pbPosCartGrid')
pos_html = pos_html.replace('posCartTotals', 'pbPosCartTotals')
pos_html = pos_html.replace('#New Invoice', '#New Purchase')

with open(purchase_filepath, 'r', encoding='utf-8') as f:
    purchase_content = f.read()

# Insert the POS View HTML
insert_marker = '        </div>\n    </div>\n</div>\n<!-- End New Purchase Modal -->'
if insert_marker in purchase_content and 'id="pbPosViewContent"' not in purchase_content:
    purchase_content = purchase_content.replace(insert_marker, pos_html + '        </div>\n' + insert_marker)

# Update switchPbView function
js_old = """    function switchPbView(viewType) {
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
    }"""

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

if js_old in purchase_content:
    purchase_content = purchase_content.replace(js_old, js_new)

# Add the POS specific JS functions (toggle orders, new supplier form etc)
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

if 'function switchPbView' in purchase_content and 'togglePbPosOrders' not in purchase_content:
    purchase_content = purchase_content.replace(js_new, js_new + js_pos_functions)

# make sure menus array is updated to include the new POS menus
menus_old = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu'];"
menus_new = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu', 'pbPosSearchSettings', 'pbPosBuyerRep', 'pbPosCartSettings'];"
if menus_old in purchase_content:
    purchase_content = purchase_content.replace(menus_old, menus_new)

with open(purchase_filepath, 'w', encoding='utf-8') as f:
    f.write(purchase_content)
print("Added POS view successfully")
