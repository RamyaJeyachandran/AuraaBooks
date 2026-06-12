import os

file_path = r"D:\AuraaZenAIProject\abproject\templates\units_settings.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<form id="unitForm"'
end_marker = '{% endblock %}'

start_idx = content.find(start_marker)
end_idx = content.rfind(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx]
    
    with open(r"D:\AuraaZenAIProject\abproject\scratch\units.js", "r", encoding="utf-8") as f:
        replacement = f.read()
        
    new_content += replacement
    new_content += content[end_idx + len(end_marker):]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Template updated.")
else:
    print("Markers not found.")
