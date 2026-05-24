import re
from collections import Counter
html = open('templates/sales_quotes.html', encoding='utf-8').read()
ids = re.findall(r'id=\"([^\"]+)\"', html)
counts = Counter(ids)
duplicates = {k: v for k, v in counts.items() if v > 1}
if duplicates:
    print('Duplicate IDs:', duplicates)
else:
    print('No duplicate IDs')
