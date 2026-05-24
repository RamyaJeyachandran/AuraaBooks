import os

html_file = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the entire modal HTML with the updated styles
# Let's extract the modal HTML from the file and replace it.

start_marker = "<!-- New Purchase Modal -->"
end_marker = "{% endblock %}"

if start_marker in content and end_marker in content:
    parts = content.split(start_marker)
    pre_modal = parts[0]
    modal_and_after = parts[1].split(end_marker)
    post_modal = end_marker + (modal_and_after[1] if len(modal_and_after) > 1 else "")
    
    # We will supply the entire new modal HTML
    new_modal_html = """
<div id="newPurchaseModal" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-[1000] hidden items-center justify-center p-4" onclick="closeNewPurchaseModal(event)">
    <div class="relative bg-white w-full max-w-[1400px] max-h-[95vh] rounded-xl shadow-2xl flex flex-col overflow-hidden" onclick="event.stopPropagation()">
        
        <!-- Header -->
        <div class="flex items-center justify-between px-6 py-4 bg-[var(--accent)] text-white border-b border-white/20">
            <div class="flex items-center gap-4">
                <div>
                    <h2 class="text-[20px] font-black flex items-center gap-2 cursor-pointer group">
                        New Purchase 
                        <svg class="w-4 h-4 text-white/70 group-hover:text-white transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </h2>
                    <div class="flex items-center gap-1 text-[13px] font-bold text-white/80 mt-1">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                        Main Branch
                    </div>
                </div>
                
                <!-- View Toggle Split Button -->
                <div class="relative ml-8">
                    <div class="flex items-center rounded-lg overflow-hidden border border-white/20 shadow-sm h-9">
                        <button class="px-3 h-full bg-white/10 hover:bg-white/20 text-white transition-all border-r border-white/20 flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 9 5.36C5.79 7.5 3.39 10.71 2.5 14.5L5.5 15.5L8.5 18.5L9.5 21.5C13.29 20.61 16.5 18.21 18.64 15C23.73 7.34 21.61 2.39 21.61 2.39ZM14.5 11.5C13.4 11.5 12.5 10.6 12.5 9.5C12.5 8.4 13.4 7.5 14.5 7.5C15.6 7.5 16.5 8.4 16.5 9.5C16.5 10.6 15.6 11.5 14.5 11.5Z"/></svg>
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbViewMenu')" class="px-2 h-full bg-white/10 hover:bg-white/20 text-white transition-all flex items-center justify-center">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </button>
                    </div>
                    <!-- View Dropdown -->
                    <div id="pbViewMenu" class="hidden absolute top-full left-0 mt-1 w-40 bg-white rounded-lg shadow-xl border border-slate-100 py-1 z-[600] text-slate-800">
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
                <!-- Save Split Button (White with Primary Border) -->
                <div class="relative group/saveModal">
                    <div class="flex items-center bg-white text-[var(--accent)] rounded overflow-hidden h-[36px] shadow-sm border border-[var(--accent)]">
                        <button class="px-6 h-full text-[13px] font-bold hover:bg-slate-50 transition-all border-r border-[var(--accent)]">
                            Save
                        </button>
                        <button onclick="toggleModalMenu(event, 'pbSaveMenu')" class="px-2 h-full hover:bg-slate-50 transition-all flex items-center justify-center">
                            <svg class="w-4 h-4 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                        </button>
                    </div>
                    <!-- Save Dropdown -->
                    <div id="pbSaveMenu" class="hidden absolute top-full right-0 mt-1 w-48 bg-white rounded shadow-xl border border-slate-200 py-1 z-[600] text-slate-800">
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save & New</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save as Draft</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save as Draft & New</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save & Print</button>
                        <button class="w-full text-left px-4 py-2 text-[12px] font-bold text-slate-600 hover:bg-slate-50">Save</button>
                    </div>
                </div>
                
                <!-- Cancel Button -->
                <button type="button" onclick="closeNewPurchaseModal(event)" class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all ml-1">Cancel</button>
                
                <!-- Close X Button -->
                <button type="button" onclick="closeNewPurchaseModal(event)" class="w-8 h-8 flex items-center justify-center bg-red-500 text-white hover:bg-red-600 rounded transition-all ml-2">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg>
                </button>
            </div>
        </div>

        <!-- Body (Scrollable) -->
        <div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar">
            
            <!-- Top Form Area -->
            <div class="flex items-start gap-4 mb-6">
                <div class="space-y-1 w-1/5">
                    <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Purchase Bill No <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <input type="text" value="1" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                </div>
                <div class="space-y-1 w-1/5">
                    <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Bill Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <div class="relative">
                        <input type="text" value="24/05/2026" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19a2 2 0 002 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
                    </div>
                </div>
                <div class="space-y-1 w-1/4">
                    <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Due Date <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <div class="flex items-center">
                        <div class="relative w-1/2">
                            <select class="w-full h-10 bg-slate-50 border border-slate-100 border-r-0 rounded-l-xl px-4 text-[12px] font-bold text-slate-600 outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                                <option>on Receipt</option>
                            </select>
                            <svg class="w-3 h-3 text-slate-400 absolute right-2 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </div>
                        <div class="relative w-1/2">
                            <input type="text" value="24/05/2026" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-r-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19a2 2 0 002 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/></svg>
                        </div>
                    </div>
                </div>
                <div class="space-y-1 w-1/5 relative">
                    <label class="text-[10px] font-black text-slate-400 uppercase tracking-widest flex items-center gap-1 mb-2">Purchase Order # <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></label>
                    <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    
                    <!-- Settings Gear next to PO -->
                    <button onclick="toggleModalMenu(event, 'pbPoSettingsMenu')" class="absolute top-8 -right-8 w-6 h-6 flex items-center justify-center text-slate-400 hover:text-[var(--accent)] transition-colors">
                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                    </button>
                    <!-- PO Settings Menu -->
                    <div id="pbPoSettingsMenu" class="hidden absolute top-12 -right-4 w-64 bg-white rounded-lg shadow-xl border border-slate-100 p-4 z-[600]">
                        <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                        <div class="space-y-3">
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-700">Show Reverse Charge</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-700">Invoice Type</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-700">Customs Duty Payable</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-700">TCS Receivable</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer opacity-50">
                                <input type="checkbox" disabled class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-500">Tax Round Off</span>
                            </label>
                            
                            <div class="text-[12px] font-medium text-slate-700 pt-2">Initial Focus <span class="text-blue-500 hover:underline cursor-pointer">Date</span></div>
                            
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)]">
                                <span class="text-[12px] font-medium text-slate-700">Ignore Auto Select if multiple Attributes</span>
                            </label>
                            <button class="text-[12px] text-blue-500 text-left hover:underline w-full">Manage Custom Fields...</button>
                            <button class="mt-2 px-6 py-2 bg-white text-[var(--accent)] border border-[var(--accent)] rounded font-bold text-[12px] hover:bg-slate-50">Save</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Supplier Section -->
            <div class="mb-8 w-1/3">
                <label class="flex items-center gap-1 text-[10px] font-black text-red-500 uppercase tracking-widest mb-2 group/tooltip relative">
                    Supplier / Vendor <svg class="w-3.5 h-3.5 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> <span class="text-red-500">*</span>
                </label>
                <div class="relative mb-4">
                    <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                        <option>Select Contact (F9)</option>
                    </select>
                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                </div>
                <div class="flex items-center gap-4">
                    <div class="space-y-1 flex-1">
                        <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice No</label>
                        <input type="text" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                    </div>
                    <div class="space-y-1 flex-1">
                        <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Supplier Invoice Date</label>
                        <div class="relative">
                            <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Items Table (Background primary color in header) -->
            <div class="border border-slate-200 bg-white shadow-sm mb-6 pb-6 relative z-[300] rounded-2xl overflow-visible">
                <table class="w-full text-left border-collapse min-w-[800px]">
                    <thead class="bg-[var(--accent)] text-white">
                        <tr>
                            <th class="px-4 py-3 text-[12px] font-bold w-12 border-b border-r border-white/20 text-center">S.No</th>
                            <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-white/20 flex items-center justify-between">
                                Item/Account
                                <div class="flex items-center gap-2">
                                    <input type="text" placeholder="Search.." class="h-6 w-32 px-2 text-[11px] rounded border-none text-slate-800 focus:outline-none hidden">
                                </div>
                            </th>
                            <th class="px-4 py-3 text-[12px] font-bold w-24 border-b border-r border-white/20 text-center">Qty</th>
                            <th class="px-4 py-3 text-[12px] font-bold w-24 border-b border-r border-white/20 text-center">Unit</th>
                            <th class="px-4 py-3 text-[12px] font-bold w-32 border-b border-r border-white/20 text-right">Rate ₹</th>
                            <th class="px-4 py-3 text-[12px] font-bold w-32 border-b border-r border-white/20 text-right">Amount</th>
                            <th class="px-3 py-3 w-12 border-b border-white/20 text-center relative z-[400]">
                                <button onclick="toggleModalMenu(event, 'pbTableSettingsMenu')" class="text-white hover:text-slate-200 transition-all">
                                    <svg class="w-4 h-4 mx-auto" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                </button>
                                <!-- Table Settings Menu -->
                                <div id="pbTableSettingsMenu" class="hidden absolute top-10 right-0 w-64 bg-white rounded-lg shadow-2xl p-4 z-[600] border-2 border-[var(--accent)] text-slate-800 text-left">
                                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t-2 border-l-2 border-[var(--accent)] rotate-45"></div>
                                    <div class="space-y-2.5 relative z-10 max-h-[300px] overflow-y-auto custom-scrollbar pr-2">
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">Description (Below Item)</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">SKU</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">HSN / SAC</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">Account</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" checked class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">Unit</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">Net Rate</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        <label class="flex justify-between items-center cursor-pointer">
                                            <div class="flex items-center gap-2"><input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded"><span class="text-[12px] font-medium text-slate-700">MRP</span></div>
                                            <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                        </label>
                                        
                                        <button class="text-[12px] text-blue-600 hover:underline block w-full text-left mt-2">Manage Custom Fields...</button>
                                        <label class="flex items-center gap-2 cursor-pointer mt-1 mb-2">
                                            <input type="checkbox" class="w-3.5 h-3.5 accent-[var(--accent)] rounded">
                                            <span class="text-[12px] font-medium text-slate-700">Item Details in Popup</span>
                                        </label>
                                        
                                        <div class="flex gap-2 mt-3 pt-3 border-t border-slate-100">
                                            <button class="px-4 py-1.5 bg-white text-[var(--accent)] border border-[var(--accent)] rounded text-[12px] font-bold hover:bg-slate-50 transition-all">Save</button>
                                            <button class="px-4 py-1.5 bg-slate-100 text-slate-700 rounded text-[12px] font-bold hover:bg-slate-200 transition-all">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <!-- Row 1 -->
                        <tr>
                            <td class="px-4 py-3 text-[13px] font-medium text-center border-r border-slate-100">1</td>
                            <td class="p-0 border-r border-slate-100 relative">
                                <div class="flex items-center justify-end px-3">
                                    <svg class="w-4 h-4 text-slate-300 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                                </div>
                            </td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0"></td>
                        </tr>
                        <!-- Row 2 -->
                        <tr>
                            <td class="px-4 py-3 text-[13px] font-medium text-center border-r border-slate-100">2</td>
                            <td class="p-0 border-r border-slate-100 relative">
                                <div class="flex items-center justify-end px-3">
                                    <svg class="w-4 h-4 text-slate-300 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                                </div>
                            </td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0"></td>
                        </tr>
                        <!-- Row 3 -->
                        <tr>
                            <td class="px-4 py-3 text-[13px] font-medium text-center border-r border-slate-100">3</td>
                            <td class="p-0 border-r border-slate-100 relative">
                                <div class="flex items-center justify-end px-3">
                                    <svg class="w-4 h-4 text-slate-300 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                                </div>
                            </td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0 border-r border-slate-100"></td>
                            <td class="p-0"></td>
                        </tr>
                    </tbody>
                    <tfoot class="border-t border-slate-200 bg-slate-50/50">
                        <tr>
                            <td colspan="5" class="px-4 py-3 text-right text-[12px] font-black text-slate-500 tracking-wider uppercase">Sub Total</td>
                            <td class="px-4 py-3 text-right text-[12px] font-medium text-slate-400"></td>
                            <td class=""></td>
                        </tr>
                        <tr>
                            <td colspan="5" class="px-4 py-3 text-right text-[12px] font-black text-slate-500 tracking-wider uppercase border-t border-slate-100">Round Off</td>
                            <td class="px-4 py-3 text-right text-[12px] font-bold text-slate-400 border-t border-slate-100">0.00</td>
                            <td class="border-t border-slate-100"></td>
                        </tr>
                        <tr>
                            <td colspan="5" class="px-4 py-4 text-right text-[14px] font-black text-slate-800 uppercase tracking-widest border-t border-slate-100">Total</td>
                            <td class="px-4 py-4 text-right text-[16px] font-black text-[var(--accent)] border-t border-slate-100">₹0.00</td>
                            <td class="border-t border-slate-100"></td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <!-- Bottom Section -->
            <div class="flex gap-8 mb-4">
                <div class="w-1/3">
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Notes</label>
                    <textarea class="w-full h-16 bg-slate-50 border border-slate-100 rounded-xl px-4 py-3 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner resize-y"></textarea>
                </div>
                <div class="w-1/4">
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Project</label>
                    <div class="relative">
                        <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                            <option>Select Project</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
                <div class="w-1/4">
                    <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">Referred By</label>
                    <div class="relative">
                        <select class="w-full h-10 bg-slate-50 border border-slate-100 rounded-xl px-4 text-[13px] font-bold outline-none focus:bg-white focus:border-[var(--accent)] shadow-inner appearance-none">
                            <option>Select Referred By</option>
                        </select>
                        <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </div>
                </div>
            </div>
            
            <div class="flex items-center gap-1.5 cursor-pointer text-slate-500 hover:text-[var(--accent)] transition-colors w-max group">
                <svg class="w-4 h-4 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 24 24"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5a2.5 2.5 0 015 0v10.5c0 .55-.45 1-1 1s-1-.45-1-1V6H10v9.5a2.5 2.5 0 005 0V5c0-2.21-1.79-4-4-4S7 2.79 7 5v12.5c0 3.04 2.46 5.5 5.5 5.5s5.5-2.46 5.5-5.5V6h-1.5z"/></svg>
                <span class="text-[12px] font-bold">Attach File</span>
            </div>

        </div>
    </div>
</div>
<!-- End New Purchase Modal -->
"""
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(pre_modal + new_modal_html + post_modal)
    print("Modal successfully completely overhauled.")
else:
    print("Could not find start or end markers for modal.")
