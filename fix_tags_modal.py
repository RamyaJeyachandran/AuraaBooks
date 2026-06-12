import re

def remove_between(text, start_marker, end_marker):
    pattern = re.compile(re.escape(start_marker) + r'.*?' + re.escape(end_marker), re.DOTALL)
    if pattern.search(text):
        print(f"Found {start_marker} to {end_marker}")
        return pattern.sub('', text)
    return text

def fix_html(filepath, is_franchisee=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the Manage Tags HTML block with the include
    start_html = '<!-- Sub Modal: Manage Tags -->'
    end_html = '</div>\n</div>\n</div>'
    
    # We find where it starts
    idx_start = content.find(start_html)
    if idx_start != -1:
        # find the end of the div by counting
        # or just regex:
        pattern = re.compile(r'<!-- Sub Modal: Manage Tags -->.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
        content = pattern.sub("{% include 'includes/manage_tags_modal.html' %}", content)
        print("Replaced Manage Tags HTML block")

    # 2. Remove the Manage Tags Javascript
    if is_franchisee:
        start_js = '// Manage Tags Javascript'
        end_js = "document.addEventListener('DOMContentLoaded', () => {\n    fetchTags();\n});"
    else:
        start_js = '// Manage Tags Javascript'
        end_js = "document.addEventListener('DOMContentLoaded', () => {\n    fetchTags();\n});"
        
    pattern_js = re.compile(r'// Manage Tags Javascript.*?' + re.escape("document.addEventListener('DOMContentLoaded', () => {\n    fetchTags();\n});"), re.DOTALL)
    if pattern_js.search(content):
        content = pattern_js.sub('', content)
        print("Replaced Manage Tags JS block")
    else:
        # Try alternate formatting
        pattern_js2 = re.compile(r'let globalTags = \[\];.*?document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*fetchTags\(\);\s*\}\);', re.DOTALL)
        if pattern_js2.search(content):
            content = pattern_js2.sub('', content)
            print("Replaced Manage Tags JS block (alt)")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_html(r'd:\AuraaZenAIProject\abproject\templates\branch.html', False)
fix_html(r'd:\AuraaZenAIProject\abproject\templates\franchisee.html', True)
