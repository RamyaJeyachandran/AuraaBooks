html = open('templates/sales_orders.html', encoding='utf-8').read()
import re
match = re.search(r'<div id=\"modalOverlay\".*?<!-- Modal Header', html, re.DOTALL)
if match:
    print(match.group(0))
