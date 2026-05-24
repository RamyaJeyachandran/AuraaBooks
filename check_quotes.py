import re
html = open('templates/sales_quotes.html', encoding='utf-8').read()
tags = re.findall(r'<[^>]+>', html)
for tag in tags:
    if tag.count('\"') % 2 != 0:
        print('Odd double quotes:', tag)
