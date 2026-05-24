import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Increase width of Bill outstanding and overdue
# Currently: min-w-[400px]
# Let's change it to min-w-[600px] (or maybe w-[600px])
if 'min-w-[400px]' in content:
    content = content.replace('min-w-[400px]', 'min-w-[600px]')
    print("Updated width")

# 2. Move Recent Navigator near the download icon button
recent_navigator_start = '            <!-- Recent Navigator -->'
recent_navigator_end = '            </div>\n        </div>\n\n        <!-- Right Side: Filters -->'

if recent_navigator_start in content:
    # Find the Recent Navigator block
    start_idx = content.find(recent_navigator_start)
    end_idx = content.find('</div>', content.find('</div>', content.find('</div>', start_idx) + 1) + 1)
    
    # Wait, the exact block is:
    block = """            <!-- Recent Navigator -->
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
            </div>"""

    if block in content:
        # Remove it from the current place
        content = content.replace(block, "")
        
        # In order to place it near the download icon (Export Split Button)
        # It's at:
        #         <!-- Right Side: Filters -->
        #         <div class="flex items-center gap-4">
        # <!-- Export Split Button -->
        
        # Since the heights are different (74px vs 40px), maybe I should reduce the height of Recent Navigator to 40px to match the export button, and adjust the layout so it looks good.
        # But wait, the pills have py-4 (approx 74px height). If I put recent navigator near export button, maybe it should be 40px (h-10).
        # Let's adjust its style to match the h-10 of the buttons on the right.
        modified_block = block.replace('h-[74px]', 'h-10').replace('rounded-2xl', 'rounded-xl')
        # Remove the top absolute dot if it overlaps too much or adjust it
        modified_block = modified_block.replace('-top-1 -right-1', '-top-1 -right-1')
        # Also remove the flex-col for Recent and PB-001 to put them in a row, or keep it compact
        modified_block = modified_block.replace('flex-col items-center justify-center', 'items-center gap-2')
        modified_block = modified_block.replace('mb-2', '')
        
        # Let's just insert it before the Export button.
        insert_target = """        <!-- Right Side: Filters -->
        <div class="flex items-center gap-4">
<!-- Export Split Button -->"""
        
        if insert_target in content:
            new_insert = """        <!-- Right Side: Filters -->
        <div class="flex items-center gap-4">
""" + modified_block + """
<!-- Export Split Button -->"""
            content = content.replace(insert_target, new_insert)
            print("Moved recent navigator")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
