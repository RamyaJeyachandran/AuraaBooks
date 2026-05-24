import re
with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx_start = content.find('<div id="quickViewModal"')
idx_end = content.find('<script>', idx_start)
if idx_start != -1 and idx_end != -1:
    qv_html = content[idx_start:idx_end]
    
    pos_html = qv_html.replace('quickViewModal', 'posViewModal')
    pos_html = pos_html.replace('qvViewModeMenu', 'posViewModeMenu')
    pos_html = pos_html.replace('qvSaveMenu', 'posSaveMenu')
    pos_html = pos_html.replace('qvSettingsMenu', 'posSettingsMenu')
    pos_html = pos_html.replace('qvCustomerTypeMenu', 'posCustomerTypeMenu')
    pos_html = pos_html.replace('closeQuickViewModal', 'closePosViewModal')
    pos_html = pos_html.replace('Quick View', 'POS View')
    
    # Insert posViewModal before <script>
    content = content[:idx_end] + pos_html + content[idx_end:]
    
    script_addition = '''
    function openPosViewModal() {
        const modal = document.getElementById('posViewModal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }
        closeModal();
        closeQuickViewModal();
    }

    function closePosViewModal() {
        const modal = document.getElementById('posViewModal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
        }
    }
'''
    content = content.replace('function closeQuickViewModal() {', script_addition + '\n    function closeQuickViewModal() {')
    
    # update selectViewMode to call openPosViewModal
    content = content.replace('// Logic for POS view if any', 'openPosViewModal();')
    
    # Update menu close logic
    content = content.replace("'qvTopDropdown', 'qvSaveMenu', 'qvSettingsMenu', 'qvCustomerTypeMenu'", "'qvTopDropdown', 'qvSaveMenu', 'qvSettingsMenu', 'qvCustomerTypeMenu', 'posTopDropdown', 'posSaveMenu', 'posSettingsMenu', 'posCustomerTypeMenu'")
    content = content.replace("const qvMenu = document.getElementById('qvViewModeMenu');\n        if (qvMenu) qvMenu.classList.add('hidden');", "const qvMenu = document.getElementById('qvViewModeMenu');\n        if (qvMenu) qvMenu.classList.add('hidden');\n        const posMenu = document.getElementById('posViewModeMenu');\n        if (posMenu) posMenu.classList.add('hidden');")

    with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'w', encoding='utf-8') as f2:
        f2.write(content)
    print('POS modal added')
else:
    print('quickViewModal not found')
