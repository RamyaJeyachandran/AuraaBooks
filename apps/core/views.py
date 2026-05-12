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
