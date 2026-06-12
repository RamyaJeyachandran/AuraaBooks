def fix_html_exact(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the HTML block
    start_html = '<!-- Sub Modal: Manage Tags -->'
    end_html_marker = '</div>\n</div>\n{% endblock %}'
    
    idx_start = content.find(start_html)
    if idx_start != -1:
        idx_end = content.find(end_html_marker, idx_start)
        if idx_end != -1:
            idx_end += len('</div>\n</div>')
            content = content[:idx_start] + "{% include 'includes/manage_tags_modal.html' %}\n" + content[idx_end:]
            print(f"Replaced HTML in {filepath}")
        else:
            print(f"Could not find HTML end in {filepath}")
    else:
        print(f"Could not find HTML start in {filepath}")

    # Find the JS block
    start_js = '// Manage Tags Javascript'
    end_js = "document.addEventListener('DOMContentLoaded', () => {\n    fetchTags();\n});"
    
    idx_js_start = content.find(start_js)
    if idx_js_start != -1:
        idx_js_end = content.find(end_js, idx_js_start)
        if idx_js_end != -1:
            idx_js_end += len(end_js)
            content = content[:idx_js_start] + content[idx_js_end:]
            print(f"Replaced JS in {filepath}")
        else:
            print(f"Could not find JS end in {filepath}")
    else:
        print(f"Could not find JS start in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_html_exact(r'd:\AuraaZenAIProject\abproject\templates\branch.html')
fix_html_exact(r'd:\AuraaZenAIProject\abproject\templates\franchisee.html')
