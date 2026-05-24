import os
import re

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove parentheses from the amounts
content = content.replace("(₹1,48,772.00)", "₹1,48,772.00")

# 2. Change all green buttons to primary color. 
# bg-[#10b981] -> bg-[var(--accent)]
content = content.replace("bg-[#10b981]", "bg-[var(--accent)]")
# shadow-green-500/20 -> shadow-[var(--accent)]/20
content = content.replace("shadow-green-500/20", "shadow-[var(--accent)]/20")

# 3. Fix z-index issue on the table by removing overflow-hidden
content = content.replace("overflow-hidden mb-6", "mb-6")

# 4. Remove all table rows except the first one.
# The table body starts with <tbody class="divide-y divide-slate-100">
# The first row ends at </tr>
# Then we can cut everything until </tbody>
match = re.search(r'(<tbody[^>]*>.*?</tr>).*?</tbody>', content, re.DOTALL)
if match:
    first_row_and_open_tag = match.group(1)
    content = content[:match.start()] + first_row_and_open_tag + "\n                </tbody>" + content[match.end():]

# 5. Add the Recent Section between Stats and Add buttons
recent_html = """
        </div>
        <div class="flex items-center gap-3">
            <!-- Recent Navigator -->
            <div class="relative mr-4">
                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-[var(--accent)] z-10 border-2 border-white"></div>
                <div class="flex items-center bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden h-[52px]">
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-r border-slate-200">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <div class="px-5 flex flex-col items-center min-w-[80px]">
                        <span class="text-[9px] font-black text-slate-400 uppercase tracking-widest leading-none mb-1">Recent</span>
                        <span class="text-[14px] font-black text-slate-700 leading-none">PB-001</span>
                    </div>
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-l border-slate-200">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                </div>
            </div>"""

content = content.replace(
    '</div>\n        <div class="flex items-center gap-3">',
    recent_html
)


# 6. Add the Export Form menu from Image 2
export_menu_html = """
                </div>
                <!-- Export Form Menu -->
                <div id="pbExportFormMenu" class="hidden absolute top-full right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-slate-100 p-5 z-[500]">
                    <div class="absolute -top-1.5 right-10 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Method</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>List</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Type</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 pl-8 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
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
                            <button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>
                            <button class="px-6 py-2 bg-slate-200 text-slate-700 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Cancel</button>
                        </div>
                    </div>
                </div>
                <!-- Export Dropdown -->"""

content = content.replace(
    '</div>\n                <!-- Export Dropdown -->',
    export_menu_html
)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated purchase_bill.html with requested fixes")
