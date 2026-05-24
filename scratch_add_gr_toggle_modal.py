import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

toggle_modal_func = """
    function toggleModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.toggle('hidden');
            if(!modal.classList.contains('hidden')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = 'auto';
            }
        }
    }
"""

if "function toggleModal" not in content:
    content = content.replace("function toggleActionMenu", toggle_modal_func + "\n    function toggleActionMenu")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added toggleModal to goods_receipt.html")
else:
    print("toggleModal already exists")
