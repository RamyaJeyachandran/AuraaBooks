import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change outer modal background
old_modal_outer = '<div class="bg-slate-50 w-full h-full max-w-[1920px] rounded-2xl shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95 duration-200">'
new_modal_outer = '<div class="bg-white w-full h-full max-w-[1920px] rounded-2xl shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95 duration-200">'
content = content.replace(old_modal_outer, new_modal_outer)

# 2. Change modal body to bg-white and remove the inner container wrapper
# We need to find the specific block and replace it.

old_body_start = """        <!-- Modal Body (Normal View equivalent) -->
        <div class="flex-1 overflow-auto bg-slate-50 p-6 flex flex-col custom-scrollbar">
            <div class="w-full max-w-[1400px] mx-auto bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col">
                
                <!-- Top Form Fields -->
                <div class="p-6 border-b border-slate-200 space-y-5">"""

new_body_start = """        <!-- Modal Body (Normal View equivalent) -->
        <div class="flex-1 overflow-auto bg-white p-6 flex flex-col custom-scrollbar space-y-6">
            
                <!-- Top Form Fields -->
                <div class="space-y-5 w-full">"""

content = content.replace(old_body_start, new_body_start)

# 3. Table Section wrapper
# Old: 
#                 </div>
#
#                 <!-- Table Section -->
#                 <div class="flex flex-col p-6">
old_table_section = """                </div>

                <!-- Table Section -->
                <div class="flex flex-col p-6">"""

new_table_section = """                </div>

                <!-- Table Section -->
                <div class="flex flex-col w-full">"""
content = content.replace(old_table_section, new_table_section)

# 4. Remove the closing tags for the inner container.
# They are right before:
# </div>
# <!-- End New Cash Purchase Modal -->
# Let's see how it looks at the end.
"""
                    </div>

                </div>
            </div>
        </div>
    </div>
</div>
<!-- End New Cash Purchase Modal -->
"""
# The structure at the end:
# Bottom Fields Section ends with </div>
# Then Table Section ends with </div>
# Then inner container ends with </div>
# Then Modal Body ends with </div>
# Then Modal wrapper ends with </div>
# Then modal background overlay ends with </div>
old_end = """                    </div>

                </div>
            </div>
        </div>
    </div>
</div>
<!-- End New Cash Purchase Modal -->"""

new_end = """                    </div>

                </div>
        </div>
    </div>
</div>
<!-- End New Cash Purchase Modal -->"""
content = content.replace(old_end, new_end)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal container simplified")
