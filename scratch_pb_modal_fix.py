import os
import re

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# The modal was accidentally appended after {% endblock %}
# Let's extract the modal + script from the end
split_str = "{% endblock %}\n\n<!-- New Purchase Modal -->"
if split_str in content:
    parts = content.split(split_str)
    # parts[0] is everything up to the first script + endblock
    # parts[1] is the modal HTML and new script
    
    # We want to put parts[1] BEFORE {% endblock %}
    new_content = parts[0] + "\n\n<!-- New Purchase Modal -->" + parts[1] + "\n{% endblock %}\n"
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed modal placement in template.")
else:
    print("Could not find the split string.")
