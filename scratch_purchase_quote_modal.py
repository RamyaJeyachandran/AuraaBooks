import os

modal_html = """
    <!-- New Purchase Quote Modal -->
    <div id="newPurchaseQuoteModal" class="hidden fixed inset-0 z-[1000] flex items-center justify-center">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" onclick="toggleModal('newPurchaseQuoteModal')"></div>
        
        <!-- Modal Content -->
        <div class="relative bg-white w-[95vw] h-[90vh] rounded-xl shadow-2xl flex flex-col overflow-hidden">
            
            <!-- Modal Header (Primary Background) -->
            <div class="flex items-center justify-between px-6 py-4 bg-[var(--accent)] text-white border-b border-white/20">
                <div>
                    <h2 class="text-[18px] font-black tracking-tight">New Purchase Quote</h2>
                    <div class="flex items-center gap-1 text-[12px] opacity-90 font-medium">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                        Main Branch
                    </div>
                </div>
                
                <div class="flex items-center gap-3">
                    <!-- Cancel Button -->
                    <button type="button" onclick="toggleModal('newPurchaseQuoteModal')" class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all">Cancel</button>
                    
                    <!-- Save Split Button (Primary Color) -->
                    <div class="relative group/saveModal">
                        <div class="flex items-center bg-[var(--accent)] text-white rounded overflow-hidden h-[36px] shadow-md border border-white/20">
                            <button type="button" class="px-6 h-full text-[13px] font-bold hover:brightness-110 transition-all border-r border-white/20">
                                Save
                            </button>
                            <button onclick="toggleActionMenu(event, 'saveModalMenu')" class="px-2 h-full hover:brightness-110 transition-all flex items-center justify-center">
                                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                            </button>
                        </div>
                        <div id="saveModalMenu" class="hidden absolute top-full right-0 mt-1 w-48 bg-white rounded shadow-xl border border-slate-200 py-1 z-[600]">
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save & New</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft & New</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save & Print</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save</button>
                        </div>
                    </div>

                    <!-- Close X Button (Red) -->
                    <button type="button" onclick="toggleModal('newPurchaseQuoteModal')" class="w-8 h-8 flex items-center justify-center bg-red-500 text-white hover:bg-red-600 rounded transition-all ml-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg>
                    </button>
                </div>
            </div>

            <!-- Modal Body (Scrollable) -->
            <div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar">
                
                <!-- Top Inputs -->
                <div class="grid grid-cols-4 gap-6 mb-8">
                    <div>
                        <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative">
                            Purchase Quote No
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tooltip:block absolute bottom-full left-0 mb-1 w-48 bg-white border border-slate-200 shadow-xl p-3 text-[11px] font-normal text-slate-600 rounded z-10">Unique identifier for this quote.</div>
                        </label>
                        <div class="text-[20px] font-black text-slate-800">PQ1</div>
                    </div>
                    <div>
                        <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative">
                            Purchase Quote Date
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tooltip:block absolute bottom-full left-0 mb-1 w-48 bg-white border border-slate-200 shadow-xl p-3 text-[11px] font-normal text-slate-600 rounded z-10">Date the quote was issued.</div>
                        </label>
                        <div class="relative">
                            <input type="text" value="23/05/2026" class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                        </div>
                    </div>
                    <div>
                        <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative">
                            Valid Till
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tooltip:block absolute bottom-full left-0 mb-1 w-48 bg-white border border-slate-200 shadow-xl p-3 text-[11px] font-normal text-slate-600 rounded z-10">Date until which this quote is valid.</div>
                        </label>
                        <div class="flex border border-slate-200 rounded overflow-hidden">
                            <div class="flex items-center px-3 bg-slate-50 border-r border-slate-200 text-[12px] font-medium text-slate-600">
                                on Receipt <svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                            </div>
                            <div class="relative flex-1">
                                <input type="text" value="23/05/2026" class="w-full h-10 px-3 text-[13px] font-bold text-slate-700 focus:border-accent outline-none border-none">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-end gap-3 relative z-[400]">
                        <div class="flex-1">
                            <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative">
                                Reference #
                                <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            </label>
                            <input type="text" class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] focus:border-accent outline-none">
                        </div>
                        
                        <!-- Reference Settings Dropdown (Primary Background) -->
                        <div class="relative pb-2">
                            <button onclick="toggleActionMenu(event, 'refSettingsMenu')" class="text-slate-400 hover:text-slate-600 transition-all">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                            </button>
                            <!-- Updated as requested: Settings Dropdown background color is primary color -->
                            <div id="refSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-72 bg-[var(--accent)] rounded-lg shadow-2xl p-4 z-[600] border border-white/20 text-white">
                                <div class="absolute -top-1 right-2 w-3 h-3 bg-[var(--accent)] rotate-45 border-t border-l border-white/20"></div>
                                <div class="space-y-3 relative z-10">
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded border-white/40">
                                        <span class="text-[12px] font-medium">Show Reverse Charge</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded border-white/40">
                                        <span class="text-[12px] font-medium">Customs Duty Payable</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded border-white/40">
                                        <span class="text-[12px] font-medium">TCS Receivable</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded border-white/40">
                                        <span class="text-[12px] font-medium">Tax Round Off</span>
                                    </label>
                                    
                                    <div class="text-[12px] pt-1">
                                        Initial Focus <a href="#" class="text-blue-200 hover:underline">Date</a>
                                    </div>
                                    
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded border-white/40">
                                        <span class="text-[12px] font-medium">Ignore Auto Select if multiple Attributes</span>
                                    </label>
                                    
                                    <div class="pt-1">
                                        <a href="#" class="text-[12px] text-blue-200 hover:underline">Manage Custom Fields...</a>
                                    </div>
                                    
                                    <button class="mt-2 px-6 py-2 bg-white text-[var(--accent)] rounded font-bold text-[12px] hover:bg-slate-100 transition-all">Save</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Supplier Block -->
                <div class="grid grid-cols-4 gap-6 mb-8">
                    <div class="col-span-1">
                        <label class="flex items-center gap-1 text-[13px] font-bold text-[#b91c1c] mb-2 group/tooltip relative">
                            Supplier <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <span class="text-red-500 ml-1">*</span>
                        </label>
                        <div class="relative">
                            <input type="text" placeholder="Select Contact (F9)" class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-400 focus:border-accent outline-none">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                        </div>
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold text-slate-600 mb-2">Supplier Quotation No</label>
                        <input type="text" class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] focus:border-accent outline-none">
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold text-slate-600 mb-2">Supplier Quotation Date</label>
                        <div class="relative">
                            <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 border border-slate-200 rounded px-3 text-[13px] placeholder-slate-300 focus:border-accent outline-none">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                        </div>
                    </div>
                </div>

                <!-- Items Table (Background primary color in header) -->
                <div class="border border-slate-200 bg-white shadow-sm mb-6 pb-6 relative z-[300]">
                    <table class="w-full text-left border-collapse">
                        <!-- Table header background is primary color -->
                        <thead class="bg-[var(--accent)] text-white">
                            <tr>
                                <th class="px-4 py-3 text-[12px] font-bold w-12 border-b border-r border-white/20">S.No</th>
                                <th class="px-4 py-3 text-[12px] font-bold border-b border-r border-white/20 flex items-center justify-between">
                                    Item
                                    <div class="flex items-center gap-2">
                                        <input type="text" placeholder="Search..." class="h-6 w-32 px-2 text-[11px] rounded border-none text-slate-800 focus:outline-none">
                                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                                    </div>
                                </th>
                                <th class="px-4 py-3 text-[12px] font-bold w-24 border-b border-r border-white/20 text-center">Qty</th>
                                <th class="px-4 py-3 text-[12px] font-bold w-24 border-b border-r border-white/20 text-center">Unit</th>
                                <th class="px-4 py-3 text-[12px] font-bold w-32 border-b border-r border-white/20 text-right">Rate ₹</th>
                                <th class="px-4 py-3 text-[12px] font-bold w-32 border-b border-r border-white/20 text-right">Amount</th>
                                <th class="px-3 py-3 w-12 border-b border-white/20 text-center relative z-[400]">
                                    <!-- Table Settings Dropdown (White bg, primary border) -->
                                    <button onclick="toggleActionMenu(event, 'tableSettingsMenu')" class="text-white hover:text-slate-200 transition-all">
                                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                    </button>
                                    <div id="tableSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded-lg shadow-2xl p-4 z-[600] border-2 border-[var(--accent)] text-slate-800 text-left">
                                        <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t-2 border-l-2 border-[var(--accent)] rotate-45"></div>
                                        <div class="space-y-2 relative z-10 max-h-[300px] overflow-y-auto custom-scrollbar pr-2">
                                            <label class="flex items-center justify-between cursor-pointer">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded"><span class="text-[12px]">Description (Below Item)</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded"><span class="text-[12px]">SKU</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded"><span class="text-[12px]">HSN / SAC</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                <div class="flex items-center gap-2"><input type="checkbox" checked class="rounded"><span class="text-[12px]">Unit</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            
                                            <div class="pt-2">
                                                <a href="#" class="text-[12px] text-blue-600 hover:underline">Manage Custom Fields...</a>
                                            </div>
                                            <label class="flex items-center gap-2 cursor-pointer mt-1 mb-2">
                                                <input type="checkbox" class="rounded">
                                                <span class="text-[12px]">Item Details in Popup</span>
                                            </label>
                                            
                                            <div class="flex items-center gap-2 mt-3">
                                                <button class="px-4 py-1.5 bg-[var(--accent)] text-white rounded font-bold text-[12px] hover:brightness-110 transition-all">Save</button>
                                                <button class="px-4 py-1.5 bg-slate-200 text-slate-700 rounded font-bold text-[12px] hover:bg-slate-300 transition-all">Cancel</button>
                                            </div>
                                        </div>
                                    </div>
                                </th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="px-4 py-3 text-[13px] border-r border-slate-100 text-center">1</td>
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
                            <tr>
                                <td class="px-4 py-3 text-[13px] border-r border-slate-100 text-center">2</td>
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
                            <tr>
                                <td class="px-4 py-3 text-[13px] border-r border-slate-100 text-center">3</td>
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
                    </table>
                    
                    <!-- Subtotals -->
                    <div class="flex flex-col items-end pt-4 pr-16 space-y-3">
                        <div class="flex items-center w-64 justify-between">
                            <span class="text-[12px] font-medium text-slate-600">Sub Total</span>
                            <span class="text-[12px] font-medium text-slate-600"></span>
                        </div>
                        <div class="flex items-center w-64 justify-between">
                            <span class="text-[12px] font-medium text-slate-600">Round Off</span>
                            <span class="text-[12px] font-medium text-slate-300">0.00</span>
                        </div>
                        <div class="flex items-center w-64 justify-between pt-3 border-t border-slate-200">
                            <span class="text-[13px] font-bold text-slate-800">Total</span>
                            <span class="text-[14px] font-black text-slate-800">₹0.00</span>
                        </div>
                    </div>
                </div>

                <!-- Bottom Section -->
                <div class="grid grid-cols-2 gap-8 pb-10">
                    <div>
                        <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative w-max">
                            Notes
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tooltip:block absolute bottom-full left-0 mb-1 w-64 bg-white border border-slate-200 shadow-xl p-3 text-[11px] font-normal text-slate-600 rounded z-10">
                                Statements which provides additional information on the quote generated and are to be printed at the end of the quote
                            </div>
                        </label>
                        <textarea class="w-full h-24 border border-slate-200 rounded p-3 text-[13px] focus:border-accent outline-none resize-none mb-2"></textarea>
                        
                        <div class="flex items-center gap-2 text-[14px] text-slate-600 cursor-pointer hover:text-slate-800 transition-all font-medium">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21.44 11.05l-9.19 9.19a6 6 0 01-8.49-8.49l9.19-9.19a4 4 0 015.66 5.66l-9.2 9.19a2 2 0 01-2.83-2.83l8.49-8.48"/></svg>
                            Attach File
                        </div>
                    </div>
                    <div>
                        <label class="flex items-center gap-1 text-[13px] font-bold text-slate-700 mb-2 group/tooltip relative w-max">
                            Terms & Conditions
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            <div class="hidden group-hover/tooltip:block absolute bottom-full left-0 mb-1 w-64 bg-white border border-slate-200 shadow-xl p-3 text-[11px] font-normal text-slate-600 rounded z-10">
                                Standard statements that form an integral part of an agreement or contract
                            </div>
                        </label>
                        <textarea class="w-full h-24 border border-slate-200 rounded p-3 text-[13px] focus:border-accent outline-none resize-none"></textarea>
                    </div>
                </div>

            </div>
        </div>
    </div>
"""

file_path = r'd:\AuraaZenAIProject\abproject\templates\purchase_quotes.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the New Purchase Quote button open the modal
button_target = 'class="px-8 py-3.5 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest"'
if button_target in content:
    content = content.replace(button_target, f'onclick="toggleModal(\'newPurchaseQuoteModal\')" {button_target}')

# Append the modal script and HTML before the endblock
script_target = """    // Close menus when clicking outside
    document.addEventListener('click', function(event) {"""
    
script_replacement = """    function toggleModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.toggle('hidden');
            if(!modal.classList.contains('hidden')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = 'auto';
            }
        }
    }

    // Close menus when clicking outside
    document.addEventListener('click', function(event) {"""

if script_target in content:
    content = content.replace(script_target, script_replacement)

# Also ensure saveModalMenu, refSettingsMenu, tableSettingsMenu are handled by the click-away listener
menu_list_target = "const menus = ['exportMenu', 'filterMenu', 'settingsMenu'];"
menu_list_replacement = "const menus = ['exportMenu', 'filterMenu', 'settingsMenu', 'saveModalMenu', 'refSettingsMenu', 'tableSettingsMenu'];"

if menu_list_target in content:
    content = content.replace(menu_list_target, menu_list_replacement)


# Finally append the HTML
if "<!-- New Purchase Quote Modal -->" not in content:
    # insert before <script> block or before {% endblock %}
    content = content.replace("<script>", modal_html + "\n<script>")
    
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal added successfully")
