js_code = '''
    function openQuickViewModal() {
        const modal = document.getElementById('quickViewModal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }
    }

    function closeQuickViewModal() {
        const modal = document.getElementById('quickViewModal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            selectViewMode('Normal View', true);
        }
    }

    function selectViewMode(mode, skipModal = false) {
        const icon = document.getElementById('viewModeIcon');
        if (icon) {
            if (mode === 'Normal View') {
                icon.innerHTML = <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>;
                if (!skipModal) {
                    const qvModal = document.getElementById('quickViewModal');
                    if (qvModal) {
                        qvModal.classList.add('hidden');
                        qvModal.classList.remove('flex');
                    }
                }
            } else if (mode === 'Quick View') {
                icon.innerHTML = <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>;
                if (!skipModal) {
                    openQuickViewModal();
                }
            }
        }
        const menu = document.getElementById('viewModeMenu');
        if(menu) menu.classList.add('hidden');
    }
'''

content = open('templates/sales_orders.html', encoding='utf-8').read()
import re

old_select_view_mode = '''    function selectViewMode(mode) {
        const icon = document.getElementById('viewModeIcon');
        if (icon) {
            if (mode === 'Normal View') {
                icon.innerHTML = <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>;
            } else if (mode === 'Quick View') {
                icon.innerHTML = <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>;
            }
        }
        document.getElementById('viewModeMenu').classList.add('hidden');
    }'''

new_content = content.replace(old_select_view_mode, js_code)
with open('templates/sales_orders.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
