import os

path = 'D:/AuraaZenAIProject/abproject/templates/franchisee.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("toggleFranchiseeDropdown", "toggleBranchDropdown")
content = content.replace("common-franchiseeCheck", "common-branchCheck")
content = content.replace("common-franchiseeDrop", "common-branchDrop")
content = content.replace("modalParentFranchisee", "modalParentBranch")

# remove populateParentFranchisees completely
import re
content = re.sub(r'function populateParentFranchisees\(.*?\)\s*\{.*?\n    \}', '', content, flags=re.DOTALL)
content = content.replace("populateParentFranchisees(index);", "")
content = content.replace("populateParentFranchisees(-1);", "")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
