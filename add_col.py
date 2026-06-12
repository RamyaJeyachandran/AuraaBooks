import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('ALTER TABLE public.tbl_units ADD COLUMN "relatedUnits" jsonb;')
    print("Column added.")
