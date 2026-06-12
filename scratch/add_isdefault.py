import os
import sys
import django

sys.path.append(r"D:\AuraaZenAIProject\abproject")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    try:
        cursor.execute('ALTER TABLE tbl_units ADD COLUMN "isDefault" BOOLEAN DEFAULT false;')
        print("Column isDefault added successfully.")
    except Exception as e:
        print(f"Error: {e}")
