import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Remove overflow-hidden from the items table containers to prevent the dropdowns from being clipped
content = content.replace("relative z-[300] overflow-hidden", "relative z-[300]")

# The user also noted "border" on the dropdown might need adjusting. 
# They want UI identical to purchase_quotes. Let's check the dropdown border in purchase_quotes.html
# Actually I'll just change border-2 border-[var(--accent)] to border border-[var(--accent)] to make it match the 1px border in the image
content = content.replace("border-2 border-[var(--accent)]", "border border-[var(--accent)]")
content = content.replace("border-t-2 border-l-2", "border-t border-l")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated table container overflow and dropdown borders.")
