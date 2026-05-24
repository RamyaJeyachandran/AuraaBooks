import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure we don't append it multiple times
if "id=\"newPurchaseModal\"" in content:
    print("Modal already exists.")
else:
    modal_html = """
<!-- New Purchase Modal -->
<div id="newPurchaseModal" class="fixed inset-0 bg-black/50 z-[1000] hidden items-center justify-center p-4" onclick="closeNewPurchaseModal(event)">
    <div class="bg-white rounded-xl shadow-2xl w-full max-w-[1400px] max-h-[95vh] flex flex-col overflow-hidden relative" onclick="event.stopPropagation()">
        
        <!-- Header -->
        <div class="flex items-center justify-between px-6 py-4 border-b border-slate-200 bg-slate-50/50">
            <div class="flex items-center gap-4">
                <div>
                    <h2 class="text-[20px] font-black text-slate-800 flex items-center gap-2 cursor-pointer group">
                        New Purchase 
                        <svg class="w-4 h-4 text-slate-400 group-hover:text-slate-600 transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </h2>
                    <div class="flex items-center gap-1 text-[13px] font-bold text-slate-500 mt-1">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                        Main Branch
                    </div>
                </div>
                
                <!-- View Toggle Split Button -->
                <div class="relative ml-8">
                    <div class="flex items-center rounded-lg overflow-hidden border border-slate-200 shadow-sm h-9">
                        <button class="px-3 h-full bg-slate-100 hover:bg-slate-200 text-slate-600 transition-all border-r border-slate-200 flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbViewMenu')" class="px-2 h-full bg-slate-100 hover:bg-slate-200 text-slate-600 transition-all flex items-center justify-center">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </button>
                    </div>
                    <!-- View Dropdown -->
                    <div id="pbViewMenu" class="hidden absolute top-full left-0 mt-1 w-40 bg-white rounded-lg shadow-xl border border-slate-100 py-1 z-[600]">
                        <button class="w-full text-left px-4 py-2.5 text-[13px] font-bold bg-[var(--accent)] text-white flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg>
                            Normal View
                        </button>
                        <button class="w-full text-left px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:bg-slate-50 flex items-center gap-2">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                            Quick View
                        </button>
                    </div>
                </div>
            </div>
            
            <div class="flex items-center gap-2">
                <!-- Save Split Button -->
                <div class="relative">
                    <div class="flex items-center rounded-lg overflow-hidden shadow-sm shadow-[var(--accent)]/20 h-9">
                        <button class="px-5 h-full bg-[var(--accent)] text-white text-[13px] font-bold hover:brightness-110 transition-all border-r border-white/20">
                            Save
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbSaveMenu')" class="px-2 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all flex items-center justify-center">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </button>
                    </div>
                    <!-- Save Dropdown -->
                    <div id="pbSaveMenu" class="hidden absolute top-full right-0 mt-1 w-48 bg-white rounded-lg shadow-xl border border-slate-100 py-1 z-[600]">
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save & New</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save as Draft</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save as Draft & New</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save & Print</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save</button>
                    </div>
                </div>
                <button type="button" onclick="closeNewPurchaseModal(event)" class="px-5 h-9 bg-slate-200 text-slate-700 rounded-lg text-[13px] font-bold hover:bg-slate-300 transition-all">Cancel</button>
            </div>
        </div>

        <!-- Body (Scrollable) -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-6">
            
            <!-- Top Form Area -->
            <div class="flex items-start gap-4 mb-6">
                <div class="space-y-1 w-1/5">
                    <label class="text-[12px] font-bold text-slate-800 flex items-center gap-1">Purchase Bill No <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <input type="text" value="1" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-800 outline-none focus:border-[var(--accent)]">
                </div>
                <div class="space-y-1 w-1/5">
                    <label class="text-[12px] font-bold text-slate-800 flex items-center gap-1">Bill Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <div class="relative">
                        <input type="text" value="24/05/2026" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-800 outline-none focus:border-[var(--accent)]">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19a2 2 0 002 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
                    </div>
                </div>
                <div class="space-y-1 w-1/4">
                    <label class="text-[12px] font-bold text-slate-800 flex items-center gap-1">Due Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <div class="flex items-center">
                        <div class="relative w-1/2">
                            <select class="w-full h-10 bg-white border border-slate-200 border-r-0 rounded-l px-3 text-[12px] font-medium text-slate-600 outline-none appearance-none">
                                <option>on Receipt</option>
                            </select>
                            <svg class="w-3 h-3 text-slate-400 absolute right-2 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </div>
                        <div class="relative w-1/2">
                            <input type="text" value="24/05/2026" class="w-full h-10 bg-white border border-slate-200 rounded-r px-3 pr-8 text-[13px] font-bold text-slate-800 outline-none focus:border-[var(--accent)]">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19a2 2 0 002 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
                        </div>
                    </div>
                </div>
                <div class="space-y-1 w-1/5 relative">
                    <label class="text-[12px] font-bold text-slate-800 flex items-center gap-1">Purchase Order # <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <input type="text" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-800 outline-none focus:border-[var(--accent)]">
                    
                    <!-- Settings Gear next to PO -->
                    <button onclick="toggleModalMenu(event, 'pbPoSettingsMenu')" class="absolute top-8 -right-8 w-6 h-6 flex items-center justify-center text-slate-500 hover:text-slate-700 transition-colors">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                    </button>
                    <!-- PO Settings Menu -->
                    <div id="pbPoSettingsMenu" class="hidden absolute top-12 -right-4 w-64 bg-white rounded-lg shadow-xl border border-slate-100 p-4 z-[600]">
                        <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        <div class="space-y-3">
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-700">Show Reverse Charge</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-700">Invoice Type</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-700">Customs Duty Payable</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-700">TCS Receivable</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer opacity-50">
                                <input type="checkbox" disabled class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-500">Tax Round Off</span>
                            </label>
                            
                            <div class="text-[12px] text-slate-700 pt-2">Initial Focus <span class="text-[var(--accent)] cursor-pointer">Date</span></div>
                            
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] text-slate-700">Ignore Auto Select if multiple Attributes</span>
                            </label>
                            <button class="text-[12px] text-[var(--accent)] text-left hover:underline w-full">Manage Custom Fields...</button>
                            <button class="mt-2 px-6 py-2 bg-[var(--accent)] text-white rounded text-[12px] font-bold hover:brightness-110">Save</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Supplier Section -->
            <div class="mb-6 w-1/3">
                <label class="text-[13px] font-bold text-[#b91c1c] flex items-center gap-1 mb-1">
                    Supplier / Vendor <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> <span class="text-[#b91c1c]">*</span>
                </label>
                <div class="relative mb-4">
                    <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-400 outline-none appearance-none">
                        <option>Select Contact (F9)</option>
                    </select>
                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                </div>
                <div class="flex items-center gap-4">
                    <div class="space-y-1 flex-1">
                        <label class="text-[11px] font-bold text-slate-700">Supplier Invoice No</label>
                        <input type="text" class="w-full h-9 bg-white border border-slate-200 rounded px-3 text-[13px] outline-none focus:border-[var(--accent)]">
                    </div>
                    <div class="space-y-1 flex-1">
                        <label class="text-[11px] font-bold text-slate-700">Supplier Invoice Date</label>
                        <div class="relative">
                            <input type="text" placeholder="DD/MM/YYYY" class="w-full h-9 bg-white border border-slate-200 rounded px-3 text-[12px] outline-none focus:border-[var(--accent)]">
                            <svg class="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-2.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19a2 2 0 002 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Items Table -->
            <div class="border border-slate-200 rounded mb-6 overflow-x-visible">
                <table class="w-full text-left border-collapse min-w-[800px]">
                    <thead class="bg-slate-50 border-b border-slate-200">
                        <tr>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 border-r border-slate-200 w-12 text-center">S.No</th>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 border-r border-slate-200 min-w-[300px]">Item/Account</th>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 border-r border-slate-200 w-24">Qty</th>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 border-r border-slate-200 w-24">Unit</th>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 border-r border-slate-200 w-32">Rate ₹</th>
                            <th class="px-4 py-3 text-[12px] font-bold text-slate-700 w-32">Amount</th>
                            <th class="px-2 py-3 text-[12px] font-bold text-slate-700 text-center w-12 relative border-l border-slate-200">
                                <button onclick="toggleModalMenu(event, 'pbTableSettingsMenu')" class="text-slate-500 hover:text-slate-700 transition-colors">
                                    <svg class="w-4 h-4 mx-auto" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                </button>
                                <!-- Table Settings Menu -->
                                <div id="pbTableSettingsMenu" class="hidden absolute top-10 right-0 w-64 bg-white rounded-lg shadow-2xl border border-slate-100 p-4 z-[600] text-left">
                                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                                    <div class="space-y-2.5 max-h-[300px] overflow-y-auto custom-scrollbar pr-2">
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">Description (Below Item)</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">SKU</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">HSN / SAC</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">Account</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" checked class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">Unit</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">Net Rate</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2">
                                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                                <span class="text-[12px] text-slate-700">MRP</span>
                                            </div>
                                            <svg class="w-3.5 h-3.5 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                        </label>
                                        
                                        <button class="text-[12px] text-[var(--accent)] hover:underline block w-full text-left mt-2">Manage Custom Fields...</button>
                                        <label class="flex items-center gap-2 cursor-pointer mt-1">
                                            <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                            <span class="text-[12px] text-slate-700">Item Details in Popup</span>
                                        </label>
                                        
                                        <div class="flex gap-2 mt-3 pt-2 border-t border-slate-100">
                                            <button class="px-4 py-1.5 bg-[var(--accent)] text-white rounded text-[12px] font-bold hover:brightness-110">Save</button>
                                            <button class="px-4 py-1.5 bg-slate-200 text-slate-700 rounded text-[12px] font-bold hover:bg-slate-300">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <!-- Row 1 -->
                        <tr class="group hover:bg-slate-50 transition-colors">
                            <td class="px-4 py-3 text-[12px] text-slate-600 text-center border-r border-slate-200">1</td>
                            <td class="px-4 py-3 border-r border-slate-200">
                                <div class="flex items-center gap-2 relative">
                                    <input type="text" placeholder="Search.." class="w-48 h-8 bg-white border border-slate-200 rounded px-2 text-[12px] outline-none focus:border-[var(--accent)]">
                                    <svg class="w-4 h-4 text-[var(--accent)] cursor-pointer" fill="currentColor" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
                                    <svg class="w-4 h-4 text-slate-400 absolute right-1 top-2 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                            </td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-2 py-3 border-l border-slate-200"></td>
                        </tr>
                        <!-- Row 2 -->
                        <tr class="group hover:bg-slate-50 transition-colors">
                            <td class="px-4 py-3 text-[12px] text-slate-600 text-center border-r border-slate-200">2</td>
                            <td class="px-4 py-3 border-r border-slate-200 relative">
                                <svg class="w-4 h-4 text-slate-300 absolute right-4 top-4 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-2 py-3 border-l border-slate-200"></td>
                        </tr>
                        <!-- Row 3 -->
                        <tr class="group hover:bg-slate-50 transition-colors">
                            <td class="px-4 py-3 text-[12px] text-slate-600 text-center border-r border-slate-200">3</td>
                            <td class="px-4 py-3 border-r border-slate-200 relative">
                                <svg class="w-4 h-4 text-slate-300 absolute right-4 top-4 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-4 py-3 border-r border-slate-200"></td>
                            <td class="px-2 py-3 border-l border-slate-200"></td>
                        </tr>
                    </tbody>
                    <tfoot class="border-t border-slate-200">
                        <tr>
                            <td colspan="5" class="px-4 py-2 text-right text-[12px] font-medium text-slate-600">Sub Total</td>
                            <td class="px-4 py-2 text-right text-[12px] font-medium text-slate-400"></td>
                            <td class="border-l border-slate-200"></td>
                        </tr>
                        <tr>
                            <td colspan="5" class="px-4 py-2 text-right text-[12px] font-medium text-slate-600 border-t border-slate-100">Round Off</td>
                            <td class="px-4 py-2 text-right text-[12px] font-medium text-slate-300 border-t border-slate-100">0.00</td>
                            <td class="border-l border-slate-200 border-t border-slate-100"></td>
                        </tr>
                        <tr>
                            <td colspan="5" class="px-4 py-2 text-right text-[13px] font-bold text-slate-800 border-t border-slate-100">Total</td>
                            <td class="px-4 py-2 text-right text-[13px] font-bold text-slate-800 border-t border-slate-100">₹0.00</td>
                            <td class="border-l border-slate-200 border-t border-slate-100"></td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <!-- Bottom Section -->
            <div class="flex gap-8 mb-4">
                <div class="w-1/3">
                    <label class="text-[12px] font-bold text-slate-700 block mb-1">Notes</label>
                    <textarea class="w-full h-16 bg-white border border-slate-200 rounded px-3 py-2 text-[12px] outline-none focus:border-[var(--accent)] resize-y"></textarea>
                </div>
                <div class="w-1/4">
                    <label class="text-[12px] font-bold text-slate-700 block mb-1">Project</label>
                    <div class="relative">
                        <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] text-slate-400 outline-none appearance-none">
                            <option>Select Project</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
                <div class="w-1/4">
                    <label class="text-[12px] font-bold text-slate-700 block mb-1">Referred By</label>
                    <div class="relative">
                        <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] text-slate-400 outline-none appearance-none">
                            <option>Select Referred By</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
            </div>
            
            <div class="flex items-center gap-1 cursor-pointer text-slate-600 hover:text-slate-800 transition-colors w-max">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5a2.5 2.5 0 015 0v10.5c0 .55-.45 1-1 1s-1-.45-1-1V6H10v9.5a2.5 2.5 0 005 0V5c0-2.21-1.79-4-4-4S7 2.79 7 5v12.5c0 3.04 2.46 5.5 5.5 5.5s5.5-2.46 5.5-5.5V6h-1.5z"/></svg>
                <span class="text-[12px] font-bold">Attach File</span>
            </div>

        </div>
    </div>
</div>
"""

    content += modal_html

    # Add button click handler to New Purchase button
    # The New Purchase button is `<button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">\n                New Purchase\n            </button>`
    # We'll use a regex to replace it
    import re
    content = re.sub(
        r'(<button class="[^"]*uppercase tracking-widest">\s*New Purchase\s*</button>)',
        lambda m: m.group(1).replace('<button ', '<button onclick="openNewPurchaseModal()" '),
        content,
        count=1
    )

    # Add JS functions if not present
    js_funcs = """
<script>
    function openNewPurchaseModal() {
        document.getElementById('newPurchaseModal').classList.remove('hidden');
        document.getElementById('newPurchaseModal').classList.add('flex');
    }
    
    function closeNewPurchaseModal(event) {
        if(event) event.stopPropagation();
        document.getElementById('newPurchaseModal').classList.add('hidden');
        document.getElementById('newPurchaseModal').classList.remove('flex');
    }
    
    function toggleModalMenu(event, menuId) {
        event.stopPropagation();
        const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu'];
        menus.forEach(id => {
            if (id !== menuId) {
                const el = document.getElementById(id);
                if (el && !el.classList.contains('hidden')) {
                    el.classList.add('hidden');
                }
            }
        });
        const menu = document.getElementById(menuId);
        if (menu) {
            menu.classList.toggle('hidden');
        }
    }

    document.addEventListener('click', function(event) {
        const menus = ['pbViewMenu', 'pbSaveMenu', 'pbPoSettingsMenu', 'pbTableSettingsMenu'];
        menus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.classList.contains('hidden') && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    });
</script>
"""
    if "openNewPurchaseModal" not in content:
        # insert before endblock
        content = content.replace("{% endblock %}", js_funcs + "\n{% endblock %}")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Added New Purchase Modal to purchase_bill.html")
