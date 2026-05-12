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
    path('sales/quotes/', views.GenericMasterView.as_view(title='Sales Quotes', parent_name='Sales'), name='sales-quotes'),
    path('sales/orders/', views.GenericMasterView.as_view(title='Sales Orders', parent_name='Sales'), name='sales-orders'),
    path('sales/invoices/', views.GenericMasterView.as_view(title='Invoices', parent_name='Sales'), name='sales-invoices'),
    path('sales/delivery-challan/', views.DeliveryChallanListView.as_view(), name='delivery-challan'),
    path('sales/credit-note/', views.CreditNoteListView.as_view(), name='sales-credit-note'),
    path('sales/receipt/', views.ReceiptListView.as_view(), name='sales-receipt'),

    # Purchase
    path('purchase/quotes/', views.GenericMasterView.as_view(title='Purchase Quotes', parent_name='Purchase'), name='purchase-quotes'),
    path('purchase/orders/', views.GenericMasterView.as_view(title='Purchase Orders', parent_name='Purchase'), name='purchase-orders'),
    path('purchase/goods-receipt/', views.GenericMasterView.as_view(title='Goods Receipt', parent_name='Purchase'), name='goods-receipt'),
    path('purchase/bills/', views.GenericMasterView.as_view(title='Purchase Bills', parent_name='Purchase'), name='purchase-bills'),
    path('purchase/payments/', views.GenericMasterView.as_view(title='Payments', parent_name='Purchase'), name='purchase-payments'),
    path('purchase/credit-note/', views.GenericMasterView.as_view(title='Supplier Credit Note', parent_name='Purchase'), name='supplier-credit-note'),

    # Expenses
    path('expenses/credit/', views.CreditExpenseListView.as_view(), name='credit-expenses'),
    path('expenses/asset/', views.AssetExpenseListView.as_view(), name='asset-expenses'),
    path('expenses/cash/', views.CashExpenseListView.as_view(), name='cash-expenses'),
    path('expenses/reclaim/', views.ReclaimExpenseListView.as_view(), name='reclaim-expenses'),

    # Accounting
    path('accounting/accounts/', views.GenericMasterView.as_view(title='Accounts', parent_name='Accounting'), name='accounts'),
    path('accounting/opening-balance/', views.GenericMasterView.as_view(title='Opening Balance', parent_name='Accounting'), name='opening-balance'),
]
