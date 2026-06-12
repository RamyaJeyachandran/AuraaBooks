import re

with open('templates/branch.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements for main terms
content = content.replace('Branch Management', 'Franchisee Management')
content = content.replace('Total Branches', 'Total Franchisees')
content = content.replace('Branches', 'Franchisees')
content = content.replace('branches', 'franchisees')
content = content.replace('Branch', 'Franchisee')
content = content.replace('branch', 'franchisee')

# Some variables we want to keep exactly as is
content = content.replace('parent_franchisee_id', 'branch_id')
content = content.replace('assignUnderFranchisee', 'assignUnderBranch')
content = content.replace('franchisees_data', 'franchisee_data')
content = content.replace('franchisee_data', 'franchisee_data')
content = content.replace('parent_franchisee', 'parent_branch')
content = content.replace('franchiseeList', 'franchiseeList')

with open('templates/franchisee.html', 'w', encoding='utf-8') as f:
    f.write(content)
