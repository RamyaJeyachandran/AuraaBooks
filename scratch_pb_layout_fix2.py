import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Table Z-Index issue by removing overflow-x-auto custom-scrollbar
content = content.replace('<div class="overflow-x-auto custom-scrollbar">', '<div>')

# 2. Rearrange the Layout
# We need to extract the Compact Count Pills and Recent Navigator,
# then remove them from Row 1, and insert them into Row 2 (the Actions Section).

# Extract Row 1 flex-1 div content
# It looks like:
# <div class="flex items-center gap-4 flex-1 mr-6">
#     <h1 class="text-[32px] font-black text-slate-800 tracking-tight">Purchase Bill</h1>
#     [Stats Pill]
#     [Recent Navigator]
# </div>

# The Actions section looks like:
# <div class="flex items-center justify-end mb-6 relative z-[200]">
#     <div class="flex items-center gap-4">
#         <!-- Export Split Button -->

# We will rewrite the Header Section and Actions Section.

header_start = content.find('<!-- Header Section -->')
table_start = content.find('<!-- Table Section (Similar to Purchase Quote) -->')

if header_start != -1 and table_start != -1:
    # We will manually replace the top part
    new_top_section = """<!-- Header Section -->
    <div class="flex items-center justify-between mb-6 relative z-[300]">
        <h1 class="text-[32px] font-black text-slate-800 tracking-tight">Purchase Bill</h1>
        <div class="flex items-center gap-3">
            <button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Purchase
            </button>
            <button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Cash Purchase
            </button>
        </div>
    </div>

    <!-- Actions & Stats Section -->
    <div class="flex items-center justify-between mb-6 relative z-[200]">
        <!-- Left Side: Stats & Recent -->
        <div class="flex items-center gap-4">
            <!-- Compact Count Pills -->
            <div class="flex items-center justify-around bg-white border border-slate-200 rounded-2xl px-8 py-4 shadow-sm min-w-[400px]">
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Bill Outstanding</span>
                    <span class="text-[30px] font-black text-slate-700 leading-none">₹1,48,772.00</span>
                </div>
                <div class="w-px h-12 bg-slate-200 mx-6"></div>
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Bill Overdue</span>
                    <span class="text-[30px] font-black text-amber-500 leading-none">₹1,48,772.00</span>
                </div>
            </div>

            <!-- Recent Navigator -->
            <div class="relative">
                <div class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-[var(--accent)] z-10 border-2 border-white"></div>
                <div class="flex items-center bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden h-[74px]">
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-r border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <div class="px-6 flex flex-col items-center justify-center min-w-[100px]">
                        <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Recent</span>
                        <span class="text-[16px] font-black text-slate-700 leading-none">PB-001</span>
                    </div>
                    <button type="button" class="px-3 h-full hover:bg-slate-50 text-slate-400 hover:text-slate-700 transition-all border-l border-slate-200">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Right Side: Filters -->
        <div class="flex items-center gap-4">
"""
    
    # We need to get the original right-side filter buttons
    # They are between `<div class="flex items-center gap-4">` inside the Actions section and `<!-- Table Section`
    # Let's search for `<!-- Export Split Button -->`
    export_start = content.find('<!-- Export Split Button -->')
    actions_end = content.find('</div>\n    </div>\n\n    <!-- Table Section')
    
    if export_start != -1 and actions_end != -1:
        filters_html = content[export_start:actions_end]
        
        # Construct the new full top half
        new_top_half = new_top_section + filters_html + "\n        </div>\n    </div>\n\n    "
        
        content = content[:header_start] + new_top_half + content[table_start:]

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated layout and fixed z-index!")
    else:
        print("Could not find export start or actions end")
else:
    print("Could not find header or table section")
