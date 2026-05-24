import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

js_funcs = """
<script>
    function openNewPurchaseModal() {
        document.getElementById('newPurchaseModal').classList.remove('hidden');
        document.getElementById('newPurchaseModal').classList.add('flex');
    }
    
    function closeNewPurchaseModal(event) {
        if(event) event.stopPropagation();
        document.getElementById('newPurchaseModal').classList.add('hidden');
        document.getElementById('newPurchaseModal').classList.remove('flex');
    }
    
    function toggleModalMenu(event, menuId) {
        event.stopPropagation();
        const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu'];
        menus.forEach(id => {
            if (id !== menuId) {
                const el = document.getElementById(id);
                if (el && !el.classList.contains('hidden')) {
                    el.classList.add('hidden');
                }
            }
        });
        const menu = document.getElementById(menuId);
        if (menu) {
            menu.classList.toggle('hidden');
        }
    }

    document.addEventListener('click', function(event) {
        const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu'];
        menus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.classList.contains('hidden') && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    });
</script>
"""

if "function openNewPurchaseModal" not in content:
    # insert it right before the last {% endblock %}
    parts = content.rsplit("{% endblock %}", 1)
    new_content = parts[0] + js_funcs + "\n{% endblock %}" + (parts[1] if len(parts) > 1 else "")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Injected missing JS functions.")
else:
    print("JS functions already present.")
