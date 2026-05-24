import sys
import os
import django

# Setup django environment if run directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models import Customer, Supplier, Item, Referrer, Branch

def seed():
    print("Seeding database...")
    
    # 1. Branch
    branches_data = ["Main Branch", "Secondary Branch"]
    for b_name in branches_data:
        Branch.objects.get_or_create(name=b_name)
        
    # 2. Customers
    customers_data = [
        {"name": "Balaji n", "email": "balaji@example.com", "mobile": "9876543210", "balance": 1500.00},
        {"name": "Harisha g", "email": "harisha@example.com", "mobile": "9876543211", "balance": 2300.00},
        {"name": "BASKAR Gumudipundi", "email": "baskar@example.com", "mobile": "9876543212", "balance": 0.00},
        {"name": "SakthiVel Madurai", "email": "sakthivel@example.com", "mobile": "9876543213", "balance": -500.00},
    ]
    for c in customers_data:
        Customer.objects.get_or_create(
            name=c["name"],
            defaults={"email": c["email"], "mobile": c["mobile"], "balance": c["balance"]}
        )
        
    # 3. Items
    items_data = [
        {"name": "Premium Paper Pack", "category": "Paper", "type": "Goods", "sku": "PPP-001", "hsn": "4802"},
        {"name": "Color Binder A4", "category": "Office Supplies", "type": "Goods", "sku": "CBA4-002", "hsn": "3926"},
        {"name": "Standard Card Holder", "category": "Office Supplies", "type": "Goods", "sku": "SCH-003", "hsn": "3926"},
    ]
    for it in items_data:
        Item.objects.get_or_create(
            name=it["name"],
            defaults={"category": it["category"], "type": it["type"], "sku": it["sku"], "hsn": it["hsn"]}
        )

    # 4. Suppliers
    suppliers_data = [
        {"name": "Supreme Stationers", "mobile": "9999999999", "balance": 0.00},
        {"name": "Global Paper Corp", "mobile": "8888888888", "balance": 12000.00},
    ]
    for s in suppliers_data:
        Supplier.objects.get_or_create(
            name=s["name"],
            defaults={"mobile": s["mobile"], "balance": s["balance"]}
        )

    # 5. Referrers
    referrers_data = [
        {"name": "Referrer Agent A", "mobile": "7777777777", "commission_percent": 5.00, "balance": 250.00},
    ]
    for r in referrers_data:
        Referrer.objects.get_or_create(
            name=r["name"],
            defaults={"mobile": r["mobile"], "commission_percent": r["commission_percent"], "balance": r["balance"]}
        )

    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed()
