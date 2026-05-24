import re

filepath = 'd:/AuraaZenAIProject/abproject/templates/purchase_orders.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to remove the view mode dropdown from the Normal View modal
pattern1 = r'<!-- Normal / Quick View Dropdown next to title.*?</button>\s*</div>\s*</div>'
content = re.sub(pattern1, '', content, flags=re.DOTALL)

# Pattern to remove the view mode dropdown from the Quick View modal
pattern2 = r'<!-- Quick View Dropdown -->.*?</div>\s*</div>\s*</div>'
content = re.sub(pattern2, '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed dropdowns from purchase_orders.html")
