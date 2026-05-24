import re
html = open('templates/sales_orders.html', encoding='utf-8').read()
modals = re.findall(r'<div[^>]*id=[\"\']([^\"\']*Modal[^\"\']*)[\"\'][^>]*>', html, re.IGNORECASE)
print('Modals found:', modals)
