import os
import sys

# Add /app to python path so it can find abproject
sys.path.append('/app')

import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abproject.settings')
django.setup()

commands = [
    # Branch
    "ALTER TABLE tbl_branch ADD COLUMN additional_info TEXT NULL;",
    "ALTER TABLE tbl_branch ADD COLUMN is_msme BOOLEAN NOT NULL DEFAULT FALSE;",
    "ALTER TABLE tbl_branch ADD COLUMN attachment VARCHAR(255) NULL;",
    "ALTER TABLE tbl_branch ADD COLUMN map_coordinates VARCHAR(255) NULL;",
    "ALTER TABLE tbl_branch ADD COLUMN parent_branch_id BIGINT NULL REFERENCES tbl_branch(id) ON DELETE SET NULL DEFERRABLE INITIALLY DEFERRED;",
    
    # BranchBankDetail
    "ALTER TABLE tbl_branch_bank ADD COLUMN ad_code VARCHAR(50) NULL;",
    "ALTER TABLE tbl_branch_bank ADD COLUMN correspondent_bank VARCHAR(255) NULL;",
    
    # BranchShippingAddress
    "ALTER TABLE tbl_branch_shipping ADD COLUMN shipping_ref_name VARCHAR(255) NULL;",
    "ALTER TABLE tbl_branch_shipping ADD COLUMN shipping_gstin VARCHAR(15) NULL;",
    "ALTER TABLE tbl_branch_shipping ADD COLUMN email VARCHAR(254) NULL;",
    "ALTER TABLE tbl_branch_shipping ADD COLUMN map_coordinates VARCHAR(255) NULL;"
]

with connection.cursor() as cursor:
    for cmd in commands:
        try:
            cursor.execute(cmd)
            print(f"Executed: {cmd}")
        except Exception as e:
            print(f"Error on {cmd}: {e}")
            # If a column already exists, just continue
            pass

print("Finished applying raw SQL updates.")
