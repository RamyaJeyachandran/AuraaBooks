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

class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Item(BaseModel):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('Goods', 'Goods'), ('Service', 'Service')])
    sku = models.CharField(max_length=50, blank=True, null=True)
    hsn = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Referrer(BaseModel):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Branch(BaseModel):
    name = models.CharField(max_length=255)
    
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
