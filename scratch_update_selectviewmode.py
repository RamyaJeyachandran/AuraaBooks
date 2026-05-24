import os
with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the `selectViewMode` function
start = content.find('function selectViewMode')
end = content.find('function filterByStatus', start)

new_selectViewMode = """function selectViewMode(mode, skipModal = false) {
        const icon = document.getElementById('viewModeIcon');
        if (icon) {
            if (mode === 'Normal View') {
                icon.innerHTML = `<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>`;
                if (!skipModal) {
                    const qvModal = document.getElementById('quickViewModal');
                    const posModal = document.getElementById('posViewModal');
                    if (qvModal) { qvModal.classList.add('hidden'); qvModal.classList.remove('flex'); }
                    if (posModal) { posModal.classList.add('hidden'); posModal.classList.remove('flex'); }
                    
                    const normalModal = document.getElementById('modalOverlay');
                    if (normalModal) {
                        normalModal.classList.remove('hidden');
                        normalModal.classList.add('flex');
                    }
                }
            } else if (mode === 'Quick View') {
                icon.innerHTML = `<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>`;
                if (!skipModal) {
                    const normalModal = document.getElementById('modalOverlay');
                    const posModal = document.getElementById('posViewModal');
                    if (normalModal) { normalModal.classList.add('hidden'); normalModal.classList.remove('flex'); }
                    if (posModal) { posModal.classList.add('hidden'); posModal.classList.remove('flex'); }
                    
                    const qvModal = document.getElementById('quickViewModal');
                    if (qvModal) {
                        qvModal.classList.remove('hidden');
                        qvModal.classList.add('flex');
                    }
                }
            } else if (mode === 'POS View') {
                icon.innerHTML = `<rect x="2" y="3" width="20" height="18" rx="2" ry="2"/><line x1="2" y1="8" x2="22" y2="8"/><line x1="8" y1="18" x2="8" y2="8"/>`;
                if (!skipModal) {
                    const normalModal = document.getElementById('modalOverlay');
                    const qvModal = document.getElementById('quickViewModal');
                    if (normalModal) { normalModal.classList.add('hidden'); normalModal.classList.remove('flex'); }
                    if (qvModal) { qvModal.classList.add('hidden'); qvModal.classList.remove('flex'); }
                    
                    const posModal = document.getElementById('posViewModal');
                    if (posModal) {
                        posModal.classList.remove('hidden');
                        posModal.classList.add('flex');
                    }
                }
            }
        }
        
        // Hide all view mode menus
        ['viewModeMenu', 'qvViewModeMenu', 'posViewModeMenu'].forEach(id => {
            const menu = document.getElementById(id);
            if (menu) menu.classList.add('hidden');
        });
    }

    function closePosViewModal() {
        const posModal = document.getElementById('posViewModal');
        if (posModal) {
            posModal.classList.add('hidden');
            posModal.classList.remove('flex');
        }
    }

    """

content = content[:start] + new_selectViewMode + content[end:]

with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'w', encoding='utf-8') as f2:
    f2.write(content)

print('Updated selectViewMode to support POS View!')
