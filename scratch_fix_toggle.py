import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add back the class toggling for Cash button
target = "            if(cashFields) cashFields.classList.remove('hidden');"
replacement = """            if(cashBtn) cashBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-[var(--accent)] text-white transition-colors w-16 text-center';
            if(creditBtn) creditBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-white text-[var(--accent)] transition-colors w-16 text-center';
            if(cashFields) cashFields.classList.remove('hidden');"""

content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Toggle styling restored")
