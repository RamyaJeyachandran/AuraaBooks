import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the tabs container HTML so it is visible by default
tabs_html_old = """                <!-- Quick View Tabs (Hidden by default) -->
                <div id="pbQuickTabsContainer" class="hidden items-center ml-8 gap-1">"""
tabs_html_new = """                <!-- Quick View Tabs -->
                <div id="pbQuickTabsContainer" class="flex items-center ml-8 gap-1">"""

if tabs_html_old in content:
    content = content.replace(tabs_html_old, tabs_html_new)
else:
    print("Warning: tabs html not found for replacement.")

# 2. Remove the Javascript logic that hides/shows the tabs container
js_old = """            if(modalTitle) modalTitle.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(tabsContainer) {
                tabsContainer.classList.remove('hidden');
                tabsContainer.classList.add('flex');
            }
            if(packingRow) packingRow.classList.remove('hidden');
            
        } else {
            creditBtn.classList.add('bg-[var(--accent)]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            cashBtn.classList.add('bg-white', 'text-[var(--accent)]');
            cashBtn.classList.remove('bg-[var(--accent)]', 'text-white');
            
            if(modalTitle) modalTitle.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(tabsContainer) {
                tabsContainer.classList.add('hidden');
                tabsContainer.classList.remove('flex');
            }
            if(packingRow) packingRow.classList.add('hidden');
        }"""

js_new = """            if(modalTitle) modalTitle.innerHTML = 'New Cash Invoice <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(packingRow) packingRow.classList.remove('hidden');
            
        } else {
            creditBtn.classList.add('bg-[var(--accent)]', 'text-white');
            creditBtn.classList.remove('bg-white', 'text-[var(--accent)]');
            
            cashBtn.classList.add('bg-white', 'text-[var(--accent)]');
            cashBtn.classList.remove('bg-[var(--accent)]', 'text-white');
            
            if(modalTitle) modalTitle.innerHTML = 'New Purchase <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>';
            if(packingRow) packingRow.classList.add('hidden');
        }"""

if js_old in content:
    content = content.replace(js_old, js_new)
else:
    print("Warning: javascript logic not found for replacement.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated tabs visibility successfully")
