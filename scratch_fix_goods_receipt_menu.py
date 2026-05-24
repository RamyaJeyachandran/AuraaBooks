import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Rename duplicated IDs that might prevent toggleActionMenu from working correctly
content = content.replace("toggleActionMenu(event, 'exportMenu')", "toggleActionMenu(event, 'grExportMenu')")
content = content.replace('id="exportMenu"', 'id="grExportMenu"')

content = content.replace("toggleActionMenu(event, 'filterMenu')", "toggleActionMenu(event, 'grFilterMenu')")
content = content.replace('id="filterMenu"', 'id="grFilterMenu"')

content = content.replace("toggleActionMenu(event, 'settingsMenu')", "toggleActionMenu(event, 'grSettingsMenu')")
content = content.replace('id="settingsMenu"', 'id="grSettingsMenu"')

content = content.replace("toggleActionMenu(event, 'titleDropdownMenu')", "toggleActionMenu(event, 'grTitleDropdownMenu')")
content = content.replace('id="titleDropdownMenu"', 'id="grTitleDropdownMenu"')

# 2. Change 'Purchase / Goods Receipt' into 'Goods Receipt'
# Remove the 'Purchase /' span
old_title_block = """            <div class="flex items-center gap-2">
                <span class="text-[32px] font-medium text-slate-500 tracking-tight">Purchase <span class="mx-1">/</span></span>
                <div class="relative group/title">
                    <button onclick="toggleActionMenu(event, 'grTitleDropdownMenu')" class="flex items-center gap-1 text-[32px] font-black text-blue-600 hover:text-blue-700 tracking-tight">
                        Goods Receipt
                        <svg class="w-6 h-6 mt-1" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>"""

new_title_block = """            <div class="flex items-center gap-2">
                <div class="relative group/title">
                    <button onclick="toggleActionMenu(event, 'grTitleDropdownMenu')" class="flex items-center gap-1 text-[32px] font-black text-blue-600 hover:text-blue-700 tracking-tight">
                        Goods Receipt
                        <svg class="w-6 h-6 mt-1" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>"""

content = content.replace(old_title_block, new_title_block)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated goods_receipt.html")
