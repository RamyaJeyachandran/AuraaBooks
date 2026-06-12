from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'tbl_customer'

class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'tbl_supplier'

class Item(BaseModel):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('Goods', 'Goods'), ('Service', 'Service')])
    sku = models.CharField(max_length=50, blank=True, null=True)
    hsn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'tbl_item'

class Referrer(BaseModel):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'tbl_referrer'

class Branch(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ledger_name = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, db_column='mobileNo', blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(db_column='emailId', blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(db_column='isActive', default=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # New columns based on branch_analysis.md
    additional_info = models.TextField(blank=True, null=True)
    is_msme = models.BooleanField(default=False)
    msme_type = models.CharField(max_length=50, blank=True, null=True)
    msme_number = models.CharField(max_length=100, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    map_coordinates = models.CharField(max_length=255, blank=True, null=True)
    parent_branch = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_branches')
    
    # Existing DB columns we must define to keep Django happy if it wants to query them
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    createddt = models.DateTimeField(db_column='createdDt', blank=True, null=True)
    updateddt = models.DateTimeField(db_column='updatedDt', blank=True, null=True)



class EntityBankDetail(BaseModel):
    ENTITY_CHOICES = (
        ('Branch', 'Branch'),
        ('Warehouse', 'Warehouse'),
        ('Franchisee', 'Franchisee'),
    )
    entity_type = models.CharField(max_length=50, choices=ENTITY_CHOICES)
    entity_id = models.IntegerField()
    
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    ad_code = models.CharField(max_length=50, blank=True, null=True)
    correspondent_bank = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_entity_bank'
        indexes = [
            models.Index(fields=['entity_type', 'entity_id']),
        ]

class EntityShippingAddress(BaseModel):
    ENTITY_CHOICES = (
        ('Branch', 'Branch'),
        ('Warehouse', 'Warehouse'),
        ('Franchisee', 'Franchisee'),
    )
    entity_type = models.CharField(max_length=50, choices=ENTITY_CHOICES)
    entity_id = models.IntegerField()
    
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    shipping_ref_name = models.CharField(max_length=255, blank=True, null=True)
    shipping_gstin = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    map_coordinates = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_entity_shipping'
        indexes = [
            models.Index(fields=['entity_type', 'entity_id']),
        ]

class BranchTagAccess(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='tag_accesses')
    tag_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_branch_tags'

class Tag(BaseModel):
    name = models.CharField(max_length=100, db_column='tagName')
    tag_type = models.CharField(max_length=10, default='B', db_column='tagType')
    
    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

class Franchisee(BaseModel):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    ledger_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_msme = models.BooleanField(default=False)
    is_composition_scheme = models.BooleanField(default=False)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Address
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    state = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    
    # Shipping
    same_as_billing = models.BooleanField(default=True)
    shipping_ref_name = models.CharField(max_length=255, blank=True, null=True)
    shipping_gstin = models.CharField(max_length=15, blank=True, null=True)
    shipping_address1 = models.CharField(max_length=255, blank=True, null=True)
    shipping_address2 = models.CharField(max_length=255, blank=True, null=True)
    shipping_phone = models.CharField(max_length=20, blank=True, null=True)
    shipping_email = models.EmailField(blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=100, default='India')
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_latitude = models.CharField(max_length=50, blank=True, null=True)
    shipping_longitude = models.CharField(max_length=50, blank=True, null=True)
    
    # Bank
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    correspondent_bank = models.TextField(blank=True, null=True)
    dealer_code = models.CharField(max_length=50, blank=True, null=True)
    
    # Branch
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    assign_under_branch = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'tbl_franchisee'

class FranchiseeTagAccess(BaseModel):
    franchisee = models.ForeignKey(Franchisee, on_delete=models.CASCADE, related_name='tag_accesses')
    tag_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_franchisee_tags'

class FranchiseeAttachment(BaseModel):
    franchisee = models.ForeignKey(Franchisee, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='franchisee_attachments/')
    filename = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_franchisee_attachments'

class PremiumQuote(BaseModel):
    estimate_no = models.CharField(max_length=50, unique=True)
    estimate_type = models.CharField(max_length=50, default='Estimates')
    estimate_date = models.DateField()
    valid_till = models.DateField()
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='premium_quotes')
    buyer_order_no = models.CharField(max_length=100, blank=True, null=True)
    buyer_order_date = models.DateField(blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)
    
    sub_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    freight = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    packing = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    insurance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tcs = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    round_off = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    notes = models.TextField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    sales_rep = models.CharField(max_length=100, blank=True, null=True)
    project = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.estimate_no} - {self.customer.name}"
        
    class Meta:
        db_table = 'tbl_premiumquote'


class PremiumQuoteItem(BaseModel):
    quote = models.ForeignKey(PremiumQuote, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    unit = models.CharField(max_length=50, default='PCS')
    rate = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    discount_type = models.CharField(max_length=10, default='%')
    discount_value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    mrp = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    cost_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.item_name} for {self.quote.estimate_no}"
        
    class Meta:
        db_table = 'tbl_premiumquoteitem'

class Module(BaseModel):
    module_name = models.CharField(max_length=255)
    module_code = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='submodules')
    menu_type = models.CharField(max_length=20, choices=[('menu', 'menu'), ('submenu', 'submenu')])
    route_path = models.CharField(max_length=255, blank=True, null=True)
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    template_permissions = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.module_name
        
    class Meta:
        db_table = 'tbl_module'

class DocumentSequence(BaseModel):
    module = models.CharField(max_length=100)
    series_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20, choices=[('Auto', 'Auto'), ('Manual', 'Manual')], default='Auto')
    prefix = models.CharField(max_length=50, blank=True, null=True)
    next_number = models.IntegerField(default=1)
    suffix = models.CharField(max_length=50, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    financial_year = models.CharField(max_length=20, default='2026-2027')
    cid = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.module} - {self.series_name}"
        
    class Meta:
        db_table = 'tbl_documentsequence'

class CustomField(BaseModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    
    is_item_grid = models.BooleanField(default=False)
    include_total = models.BooleanField(default=False)
    is_required = models.BooleanField(default=False)
    display_in_print = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    subtypes = models.TextField(default='["All"]')
    cid = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.module} - {self.name}"
        
    class Meta:
        db_table = 'tbl_customfield'

class DefaultContent(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    email_subject = models.CharField(max_length=255, blank=True, null=True)
    email_content = models.TextField(blank=True, null=True)
    sms_msg_id = models.CharField(max_length=100, blank=True, null=True)
    sms_content = models.TextField(blank=True, null=True)
    whatsapp_msg_id = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_content = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'ab_compcontent'
        unique_together = ('branch', 'document_type', 'sub_type')

    def __str__(self):
        return f"{self.document_type} - {self.sub_type or 'Default'}"

class GeneralSettings(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    
    sales_form_config = models.TextField(blank=True, null=True, help_text="Maps to salSettings")
    sales_charges_config = models.TextField(blank=True, null=True, help_text="Maps to salChargesCode")
    purchase_charges_config = models.TextField(blank=True, null=True, help_text="Maps to purChargesCode")
    receipt_charges_config = models.TextField(blank=True, null=True, help_text="Maps to recpChargesCode")

    def __str__(self):
        return f"General Settings - Branch {self.branch_id} ({self.cid})"

    class Meta:
        db_table = 'ab_compsettings'

class SmtpSettings(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=1, choices=[('E', 'Email'), ('S', 'SMS')], default='E')
    settings = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"SMTP Settings - {self.type} ({self.cid})"

    class Meta:
        db_table = 'ab_compsmtp'

class StorageLocation(BaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    cid = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    range_from = models.CharField(max_length=100, blank=True, null=True)
    range_to = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        db_table = 'ab_storage'

class UserRole(BaseModel):
    role_name = models.CharField(max_length=50)
    permission_level = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'ab_role'

class UserRolePermission(BaseModel):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='permissions')
    module_name = models.CharField(max_length=50)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    extras = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = 'ab_role_permissions'

class AppUser(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    signature_url = models.CharField(max_length=500, null=True, blank=True)
    locations = models.JSONField(default=list, blank=True, help_text="Array of location codes like ['B-1', 'W-2']")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ab_users'

class UserActivityLog(BaseModel):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    user_name_snapshot = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=500)
    log_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    extra_info = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user_name_snapshot} - {self.action}"

    class Meta:
        db_table = 'ab_trans_log'

class AccessDevice(BaseModel):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    last_access = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ab_devices'

class Warehouse(BaseModel):
    # Basic Info
    name = models.CharField(max_length=255, verbose_name="Stock Location Name")
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    ledger_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    is_msme = models.BooleanField(default=False)
    msme_type = models.CharField(max_length=50, blank=True, null=True)
    msme_number = models.CharField(max_length=100, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    work_phone = models.CharField(max_length=20, blank=True, null=True)
    is_composition_scheme = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    attachments = models.TextField(blank=True, null=True, help_text="JSON array of attached file paths/data")
    address_branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, related_name='address_warehouses')
    bank_branch_assigned = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, related_name='bank_warehouses')

    # Note: Address and Bank details are now handled by EntityBankDetail and EntityShippingAddress

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_warehouse'

class Unit(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    descr = models.TextField(blank=True, null=True)
    convFactor = models.DecimalField(max_digits=18, decimal_places=6, default=1.0, db_column='convFactor')
    companyId = models.IntegerField(null=True, blank=True, db_column='companyId')
    branchId = models.IntegerField(null=True, blank=True, db_column='branchId')
    isActive = models.BooleanField(default=True, db_column='isActive')
    isDefault = models.BooleanField(default=False, db_column='isDefault')
    createdBy = models.IntegerField(null=True, blank=True, db_column='createdBy')
    createdDt = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_column='createdDt')
    updatedDt = models.DateTimeField(auto_now=True, null=True, blank=True, db_column='updatedDt')
    updatedBy = models.IntegerField(null=True, blank=True, db_column='updatedBy')
    
    relatedUnits = models.JSONField(default=list, blank=True, null=True, db_column='relatedUnits', help_text="Stores multiple related units and their conversion factors like [{'relatedUnitId': 2, 'convFactor': 10}]")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_units'
