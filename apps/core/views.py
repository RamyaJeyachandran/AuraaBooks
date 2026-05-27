from django.shortcuts import render
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class GenericMasterView(TemplateView):
    template_name = 'generic_page.html'
    title = ""
    parent_name = ""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['parent_name'] = self.parent_name
        return context

class CustomerListView(TemplateView):
    template_name = 'customers.html'

class SupplierListView(TemplateView):
    template_name = 'suppliers.html'

class ItemListView(TemplateView):
    template_name = 'items.html'

class ReferrerListView(TemplateView):
    template_name = 'referrers.html'

class WarehouseListView(TemplateView):
    template_name = 'warehouse.html'

class PurchaseListView(TemplateView):
    template_name = 'purchases.html'

class ExpenseListView(TemplateView):
    template_name = 'expenses.html'

class AccountingView(TemplateView):
    template_name = 'accounting.html'

class BranchListView(TemplateView):
    template_name = 'branch.html'

class FranchiseeListView(TemplateView):
    template_name = 'franchisee.html'

    def get_context_data(self, **kwargs):
        from .models import Branch
        context = super().get_context_data(**kwargs)
        context['branches'] = Branch.objects.all()
        return context

class ProjectListView(TemplateView):
    template_name = 'project.html'

class SalesRepListView(TemplateView):
    template_name = 'sales_rep.html'

class BankCashListView(TemplateView):
    template_name = 'banks_cash.html'

class RateSheetListView(TemplateView):
    template_name = 'rate_sheet.html'

class StockJournalListView(TemplateView):
    template_name = 'stock_journal.html'
class CreditExpenseListView(TemplateView):
    template_name = 'expenses_credit.html'

class AssetExpenseListView(TemplateView):
    template_name = 'expenses_asset.html'

class CashExpenseListView(TemplateView):
    template_name = 'expenses_cash.html'

class ReclaimExpenseListView(TemplateView):
    template_name = 'expenses_reclaim.html'

class DeliveryChallanListView(TemplateView):
    template_name = 'sales_delivery_challan.html'

class CreditNoteListView(TemplateView):
    template_name = 'sales_credit_note.html'

class ReceiptListView(TemplateView):
    template_name = 'sales_receipt.html'


class SalesQuotesListView(TemplateView):
    template_name = 'sales_quotes.html'

    def get_context_data(self, **kwargs):
        from .models import PremiumQuote, Customer
        context = super().get_context_data(**kwargs)
        context['premium_quotes'] = PremiumQuote.objects.all().order_by('-id')
        context['customers'] = Customer.objects.all()
        return context


class SalesOrdersListView(TemplateView):
    template_name = 'sales_orders.html'


class SalesInvoicesListView(TemplateView):
    template_name = 'sales_invoices.html'


class PurchaseQuotesListView(TemplateView):
    template_name = 'purchase_quotes.html'

class PurchaseOrdersListView(TemplateView):
    template_name = 'purchase_orders.html'

class SupplierCreditNoteListView(TemplateView):
    template_name = 'supplier_credit_note.html'

class GoodsReceiptListView(TemplateView):
    template_name = 'goods_receipt.html'

class PurchaseBillView(TemplateView):
    template_name = 'purchase_bill.html'

class PurchasePaymentView(TemplateView):
    template_name = 'purchase_payment.html'


class AccountsListView(TemplateView):
    template_name = 'accounts.html'


class OpeningBalanceListView(TemplateView):
    template_name = 'opening_balance.html'


class SettingsDashboardView(TemplateView):
    template_name = 'settings_dashboard.html'


class SmtpSettingsView(TemplateView):
    template_name = 'smtp_settings.html'


class StorageLocationView(TemplateView):
    template_name = 'storage_location.html'


class CustomerPointsSettingsView(TemplateView):
    template_name = 'customer_points_settings.html'


class QrCodeSettingsView(TemplateView):
    template_name = 'qr_code_settings.html'


class UnitsSettingsView(TemplateView):
    template_name = 'units_settings.html'


class PrintSettingsView(TemplateView):
    template_name = 'print_settings.html'


class ModulesSettingsView(TemplateView):
    template_name = 'modules_settings.html'


class SerialNumbersView(TemplateView):
    template_name = 'serial_numbers_settings.html'


class CompanySettingsView(TemplateView):
    template_name = 'company_settings.html'


class DefaultContentView(TemplateView):
    template_name = 'default_content_settings.html'


class TaxRatesSettingsView(TemplateView):
    template_name = 'tax_rates_settings.html'


class CustomFieldsView(TemplateView):
    template_name = 'custom_fields_settings.html'


class GeneralSettingsView(TemplateView):
    template_name = 'general_settings.html'


class UsersSettingsView(TemplateView):
    template_name = 'users_settings.html'
















