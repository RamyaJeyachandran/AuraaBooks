import re

html = open('templates/warehouse.html', 'r', encoding='utf-8').read()

# Replace save buttons
html = html.replace('<button class="px-8 h-12 bg-white text-[var(--accent)] rounded-l-[14px] text-[13px] font-black uppercase tracking-widest border-r border-[var(--accent)]/30 hover:bg-slate-50 transition-all">SAVE</button>', '<button onclick="saveWarehouse(false)" class="px-8 h-12 bg-white text-[var(--accent)] rounded-l-[14px] text-[13px] font-black uppercase tracking-widest border-r border-[var(--accent)]/30 hover:bg-slate-50 transition-all">SAVE</button>')
html = html.replace('<button class="w-full text-left px-7 py-3 text-[12px] font-black text-slate-600 hover:bg-[var(--accent)] hover:text-white transition-all uppercase tracking-widest border-b border-slate-50">Save & New</button>', '<button onclick="saveWarehouse(true)" class="w-full text-left px-7 py-3 text-[12px] font-black text-slate-600 hover:bg-[var(--accent)] hover:text-white transition-all uppercase tracking-widest border-b border-slate-50">Save & New</button>')
html = html.replace('<button class="w-full text-left px-7 py-3 text-[12px] font-black text-slate-600 hover:bg-[var(--accent)] hover:text-white transition-all uppercase tracking-widest">Save</button>', '<button onclick="saveWarehouse(false)" class="w-full text-left px-7 py-3 text-[12px] font-black text-slate-600 hover:bg-[var(--accent)] hover:text-white transition-all uppercase tracking-widest">Save</button>')

# ID mapping: find the label and the next input/select/textarea
id_map = {
    'STOCK LOCATION NAME': 'wh-name',
    'CONTACT PERSON': 'wh-contact-person',
    'LEDGER NAME \\*': 'wh-ledger-name',
    'EMAIL ID': 'wh-email',
    'PAN': 'wh-pan',
    'CONTACT MOBILE': 'wh-mobile',
    'WORK PHONE': 'wh-work-phone',
    'ADDRESS LINE 1': 'wh-addr1',
    'ADDRESS LINE 2': 'wh-addr2',
    'CITY / TOWN': 'wh-city',
    'POSTAL / ZIP CODE': 'wh-postal',
    'COUNTRY': 'wh-country',
    'STATE': 'wh-state',
    'ACCOUNT NAME': 'wh-bank-account-name',
    'ACCOUNT NUMBER': 'wh-bank-account-number',
    'ACCOUNT TYPE': 'wh-bank-account-type',
    'BANK NAME': 'wh-bank-name',
    'BANK BRANCH': 'wh-bank-branch',
    'IFSC CODE': 'wh-bank-ifsc',
    'Swift Code': 'wh-bank-swift',
    'Authorised Dealer Code': 'wh-bank-ad',
    'CORRESPONDENT BANK': 'wh-bank-correspondent'
}

for label, dom_id in id_map.items():
    if label == 'Swift Code' or label == 'Authorised Dealer Code':
        pattern = re.compile(rf'(?s)(<label[^>]*>.*?{label}.*?</label>\s*<(?:input|select|textarea)[^>]*?)(/?>)')
        html = pattern.sub(rf'\g<1> id="{dom_id}"\g<2>', html)
    else:
        pattern = re.compile(rf'(?s)(<label[^>]*>.*?{label}.*?</label>\s*<(?:input|select|textarea)[^>]*?)(/?>)')
        html = pattern.sub(rf'\g<1> id="{dom_id}"\g<2>', html)

with open('templates/warehouse.html', 'w', encoding='utf-8') as f:
    f.write(html)
