with open('d:/AuraaZenAIProject/abproject/templates/purchase_bill.html', 'r', encoding='utf-8') as f:
    c = f.read()

m2 = c.find('id="newCashPurchaseModal"')
print('pbViewMenu inside newCashPurchaseModal:', c.find('id="pbViewMenu"', m2) != -1)
print('pbViewQuickBtn inside newCashPurchaseModal:', c.find('id="pbViewQuickBtn"', m2) != -1)
