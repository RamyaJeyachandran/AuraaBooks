import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the hiding of the Cash/Credit toggle button
content = content.replace("            if(cashBtn) cashBtn.parentElement.classList.add('hidden'); // Hide toggle in Cash Invoice mode\n", "")
content = content.replace("            if(cashBtn) cashBtn.parentElement.classList.remove('hidden');\n", "")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Toggle un-hidden")
