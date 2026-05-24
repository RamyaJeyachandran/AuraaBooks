import os

files = [
    r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html",
    r"d:\AuraaZenAIProject\abproject\templates\purchase_payment.html"
]

js_funcs = """
<script>
    function openNewPurchaseModal() {
        const modal = document.getElementById('newPurchaseModal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            document.body.style.overflow = 'hidden';
        }
    }
    
    function closeNewPurchaseModal(event) {
        if(event) event.stopPropagation();
        const modal = document.getElementById('newPurchaseModal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            document.body.style.overflow = '';
        }
    }

    function openNewCashPurchaseModal() {
        const modal = document.getElementById('newCashPurchaseModal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            document.body.style.overflow = 'hidden';
        }
    }
    
    function closeNewCashPurchaseModal(event) {
        if(event) event.stopPropagation();
        const modal = document.getElementById('newCashPurchaseModal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            document.body.style.overflow = '';
        }
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

for html_file in files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure we don't add it twice
    if "function openNewPurchaseModal" not in content:
        parts = content.rsplit("{% endblock %}", 1)
        if len(parts) > 1:
            new_content = parts[0] + js_funcs + "\n{% endblock %}" + parts[1]
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Injected missing JS functions into {html_file}.")
        else:
            print(f"Could not find endblock in {html_file}.")
    else:
        print(f"JS functions already present in {html_file}.")
