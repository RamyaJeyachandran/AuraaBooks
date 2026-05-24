import os
import shutil

src = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"
dst = r"d:\AuraaZenAIProject\abproject\templates\purchase_payment.html"

shutil.copyfile(src, dst)

print("Copied purchase_bill.html to purchase_payment.html")
