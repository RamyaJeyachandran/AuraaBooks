import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change 'Item' text color to primary color (#1e78b9)
content = content.replace(
    '<span class="text-[12px] font-bold text-white">Item</span>',
    '<span class="text-[12px] font-bold text-[#1e78b9]">Item</span>'
)

# 2. Remove Buyer's Order No/Date from settings popover
buyer_order_html = """                            <label class="px-4 py-2 flex items-center gap-3 cursor-pointer hover:bg-slate-50">
                                <input type="checkbox" class="w-4 h-4 rounded border-slate-300 accent-[#1e78b9]" checked>
                                <span class="text-[13px] text-slate-700">Buyer Order No/Date</span>
                            </label>"""
content = content.replace(buyer_order_html, "")

# 3. Move Customer after Reference in single row
# In the original, the grids are:
# <div class="grid grid-cols-4 gap-6 relative">
#   ... (Invoice No, Invoice Date, Due Date, Reference #)
#   ... settings popover
# </div>
# <div class="grid grid-cols-4 gap-6 mt-4">
#   ... Deposit A/C, Reference, Customer
# </div>
# If the user wants "move the customer after the Reference in single row",
# They mean the Cash fields "Reference". Currently the second row is:
# Deposit A/C (col-span-1), Reference (col-span-1), Customer (col-span-2).
# This is ALREADY a single row. 
# BUT wait! What if they want "Customer" to NOT be col-span-2, but just normally after Reference, and the whole row is just those 3?
# OR what if they mean the TOP row Reference #?
# If we put them all in one grid grid-cols-5:
# Invoice No, Invoice Date, Due Date, Reference #, Customer.
# Let's move Customer to the top grid and make it grid-cols-5.
top_grid_start = '<div class="grid grid-cols-4 gap-6 relative">'
top_grid_new = '<div class="grid grid-cols-5 gap-6 relative">'
content = content.replace(top_grid_start, top_grid_new)

# Extract Customer field
customer_field_start = '<!-- Customer -->'
customer_field_end = '<!-- TABLE SECTION -->'
customer_field_match = re.search(r'(<!-- Customer -->.*?)</div>\s*</div>\s*<!-- TABLE SECTION -->', content, re.DOTALL)

if customer_field_match:
    customer_html = customer_field_match.group(1)
    
    # Remove customer from old location
    content = content.replace(customer_html, "")
    
    # Find the end of the top grid to insert Customer there
    # The top grid ends right before: <div class="grid grid-cols-4 gap-6 mt-4">
    top_grid_end_marker = '</div>\n                \n                <div class="grid grid-cols-4 gap-6 mt-4">'
    
    # Change customer to col-span-1 so it fits nicely
    new_customer_html = customer_html.replace('col-span-2', 'col-span-1')
    
    content = content.replace(top_grid_end_marker, f'{new_customer_html}\n                </div>\n                \n                <div class="grid grid-cols-4 gap-6 mt-4">')

# 4. Change download icon button color into primary color
download_btn_old = '<button class="text-[#1e78b9] hover:bg-blue-50 p-1 rounded">'
download_btn_new = '<button class="bg-[#1e78b9] text-white hover:bg-[#155e91] p-1 rounded">'
content = content.replace(download_btn_old, download_btn_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
