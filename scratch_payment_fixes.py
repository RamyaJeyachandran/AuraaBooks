import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_payment.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Dashboard text
old_dashboard = """        <div class="flex flex-col">
            <h1 class="text-[32px] font-black text-slate-800 tracking-tight">Payment</h1>
            <span class="text-[12px] font-bold text-slate-500 uppercase tracking-widest mt-1">Dashboard</span>
        </div>"""
new_dashboard = """        <h1 class="text-[32px] font-black text-slate-800 tracking-tight">Payment</h1>"""
content = content.replace(old_dashboard, new_dashboard)

# 2. Swap Recent section and Fiscal Year
old_header_right = """        <div class="flex items-center gap-6">
            <!-- Recent Navigator -->
            <div class="relative">
                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-[var(--accent)] z-10 border-2 border-white"></div>
                <div class="flex items-center bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden h-10">
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-r border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <div class="px-6 flex items-center gap-2 min-w-[100px]">
                        <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none ">Recent</span>
                        <span class="text-[16px] font-black text-slate-700 leading-none">PMT-001</span>
                    </div>
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-l border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                </div>
            </div>

            <div class="flex flex-col items-end">
                <span class="text-[20px] font-black text-[#2f88d4] leading-none">₹3,66,200.00</span>
                <span class="text-[11px] font-bold text-slate-400 mt-1">This Fiscal Year</span>
            </div>"""

new_header_right = """        <div class="flex items-center gap-6">
            <div class="flex flex-col items-end">
                <span class="text-[20px] font-black text-[#2f88d4] leading-none">₹3,66,200.00</span>
                <span class="text-[11px] font-bold text-slate-400 mt-1">This Fiscal Year</span>
            </div>

            <!-- Recent Navigator -->
            <div class="relative">
                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-[var(--accent)] z-10 border-2 border-white"></div>
                <div class="flex items-center bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden h-10">
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-r border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <div class="px-6 flex items-center gap-2 min-w-[100px]">
                        <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none ">Recent</span>
                        <span class="text-[16px] font-black text-slate-700 leading-none">PMT-001</span>
                    </div>
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-l border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                </div>
            </div>"""
content = content.replace(old_header_right, new_header_right)

# 3. Change {% block extra_scripts %} to {% block extra_js %}
content = content.replace("{% block extra_scripts %}", "{% block extra_js %}")

# 4. Change the 3 horizontal dots background color to dark gray
old_dots = """            <!-- Settings Button -->
            <div class="relative group/settings z-[480]">
                <button onclick="toggleActionMenu(event, 'pbSettingsMenu')" class="w-10 h-10 flex items-center justify-center text-slate-500 hover:text-slate-800 transition-all">"""
new_dots = """            <!-- Settings Button -->
            <div class="relative group/settings z-[480]">
                <button onclick="toggleActionMenu(event, 'pbSettingsMenu')" class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm">"""
content = content.replace(old_dots, new_dots)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to purchase_payment.html")
