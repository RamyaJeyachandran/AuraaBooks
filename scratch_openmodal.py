import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Modify openModal
open_modal_old = """    function openModal(title) {
        const overlay = document.getElementById('modalOverlay');
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
        }
        if (title === 'Cash Invoice') {
            setInvoiceType('Cash');
        } else {
            setInvoiceType('Credit');
        }
    }"""

open_modal_new = """    function openModal(title) {
        const overlay = document.getElementById('modalOverlay');
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
        }
        
        // Reset tabs to only 1
        const tabsContainer = document.getElementById('quickTabsContainer');
        if (tabsContainer) {
            const tabs = tabsContainer.querySelectorAll('.tab-btn');
            for (let i = 1; i < tabs.length; i++) {
                tabs[i].remove();
            }
            if (tabs.length > 0) {
                switchToQuickTab(tabs[0], 1);
            }
            tabCount = 1; // Reset global counter
        }
        
        // Switch to Normal View by default
        if (typeof switchView === 'function') {
            switchView('Normal View');
        }
        
        if (title === 'Cash Invoice') {
            setInvoiceType('Cash');
        } else {
            setInvoiceType('Credit');
        }
    }"""

if "function openModal(" in content:
    content = content.replace(open_modal_old, open_modal_new)
else:
    print("openModal not found!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("openModal updated")
