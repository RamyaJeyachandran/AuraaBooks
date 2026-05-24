import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the Export button to have the left-click form popup
# Currently the left button is just a button without onclick.
# We'll add onclick="toggleActionMenu(event, 'grExportFormMenu')" to the left button
old_export_button = """<button class="px-4 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all border-r border-white/20 flex items-center justify-center">"""
new_export_button = """<button onclick="toggleActionMenu(event, 'grExportFormMenu')" class="px-4 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all border-r border-white/20 flex items-center justify-center">"""
content = content.replace(old_export_button, new_export_button)

# 2. Add the grExportFormMenu right before the grExportMenu
old_export_menu = """<div id="grExportMenu" class="hidden absolute top-full right-0 mt-2 w-48 bg-white rounded-2xl shadow-2xl border border-slate-100 py-2 z-[500]">"""

export_form_menu = """<!-- Export Form Dropdown (Left Click) -->
                <div id="grExportFormMenu" class="hidden absolute top-full right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-slate-100 p-5 z-[500]">
                    <div class="absolute -top-1.5 right-10 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Method</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-slate-400 appearance-none">
                                    <option>List</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Type</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 pl-8 text-[13px] font-medium text-slate-700 outline-none focus:border-slate-400 appearance-none">
                                    <option>PDF</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute left-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 pt-1">
                            <div class="relative w-1/2">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] font-medium text-slate-700 outline-none appearance-none">
                                    <option>This Fiscal Year</option>
                                </select>
                                <svg class="w-3.5 h-3.5 text-slate-500 absolute right-2 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                            <div class="flex items-center gap-1">
                                <span class="text-[12px] font-medium text-slate-600">Apr 1, 2026 - Mar 31, 2027</span>
                                <div class="flex flex-col">
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 14l5-5 5 5z"/></svg>
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-center gap-2 pt-4">
                            <button class="px-6 py-2 bg-[#10b981] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>
                            <button class="px-6 py-2 bg-slate-200 text-slate-600 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Cancel</button>
                        </div>
                    </div>
                </div>
                """

content = content.replace(old_export_menu, export_form_menu + old_export_menu)

# 3. Update the Apply button in Settings Menu to light gray
old_apply_btn = """<button class="w-full mt-2 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply</button>"""
new_apply_btn = """<button class="w-24 mt-2 py-2 bg-slate-200 text-slate-600 rounded font-bold text-[14px] hover:bg-slate-300 transition-all">Apply</button>"""
content = content.replace(old_apply_btn, new_apply_btn)

# Make sure the settings menu matches the styling in the image (rounded-lg not 2xl, no blue hover for checkboxes, square checkboxes)
old_settings_menu_start = """<div id="grSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded-2xl shadow-2xl border border-slate-100 p-4 z-[500]">"""
new_settings_menu_start = """<div id="grSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded shadow-xl border border-slate-200 p-4 z-[500]">"""
content = content.replace(old_settings_menu_start, new_settings_menu_start)

# Replacing checkboxes to match standard square checkboxes
import re
checkbox_pattern = re.compile(r'<label class="flex items-center gap-3 cursor-pointer group/item">.*?</label>', re.DOTALL)

settings_content = """<div class="space-y-3">
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Ref.No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Due Days</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" checked class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Status</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" checked class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Due Amount</span>
                        </label>
                        
                        <div class="h-px bg-slate-200 my-2"></div>
                        
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Delivery Chalan No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Delivery Chalan Date</span>
                        </label>
                        
                        <div class="pt-2">
                            <button class="px-6 py-2 bg-slate-200 text-slate-700 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Apply</button>
                        </div>
                    </div>"""

# Find the div with space-y-3 and replace it
space_y_3_pattern = re.compile(r'<div class="space-y-3">.*?</div>\s*</div>\s*</div>', re.DOTALL)
match = space_y_3_pattern.search(content)
if match:
    content = content[:match.start()] + settings_content + "\n                </div>\n            </div>" + content[match.end():]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("goods_receipt.html dropdown menus updated.")
