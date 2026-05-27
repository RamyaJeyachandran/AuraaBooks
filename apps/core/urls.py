from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Masters
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('referrers/', views.ReferrerListView.as_view(), name='referrer-list'),
    path('warehouse/', views.WarehouseListView.as_view(), name='warehouse-list'),
    path('branch/', views.BranchListView.as_view(), name='branch-list'),
    path('franchisee/', views.FranchiseeListView.as_view(), name='franchisee-list'),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('sales-rep/', views.SalesRepListView.as_view(), name='sales-rep-list'),
    path('bank-cash/', views.BankCashListView.as_view(), name='bank-cash-list'),
    path('rate-sheet/', views.RateSheetListView.as_view(), name='rate-sheet-list'),
    path('stock-journal/', views.StockJournalListView.as_view(), name='stock-journal-list'), # FORCE RELOAD 2026-05-12

    # Sales
    path('sales/quotes/', views.SalesQuotesListView.as_view(), name='sales-quotes'),
    path('sales/orders/', views.SalesOrdersListView.as_view(), name='sales-orders'),
    path('sales/invoices/', views.SalesInvoicesListView.as_view(), name='sales-invoices'),
    path('sales/delivery-challan/', views.DeliveryChallanListView.as_view(), name='delivery-challan'),
    path('sales/credit-note/', views.CreditNoteListView.as_view(), name='sales-credit-note'),
    path('sales/receipt/', views.ReceiptListView.as_view(), name='sales-receipt'),

    # Purchase
    path('purchase/quotes/', views.PurchaseQuotesListView.as_view(), name='purchase-quotes'),
    path('purchase/orders/', views.PurchaseOrdersListView.as_view(), name='purchase-orders'),
    path('purchase/goods-receipt/', views.GoodsReceiptListView.as_view(), name='goods-receipt'),
    path('purchase/bills/', views.PurchaseBillView.as_view(), name='purchase-bills'),
    path('purchase/payments/', views.PurchasePaymentView.as_view(), name='purchase-payments'),
    path('purchase/credit-note/', views.SupplierCreditNoteListView.as_view(), name='supplier-credit-note'),

    # Expenses
    path('expenses/credit/', views.CreditExpenseListView.as_view(), name='credit-expenses'),
    path('expenses/asset/', views.AssetExpenseListView.as_view(), name='asset-expenses'),
    path('expenses/cash/', views.CashExpenseListView.as_view(), name='cash-expenses'),
    path('expenses/reclaim/', views.ReclaimExpenseListView.as_view(), name='reclaim-expenses'),

    # Accounting
    path('accounting/accounts/', views.AccountsListView.as_view(), name='accounts'),
    path('accounting/opening-balance/', views.OpeningBalanceListView.as_view(), name='opening-balance'),

    # Settings
    path('settings/', views.SettingsDashboardView.as_view(), name='settings-dashboard'),
    path('settings/smtp/', views.SmtpSettingsView.as_view(), name='smtp-settings'),
    path('settings/storage/', views.StorageLocationView.as_view(), name='storage-location'),
    path('settings/general/', views.GeneralSettingsView.as_view(), name='general-settings'),
    path('settings/preferences/', views.GenericMasterView.as_view(title='Preferences', parent_name='Settings'), name='preferences'),
    path('settings/customer-points/', views.CustomerPointsSettingsView.as_view(), name='customer-points-settings'),
    path('settings/qr-code/', views.QrCodeSettingsView.as_view(), name='qr-code-settings'),
    path('settings/units/', views.UnitsSettingsView.as_view(), name='units-settings'),
    path('settings/print/', views.PrintSettingsView.as_view(), name='print-settings'),
    path('settings/modules/', views.ModulesSettingsView.as_view(), name='modules-settings'),
    path('settings/serial-numbers/', views.SerialNumbersView.as_view(), name='serial-numbers-settings'),
    path('settings/company/', views.CompanySettingsView.as_view(), name='company-settings'),
    path('settings/default-content/', views.DefaultContentView.as_view(), name='default-content-settings'),
    path('settings/tax-rates/', views.TaxRatesSettingsView.as_view(), name='tax-rates-settings'),
    path('settings/custom-fields/', views.CustomFieldsView.as_view(), name='custom-fields-settings'),
    path('settings/users/', views.UsersSettingsView.as_view(), name='users-settings'),
]







