import os

filepath = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the button to trigger openNewCashPurchaseModal()
content = content.replace(
    '<button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">\n                New Cash Purchase\n            </button>',
    '<button onclick="openNewCashPurchaseModal()" class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">\n                New Cash Purchase\n            </button>'
)

# 2. HTML block for New Cash Purchase Modal
cash_modal_html = """
<!-- New Cash Purchase Modal -->
<div id="newCashPurchaseModal" class="hidden fixed inset-0 z-[1000] flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4">
    <div class="bg-slate-50 w-full h-full max-w-[1920px] rounded-2xl shadow-2xl flex flex-col overflow-hidden animate-in zoom-in-95 duration-200">
        
        <!-- Modal Header -->
        <div class="h-16 bg-[var(--accent)] border-b border-[var(--accent)]/10 px-6 flex items-center justify-between shrink-0">
            <div class="flex items-center gap-4">
                <div class="flex flex-col">
                    <h2 class="text-[18px] font-black text-white flex items-center gap-1">
                        New Cash Purchase
                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </h2>
                    <span class="text-[12px] font-bold text-white/80 flex items-center gap-1">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
                        Main Branch
                    </span>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <div class="relative flex items-center shadow-sm rounded-lg overflow-hidden h-9">
                    <button class="px-4 h-full bg-white text-[var(--accent)] border-y border-l border-[var(--accent)] text-[13px] font-bold hover:bg-slate-50 transition-all flex items-center gap-2" title="Save this purchase">
                        Save
                    </button>
                    <button class="px-2 h-full bg-white text-[var(--accent)] border-y border-r border-l border-[var(--accent)] hover:bg-slate-50 transition-all flex items-center justify-center">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </button>
                </div>
                <button onclick="closeNewCashPurchaseModal()" class="px-4 h-9 bg-slate-700 text-white rounded-lg text-[13px] font-bold hover:bg-slate-800 transition-all shadow-sm" title="Cancel">Cancel</button>
                <button onclick="closeNewCashPurchaseModal()" class="w-9 h-9 bg-red-500 text-white rounded-lg flex items-center justify-center hover:bg-red-600 transition-all shadow-sm" title="Close">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
        </div>

        <!-- Modal Body (Normal View equivalent) -->
        <div class="flex-1 overflow-auto bg-slate-50 p-6 flex flex-col">
            <div class="w-full max-w-[1400px] mx-auto bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col">
                
                <!-- Top Form Fields -->
                <div class="p-6 border-b border-slate-200 space-y-5">
                    
                    <!-- Single Row Fields -->
                    <div class="grid grid-cols-5 gap-6">
                        <!-- Purchase Bill No -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Purchase Bill No <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>
                            <div class="text-[16px] font-black text-slate-800 mt-2" title="Purchase Bill Number">1</div>
                        </div>

                        <!-- Bill Date -->
                        <div class="relative">
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center justify-between">
                                <span class="flex items-center gap-1">Bill Date <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>
                                <button onclick="toggleActionMenu(event, 'pbCashBillDateSettings')" class="text-slate-400 hover:text-[var(--accent)]" title="Bill Date Settings">
                                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                </button>
                            </label>
                            <div class="relative">
                                <input type="text" value="24/05/2026" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-700 outline-none focus:border-[var(--accent)]" title="Select Date">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                            </div>
                            
                            <!-- Popover: Bill Date Settings -->
                            <div id="pbCashBillDateSettings" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl border border-slate-100 p-4 z-[500]">
                                <div class="absolute -top-1.5 right-6 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                <div class="space-y-4">
                                    <label class="flex items-center gap-3 cursor-pointer">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                        <span class="text-[13px] text-slate-700">Show Reverse Charge</span>
                                    </label>
                                    <label class="flex items-center gap-3 cursor-pointer opacity-50">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300" disabled>
                                        <span class="text-[13px] text-slate-700">Tax Round Off</span>
                                    </label>
                                    <div class="text-[13px] text-slate-700 pt-1">
                                        Initial Focus <a href="#" class="text-blue-500 hover:underline ml-1 font-medium">Date</a>
                                    </div>
                                    <label class="flex items-center gap-3 cursor-pointer">
                                        <input type="checkbox" class="w-4 h-4 accent-[var(--accent)] rounded border-slate-300">
                                        <span class="text-[13px] text-slate-700">Ignore Auto Select if multiple Attributes</span>
                                    </label>
                                    <div class="pt-1">
                                        <a href="#" class="text-blue-500 hover:underline text-[13px]">Manage Custom Fields...</a>
                                    </div>
                                    <div class="pt-2">
                                        <button class="px-5 py-2 bg-[#22c55e] text-white rounded font-bold text-[13px] hover:bg-green-600 transition-all">Save</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Supplier / Vendor -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier / Vendor <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none focus:border-[var(--accent)] appearance-none" title="Supplier / Vendor">
                                    <option>Select Contact (F9)</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>

                        <!-- Supplier Invoice No -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier Invoice No</label>
                            <input type="text" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-700 outline-none focus:border-[var(--accent)]" title="Supplier Invoice No">
                        </div>

                        <!-- Supplier Invoice Date -->
                        <div>
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Supplier Invoice Date</label>
                            <div class="relative">
                                <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none focus:border-[var(--accent)]" title="Supplier Invoice Date">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                            </div>
                        </div>
                    </div>

                    <!-- Dynamic Payment Fields Container -->
                    <div id="pbCashPaymentRowsContainer" class="space-y-4 pt-2 border-t border-slate-100">
                        <div class="flex items-end gap-6 payment-row">
                            <div class="w-64">
                                <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Paid from A/C</label>
                                <div class="relative">
                                    <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none" title="Paid from Account">
                                        <option>Cash</option>
                                    </select>
                                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                            </div>
                            <div class="w-96">
                                <label class="text-[12px] font-bold text-slate-500 mb-1.5 flex items-center gap-1">Reference</label>
                                <div class="flex items-center h-10 border border-slate-200 rounded bg-white">
                                    <div class="relative border-r border-slate-200 h-full w-24">
                                        <select class="w-full h-full bg-transparent px-3 text-[13px] text-slate-500 outline-none appearance-none" title="Reference Type">
                                            <option>Cash</option>
                                        </select>
                                        <svg class="w-3 h-3 text-slate-400 absolute right-2 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                    </div>
                                    <input type="text" class="flex-1 h-full px-3 text-[13px] bg-transparent outline-none" title="Reference Number">
                                </div>
                            </div>
                            <button type="button" onclick="addPbCashPaymentRow()" class="w-10 h-10 bg-slate-200 hover:bg-slate-300 rounded flex items-center justify-center transition-all text-slate-500" title="Add Row">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
                            </button>
                        </div>
                    </div>
                    
                </div>

                <!-- Table Section -->
                <div class="flex-1 overflow-hidden flex flex-col p-6">
                    <div class="border border-slate-200 rounded-xl overflow-hidden flex flex-col h-[360px] shadow-sm">
                        <!-- Table Header -->
                        <div class="flex items-center h-12 bg-[var(--accent)] text-white border-b border-slate-200 shrink-0">
                            <div class="w-16 px-4 text-[12px] font-bold">S.No</div>
                            <div class="flex-1 px-4 text-[12px] font-bold">Item/Account</div>
                            <div class="w-48 px-4 flex items-center gap-2">
                                <div class="relative flex-1">
                                    <input type="text" placeholder="Search..." class="w-full h-8 bg-white/10 border border-white/20 rounded px-3 text-[12px] text-white placeholder-white/50 outline-none focus:border-white transition-all" title="Search Items">
                                </div>
                                <button class="text-white hover:text-blue-200" title="Download Template">
                                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
                                </button>
                            </div>
                            <div class="w-24 px-4 text-[12px] font-bold text-center">Qty</div>
                            <div class="w-32 px-4 text-[12px] font-bold text-right">Rate ₹</div>
                            <div class="w-32 px-4 text-[12px] font-bold text-right">Amount</div>
                            <div class="w-12 flex justify-center border-l border-white/20 relative">
                                <button onclick="toggleActionMenu(event, 'pbCashTableSettings')" class="w-8 h-8 flex items-center justify-center hover:bg-white/10 rounded" title="Table Settings">
                                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                </button>
                                
                                <!-- Table Settings Popover -->
                                <div id="pbCashTableSettings" class="hidden absolute top-full right-0 mt-2 w-72 bg-white rounded-lg shadow-2xl border border-slate-100 p-2 z-[500] text-left">
                                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                    <div class="max-h-[400px] overflow-y-auto px-2 py-1 space-y-2">
                                        <!-- Options from Image 4 -->
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>D</u>escription (Below Item)</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>S</u>KU</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>H</u>SN / SAC</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>A</u>ccount</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>T</u>ax</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>L</u>ocation</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3 opacity-60">
                                                <input type="checkbox" checked disabled class="w-3.5 h-3.5 accent-slate-400 rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Qty</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3 opacity-60">
                                                <input type="checkbox" checked disabled class="w-3.5 h-3.5 accent-slate-400 rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Rate</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>U</u>nit</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Net Rate</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700"><u>M</u>RP</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Discount Per Item</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Discount Overall</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" checked class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Group Similar Item</span>
                                            </div>
                                        </label>
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Charges Amount</span>
                                            </div>
                                            <svg class="w-4 h-4 text-blue-400 opacity-50 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                        </label>
                                        
                                        <div class="pt-1">
                                            <a href="#" class="text-blue-500 hover:underline text-[13px]">Manage Custom Fields...</a>
                                        </div>
                                        
                                        <label class="flex items-center justify-between cursor-pointer group">
                                            <div class="flex items-center gap-3">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded border-slate-300">
                                                <span class="text-[12px] text-slate-700">Item Details in Popup</span>
                                            </div>
                                        </label>
                                        
                                        <div class="pt-2 flex gap-2">
                                            <button class="px-5 py-2 bg-[#22c55e] text-white rounded font-bold text-[13px] hover:bg-green-600 transition-all">Save</button>
                                            <button class="px-5 py-2 bg-slate-200 text-slate-600 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Table Rows -->
                        <div class="flex-1 overflow-y-auto">
                            <!-- Row 1 -->
                            <div class="flex items-center border-b border-slate-100 h-14 bg-white hover:bg-slate-50 transition-all">
                                <div class="w-16 px-4 text-[12px] text-slate-500 font-medium">1</div>
                                <div class="flex-1 px-4 relative group">
                                    <input type="text" class="w-full bg-transparent outline-none text-[13px] text-slate-700 placeholder-transparent focus:placeholder-slate-300 transition-all" title="Item / Account">
                                    <svg class="w-4 h-4 text-slate-300 absolute right-4 top-1 pointer-events-none group-hover:text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                                <div class="w-48 px-4 flex items-center gap-2"></div>
                                <div class="w-24 px-4">
                                    <input type="text" class="w-full text-center bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Quantity">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Rate">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Amount" readonly>
                                </div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                            <!-- Row 2 -->
                            <div class="flex items-center border-b border-slate-100 h-14 bg-white hover:bg-slate-50 transition-all">
                                <div class="w-16 px-4 text-[12px] text-slate-500 font-medium">2</div>
                                <div class="flex-1 px-4 relative group">
                                    <input type="text" class="w-full bg-transparent outline-none text-[13px] text-slate-700 placeholder-transparent focus:placeholder-slate-300 transition-all" title="Item / Account">
                                    <svg class="w-4 h-4 text-slate-300 absolute right-4 top-1 pointer-events-none group-hover:text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                                <div class="w-48 px-4 flex items-center gap-2"></div>
                                <div class="w-24 px-4">
                                    <input type="text" class="w-full text-center bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Quantity">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Rate">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Amount" readonly>
                                </div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                            <!-- Row 3 -->
                            <div class="flex items-center border-b border-slate-100 h-14 bg-white hover:bg-slate-50 transition-all">
                                <div class="w-16 px-4 text-[12px] text-slate-500 font-medium">3</div>
                                <div class="flex-1 px-4 relative group">
                                    <input type="text" class="w-full bg-transparent outline-none text-[13px] text-slate-700 placeholder-transparent focus:placeholder-slate-300 transition-all" title="Item / Account">
                                    <svg class="w-4 h-4 text-slate-300 absolute right-4 top-1 pointer-events-none group-hover:text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                                <div class="w-48 px-4 flex items-center gap-2"></div>
                                <div class="w-24 px-4">
                                    <input type="text" class="w-full text-center bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Quantity">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Rate">
                                </div>
                                <div class="w-32 px-4">
                                    <input type="text" class="w-full text-right bg-transparent outline-none text-[13px] text-slate-700 font-medium" title="Amount" readonly>
                                </div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                        </div>

                        <!-- Table Footer / Summary -->
                        <div class="bg-slate-50 border-t border-slate-200">
                            <div class="flex items-center h-10 border-b border-slate-200/60">
                                <div class="flex-1 text-right px-4 text-[12px] text-slate-500">Sub Total</div>
                                <div class="w-32 px-4 text-right text-[13px] text-slate-800 font-medium"></div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                            <div class="flex items-center h-10 border-b border-slate-200/60">
                                <div class="flex-1 text-right px-4 text-[12px] text-slate-500">Round Off</div>
                                <div class="w-32 px-4 text-right text-[13px] text-slate-300 font-medium">0.00</div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                            <div class="flex items-center h-12 bg-white">
                                <div class="flex-1 text-right px-4 text-[13px] font-black text-slate-800">Total</div>
                                <div class="w-32 px-4 text-right text-[14px] font-black text-slate-800">₹0.00</div>
                                <div class="w-12 border-l border-transparent"></div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Bottom Fields Section -->
                    <div class="mt-6 flex items-start gap-12">
                        <div class="flex-1 max-w-sm">
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 block">Notes</label>
                            <textarea class="w-full h-20 bg-white border border-slate-200 rounded px-3 py-2 text-[13px] text-slate-700 outline-none focus:border-[var(--accent)] resize-none" title="Notes"></textarea>
                            
                            <button class="flex items-center gap-1.5 text-[12px] font-bold text-slate-600 hover:text-[var(--accent)] mt-4" title="Attach File">
                                <svg class="w-4 h-4 rotate-45" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"/></svg>
                                Attach File
                            </button>
                        </div>
                        <div class="w-64 mt-10">
                            <label class="text-[12px] font-bold text-slate-500 mb-1.5 block">Project</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none focus:border-[var(--accent)] appearance-none" title="Select Project">
                                    <option>Select Project</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</div>
<!-- End New Cash Purchase Modal -->
"""

content = content.replace('<!-- End New Purchase Modal -->', '<!-- End New Purchase Modal -->\n' + cash_modal_html)

# 3. Add Javascript functions
js_logic = """
    // Cash Purchase Modal specific functions
    function openNewCashPurchaseModal() {
        document.getElementById('newCashPurchaseModal').classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    function closeNewCashPurchaseModal() {
        document.getElementById('newCashPurchaseModal').classList.add('hidden');
        document.body.style.overflow = 'auto';
    }

    function addPbCashPaymentRow() {
        const container = document.getElementById('pbCashPaymentRowsContainer');
        const rowHTML = `
            <div class="flex items-end gap-6 payment-row animate-in fade-in slide-in-from-top-4 duration-300">
                <div class="w-64">
                    <div class="relative">
                        <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none" title="Paid from Account">
                            <option>Cash</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
                <div class="w-96">
                    <div class="flex items-center h-10 border border-slate-200 rounded bg-white">
                        <div class="relative border-r border-slate-200 h-full w-24">
                            <select class="w-full h-full bg-transparent px-3 text-[13px] text-slate-500 outline-none appearance-none" title="Reference Type">
                                <option>Cash</option>
                            </select>
                            <svg class="w-3 h-3 text-slate-400 absolute right-2 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </div>
                        <input type="text" class="flex-1 h-full px-3 text-[13px] bg-transparent outline-none" title="Reference Number">
                    </div>
                </div>
                <button type="button" onclick="this.closest('.payment-row').remove()" class="w-10 h-10 bg-red-50 hover:bg-red-100 text-red-500 rounded flex items-center justify-center transition-all" title="Remove Row">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', rowHTML);
    }
"""

if '// POS specific functions' in content:
    content = content.replace('// POS specific functions', js_logic + '\n    // POS specific functions')
else:
    # If POS was removed cleanly, find switchPbView or something to append JS
    content = content.replace('function switchPbView', js_logic + '\n    function switchPbView')

# Add popover ids to menus array to close on outside click
if "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu'];" in content:
    menus_old = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu'];"
    menus_new = "const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu', 'pbEnterItemMenu', 'pbQuickSettingsMenu', 'pbCashBillDateSettings', 'pbCashTableSettings'];"
    content = content.replace(menus_old, menus_new)
else:
    print("Could not find menus array to update")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added New Cash Purchase modal")
