import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

script_block = """
<script>
    function toggleActionMenu(event, menuId) {
        event.stopPropagation();
        
        // Close all other menus
        const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu'];
        menus.forEach(id => {
            if (id !== menuId) {
                const el = document.getElementById(id);
                if (el && !el.classList.contains('hidden')) {
                    el.classList.add('hidden');
                }
            }
        });

        // Toggle the clicked menu
        const menu = document.getElementById(menuId);
        if (menu) {
            menu.classList.toggle('hidden');
        }
    }

    // Close menus when clicking outside
    document.addEventListener('click', function(event) {
        const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu'];
        menus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.classList.contains('hidden') && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    });
</script>
{% endblock %}
"""

if "<script>" not in content:
    content = content.replace("{% endblock %}", script_block)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Script block added to goods_receipt.html")
else:
    print("Script block already exists")
