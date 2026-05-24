with open('d:/AuraaZenAIProject/abproject/templates/purchase_bill.html', 'r', encoding='utf-8') as f:
    c = f.read()

m1 = c.find('id="newPurchaseModal"')
m2 = c.find('id="newCashPurchaseModal"')
q1 = c.find('id="pbQuickViewContent"', m1, m2)
q2 = c.find('id="pbQuickViewContent"', m2)

print('pbQuickViewContent inside newPurchaseModal:', q1 != -1)
print('pbQuickViewContent inside newCashPurchaseModal:', q2 != -1)

# also check if the Quick View Tabs container is inside
qtabs1 = c.find('id="pbQuickTabsContainer"', m1, m2)
qtabs2 = c.find('id="pbQuickTabsContainer"', m2)
print('pbQuickTabsContainer inside newPurchaseModal:', qtabs1 != -1)
print('pbQuickTabsContainer inside newCashPurchaseModal:', qtabs2 != -1)
