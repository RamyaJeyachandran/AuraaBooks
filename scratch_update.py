import re

file_path = r'd:\AuraaZenAIProject\abproject\templates\sales_invoices.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ID to header and back button
content = content.replace(
    '<div class="px-6 flex items-center justify-between bg-[var(--accent)] border-b border-white/10 h-[60px] shrink-0">',
    '<div id="invoiceModalHeader" class="px-6 flex items-center justify-between bg-[var(--accent)] border-b border-white/10 h-[60px] shrink-0 transition-colors">'
)
content = content.replace(
    '<button class="text-[18px] font-bold text-white flex items-center gap-1 hover:text-white/80 outline-none">',
    '<button id="modalBackButton" onclick="closeModal()" class="text-[18px] font-bold text-white flex items-center gap-1 hover:opacity-80 outline-none transition-colors">'
)

# 2. Add 'openModal' and 'closeModal'
script_start = "    function toggleActionMenu(event, menuId) {"
new_funcs = """    function openModal(title) {
        const overlay = document.getElementById('modalOverlay');
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
        }
        if (title === 'Cash Invoice') {
            setInvoiceType('Cash');
        } else {
            setInvoiceType('Credit');
        }
    }

    function closeModal() {
        const overlay = document.getElementById('modalOverlay');
        if (overlay) {
            overlay.classList.add('hidden');
            overlay.classList.remove('flex');
        }
    }

"""
if "function openModal(" not in content:
    content = content.replace(script_start, new_funcs + script_start)

# 3. Update Print / Save buttons to be green
# Print Button Group
content = content.replace(
    '<div class="relative group/print h-8 shadow-sm">\n                            <div class="flex items-stretch h-full rounded overflow-hidden border border-[var(--accent)]/10">\n                                <button type="button" class="px-4 h-full bg-white hover:bg-slate-50 text-[var(--accent)] text-[13px] font-bold transition-colors outline-none uppercase tracking-widest">\n                                    Print\n                                </button>\n                                <button type="button" onclick="toggleActionMenu(event, \'printSplitMenu\')" class="px-2 h-full bg-white hover:bg-slate-50 text-[var(--accent)] border-l border-[var(--accent)]/10 flex items-center justify-center transition-colors outline-none">\n                                    <span class="text-[10px]">▼</span>\n                                </button>\n                            </div>',
    '<div class="relative group/print h-8 shadow-sm">\n                            <div class="flex items-stretch h-full rounded overflow-hidden">\n                                <button type="button" class="px-4 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white text-[13px] font-bold transition-colors outline-none">\n                                    Print\n                                </button>\n                                <button type="button" onclick="toggleActionMenu(event, \'printSplitMenu\')" class="px-2 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white border-l border-white/20 flex items-center justify-center transition-colors outline-none">\n                                    <span class="text-[10px]">▼</span>\n                                </button>\n                            </div>'
)

# Save Button Group
content = content.replace(
    '<div class="relative group/save h-8 shadow-sm">\n                            <div class="flex items-stretch h-full rounded overflow-hidden border border-[var(--accent)]/10">\n                                <button type="button" onclick="saveInvoice()" class="px-5 h-full bg-white hover:bg-slate-50 text-[var(--accent)] text-[13px] font-bold transition-colors outline-none uppercase tracking-widest">\n                                    Save\n                                </button>\n                                <button type="button" onclick="toggleActionMenu(event, \'saveSplitMenu\')" class="px-2 h-full bg-white hover:bg-slate-50 text-[var(--accent)] border-l border-[var(--accent)]/10 flex items-center justify-center transition-colors outline-none">\n                                    <span class="text-[10px]">▼</span>\n                                </button>\n                            </div>',
    '<div class="relative group/save h-8 shadow-sm">\n                            <div class="flex items-stretch h-full rounded overflow-hidden">\n                                <button type="button" onclick="saveInvoice()" class="px-5 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white text-[13px] font-bold transition-colors outline-none">\n                                    Save\n                                </button>\n                                <button type="button" onclick="toggleActionMenu(event, \'saveSplitMenu\')" class="px-2 h-full bg-[#10b981] hover:bg-[#0ea5e9] text-white border-l border-white/20 flex items-center justify-center transition-colors outline-none">\n                                    <span class="text-[10px]">▼</span>\n                                </button>\n                            </div>'
)

# Add Save Dropdown contents explicitly to match user request
content = content.replace(
    """<div id="saveSplitMenu" class="hidden absolute top-full right-0 mt-1 w-48 bg-white rounded shadow-xl border border-slate-200 py-2 z-[600]">
                                <button type="button" onclick="selectSaveOption('Save & New')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save & New</button>
                                <button type="button" onclick="selectSaveOption('Save as Draft')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft</button>
                                <button type="button" onclick="selectSaveOption('Save as Draft & New')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft & New</button>
                                <button type="button" onclick="selectSaveOption('Save')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save</button>
                            </div>""",
    """<div id="saveSplitMenu" class="hidden absolute top-full right-0 mt-1 w-40 bg-white rounded shadow-xl border border-slate-200 py-2 z-[600]">
                                <button type="button" onclick="selectSaveOption('Save & New')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save & New</button>
                                <button type="button" onclick="selectSaveOption('Save')" class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Save</button>
                            </div>"""
)

# Add Deposit A/C and Reference underneath Customer
old_fields = """                    <!-- Top Settings Cog -->
                    <div class="absolute -right-2 -top-2">"""

new_fields = """                    <!-- Cash Invoice Specific Fields (Hidden by default) -->
                    <div id="cashInvoiceFields" class="hidden col-span-4 grid grid-cols-4 gap-6 pt-4 border-t border-slate-100">
                        <div class="col-span-2">
                            <!-- spacer -->
                        </div>
                        <div class="flex flex-col gap-1">
                            <label class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Deposit A/C</label>
                            <div class="relative">
                                <select class="w-full h-9 bg-white border border-slate-300 rounded px-3 text-[13px] font-bold text-slate-700 outline-none appearance-none">
                                    <option>Cash</option>
                                    <option>Bank</option>
                                </select>
                                <span class="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] pointer-events-none text-slate-400">▼</span>
                            </div>
                        </div>
                        <div class="flex items-end gap-2">
                            <div class="flex flex-col gap-1 flex-1">
                                <label class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Reference</label>
                                <div class="flex border border-slate-300 rounded overflow-hidden">
                                    <div class="relative w-24 border-r border-slate-300">
                                        <select class="w-full h-9 bg-white px-3 text-[12px] font-bold text-slate-700 outline-none appearance-none">
                                            <option>Cash</option>
                                        </select>
                                        <span class="absolute right-2 top-1/2 -translate-y-1/2 text-[10px] pointer-events-none text-slate-400">▼</span>
                                    </div>
                                    <input type="text" class="flex-1 h-9 px-3 text-[13px] font-bold text-slate-700 outline-none">
                                </div>
                            </div>
                            <!-- Dropdown + button -->
                            <div class="relative">
                                <div class="flex items-stretch h-9 border border-slate-300 rounded overflow-hidden">
                                    <button class="px-3 bg-slate-100 hover:bg-slate-200 text-slate-600 font-black border-r border-slate-300 transition-colors">+</button>
                                    <button onclick="toggleActionMenu(event, 'cashAddMenu')" class="px-2 bg-slate-100 hover:bg-slate-200 text-slate-600 transition-colors"><span class="text-[10px]">▼</span></button>
                                </div>
                                <div id="cashAddMenu" class="hidden absolute top-full right-0 mt-1 w-40 bg-white rounded shadow-xl border border-slate-200 py-1 z-[600]">
                                    <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Add Cash/Bank</button>
                                    <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50">Add Account</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Top Settings Cog -->
                    <div class="absolute -right-2 -top-2">"""
if "id=\"cashInvoiceFields\"" not in content:
    content = content.replace(old_fields, new_fields)

# 5. Update setInvoiceType
set_invoice_type_old = """    function setInvoiceType(type) {
        const titleEl = document.getElementById('modalTitleText');
        const customerLabel = document.getElementById('customerLabel');
        const searchInput = document.getElementById('customerSearch');
        const cashBtn = document.getElementById('btnCashToggle');
        const creditBtn = document.getElementById('btnCreditToggle');
        const centerTabs = document.getElementById('centerTabs');"""

set_invoice_type_new = """    function setInvoiceType(type) {
        const titleEl = document.getElementById('modalTitleText');
        const customerLabel = document.getElementById('customerLabel');
        const searchInput = document.getElementById('customerSearch');
        const cashBtn = document.getElementById('btnCashToggle');
        const creditBtn = document.getElementById('btnCreditToggle');
        const centerTabs = document.getElementById('centerTabs');
        
        const header = document.getElementById('invoiceModalHeader');
        const backBtn = document.getElementById('modalBackButton');
        const cashFields = document.getElementById('cashInvoiceFields');"""

if "const header = document.getElementById('invoiceModalHeader');" not in content:
    content = content.replace(set_invoice_type_old, set_invoice_type_new)

type_cash_old = """        if (type === 'Cash') {
            titleEl.textContent = 'New Cash Invoice';
            customerLabel.innerHTML = 'Item <span class="text-[10px]">▼</span>';
            
            cashBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-[var(--accent)] text-white transition-colors w-16 text-center';
            creditBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-white text-[var(--accent)] transition-colors w-16 text-center';
            
            if(centerTabs) centerTabs.classList.remove('hidden');"""

type_cash_new = """        if (type === 'Cash') {
            titleEl.textContent = 'New Cash Invoice';
            customerLabel.innerHTML = 'Item <span class="text-[10px]">▼</span>';
            
            if(cashBtn) cashBtn.parentElement.classList.add('hidden'); // Hide toggle in Cash Invoice mode
            if(cashFields) cashFields.classList.remove('hidden');
            
            if(header) {
                header.classList.remove('bg-[var(--accent)]', 'border-white/10');
                header.classList.add('bg-slate-50', 'border-slate-200');
            }
            if(backBtn) {
                backBtn.classList.remove('text-white', 'hover:text-white/80');
                backBtn.classList.add('text-slate-800', 'hover:text-slate-600');
            }
            
            if(centerTabs) centerTabs.classList.remove('hidden');"""

if "if(cashBtn) cashBtn.parentElement.classList.add('hidden');" not in content:
    content = content.replace(type_cash_old, type_cash_new)

type_credit_old = """        } else {
            titleEl.textContent = 'New Invoice';
            customerLabel.innerHTML = 'Customer <span class="text-[10px]">▼</span>';
            
            cashBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-white text-[var(--accent)] transition-colors w-16 text-center';
            creditBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-[var(--accent)] text-white transition-colors w-16 text-center';
            
            if(centerTabs) centerTabs.classList.add('hidden');
        }"""

type_credit_new = """        } else {
            titleEl.textContent = 'New Invoice';
            customerLabel.innerHTML = 'Customer <span class="text-[10px]">▼</span>';
            
            if(cashBtn) cashBtn.parentElement.classList.remove('hidden');
            if(cashBtn) cashBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-white text-[var(--accent)] transition-colors w-16 text-center';
            if(creditBtn) creditBtn.className = 'px-4 py-1.5 text-[13px] font-bold bg-[var(--accent)] text-white transition-colors w-16 text-center';
            if(cashFields) cashFields.classList.add('hidden');
            
            if(header) {
                header.classList.add('bg-[var(--accent)]', 'border-white/10');
                header.classList.remove('bg-slate-50', 'border-slate-200');
            }
            if(backBtn) {
                backBtn.classList.add('text-white', 'hover:text-white/80');
                backBtn.classList.remove('text-slate-800', 'hover:text-slate-600');
            }
            
            if(centerTabs) centerTabs.classList.add('hidden');
        }"""
if "if(cashBtn) cashBtn.parentElement.classList.remove('hidden');" not in content:
    content = content.replace(type_credit_old, type_credit_new)

# 6. Change labels based on type
content = content.replace(
    '<label class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Invoice No',
    '<label id="invNoLabel" class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Invoice No'
)
content = content.replace(
    '<label class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Invoice Date',
    '<label id="invDateLabel" class="text-[12px] font-bold text-slate-700 flex items-center gap-1">Invoice Date'
)

label_changes_cash = """            if(document.getElementById('invNoLabel')) document.getElementById('invNoLabel').childNodes[0].nodeValue = 'Cash Invoice No ';
            if(document.getElementById('invDateLabel')) document.getElementById('invDateLabel').childNodes[0].nodeValue = 'Cash Invoice Date ';\n"""
if "document.getElementById('invNoLabel').childNodes[0].nodeValue = 'Cash Invoice No '" not in content:
    content = content.replace("            if(cashFields) cashFields.classList.remove('hidden');", "            if(cashFields) cashFields.classList.remove('hidden');\n" + label_changes_cash)

label_changes_credit = """            if(document.getElementById('invNoLabel')) document.getElementById('invNoLabel').childNodes[0].nodeValue = 'Invoice No ';
            if(document.getElementById('invDateLabel')) document.getElementById('invDateLabel').childNodes[0].nodeValue = 'Invoice Date ';\n"""
if "document.getElementById('invNoLabel').childNodes[0].nodeValue = 'Invoice No '" not in content:
    content = content.replace("            if(cashFields) cashFields.classList.add('hidden');", "            if(cashFields) cashFields.classList.add('hidden');\n" + label_changes_credit)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates successful")
