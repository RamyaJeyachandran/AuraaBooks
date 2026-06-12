import re
import sys

def replace_tags_modal(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The pattern matches from <!-- Sub Modal: Manage Tags --> to the closing </script> right before <style>
    pattern = re.compile(r'<!-- Sub Modal: Manage Tags -->.*?</script>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub("{% include 'includes/manage_tags_modal.html' %}", content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced in {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

replace_tags_modal(r'd:\AuraaZenAIProject\abproject\templates\branch.html')
replace_tags_modal(r'd:\AuraaZenAIProject\abproject\templates\franchisee.html')
