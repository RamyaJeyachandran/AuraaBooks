import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abproject.settings")
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_franchisee_tags (
        id bigserial PRIMARY KEY,
        created_at timestamp with time zone NOT NULL,
        updated_at timestamp with time zone NOT NULL,
        tag_name varchar(100) NOT NULL,
        franchisee_id bigint NOT NULL REFERENCES tbl_franchisee(id) DEFERRABLE INITIALLY DEFERRED
    );
    CREATE TABLE IF NOT EXISTS tbl_franchisee_attachments (
        id bigserial PRIMARY KEY,
        created_at timestamp with time zone NOT NULL,
        updated_at timestamp with time zone NOT NULL,
        file varchar(100) NOT NULL,
        filename varchar(255) NOT NULL,
        franchisee_id bigint NOT NULL REFERENCES tbl_franchisee(id) DEFERRABLE INITIALLY DEFERRED
    );
    """)
    print("Tables created successfully.")
