import os
import re

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Dropdown Buttons
# Export Form Menu: Export -> primary, Cancel -> dark gray
content = content.replace(
    '<button class="px-6 py-2 bg-[#10b981] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>',
    '<button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>'
)
content = content.replace(
    '<button class="px-6 py-2 bg-slate-200 text-slate-600 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Cancel</button>',
    '<button class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all">Cancel</button>'
)

# Filter Menu: Search -> primary, Clear -> dark gray
content = content.replace(
    '<button class="px-6 py-3 bg-[#10b981] text-white rounded-xl text-[13px] font-bold hover:brightness-110 transition-all">Search</button>',
    '<button class="px-6 py-3 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold hover:brightness-110 transition-all">Search</button>'
)
content = content.replace(
    '<button class="px-6 py-3 bg-slate-200 text-slate-600 rounded-xl text-[13px] font-bold hover:bg-slate-300 transition-all">Clear</button>',
    '<button class="px-6 py-3 bg-slate-700 text-white rounded-xl text-[13px] font-bold hover:bg-slate-800 transition-all">Clear</button>'
)

# Settings Menu: Apply -> primary
content = content.replace(
    '<button class="px-6 py-2 bg-slate-200 text-slate-700 rounded font-bold text-[13px] hover:bg-slate-300 transition-all">Apply</button>',
    '<button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Apply</button>'
)

# 2. Add toggleModal trigger to the "New Goods Receipt" button
new_button_html = '<button type="button" onclick="toggleModal(\'newGoodsReceiptModal\')" class="px-8 py-3.5 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">\n                New Goods Receipt\n            </button>'

# Use regex to find and replace the new goods receipt button
content = re.sub(
    r'<button type="button" class="px-8 py-3\.5 bg-\[var\(--accent\)\].*?New Goods Receipt\s*</button>',
    new_button_html,
    content,
    flags=re.DOTALL
)

# 3. Add the Modal HTML
modal_html = """
    <!-- New Goods Receipt Modal -->
    <div id="newGoodsReceiptModal" class="hidden fixed inset-0 z-[1000] flex items-center justify-center">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" onclick="toggleModal('newGoodsReceiptModal')"></div>
        
        <!-- Modal Content -->
        <div class="relative bg-white w-[98vw] h-[95vh] rounded-xl shadow-2xl flex flex-col overflow-hidden">
            
            <!-- Modal Header (White Background, simple text as in image) -->
            <div class="flex items-center justify-between px-6 py-3 bg-white border-b border-slate-200">
                <div>
                    <h2 class="text-[18px] font-black text-slate-800 tracking-tight">New Goods Receipt</h2>
                    <div class="flex items-center gap-1 text-[12px] text-slate-500 font-medium">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                        Main Branch
                    </div>
                </div>
                
                <div class="flex items-center gap-3">
                    <!-- Save Split Button -->
                    <div class="relative group/saveModal">
                        <div class="flex items-center bg-[#10b981] text-white rounded overflow-hidden h-[36px] shadow-sm">
                            <button type="button" class="px-6 h-full text-[13px] font-bold hover:brightness-110 transition-all border-r border-white/20">
                                Save
                            </button>
                            <button onclick="toggleActionMenu(event, 'saveGRMenu')" class="px-2 h-full hover:brightness-110 transition-all flex items-center justify-center">
                                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                            </button>
                        </div>
                        <div id="saveGRMenu" class="hidden absolute top-full right-0 mt-1 w-48 bg-white rounded shadow-xl border border-slate-200 py-1 z-[600]">
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save & New</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save as Draft & New</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save & Print</button>
                            <button class="w-full text-left px-4 py-2 text-[12px] text-slate-700 hover:bg-slate-50 transition-all">Save</button>
                        </div>
                    </div>

                    <!-- Cancel Button -->
                    <button type="button" onclick="toggleModal('newGoodsReceiptModal')" class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all">Cancel</button>
                </div>
            </div>

            <!-- Modal Body (Scrollable) -->
            <div class="flex-1 overflow-y-auto bg-white p-6 custom-scrollbar">
                
                <!-- 6 Columns in a single row -->
                <div class="grid grid-cols-6 gap-4 mb-8">
                    <!-- 1. Receipt No -->
                    <div>
                        <label class="block text-[12px] font-bold text-slate-700 mb-1">Receipt No</label>
                        <div class="text-[20px] font-black text-slate-800">GR1</div>
                    </div>
                    
                    <!-- 2. Receipt Date -->
                    <div>
                        <label class="flex items-center gap-1 text-[12px] font-bold text-slate-700 mb-1">
                            Receipt Date
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        </label>
                        <div class="relative">
                            <input type="text" value="24/05/2026" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-700 outline-none focus:border-[var(--accent)]">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                        </div>
                    </div>
                    
                    <!-- 3. Reference # + Gear Icon -->
                    <div class="flex items-end gap-2 relative z-[500]">
                        <div class="flex-1">
                            <label class="flex items-center gap-1 text-[12px] font-bold text-slate-700 mb-1">
                                Reference #
                                <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                            </label>
                            <input type="text" placeholder="Purc.quote,Purc.order,Sup.credit" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] text-slate-400 outline-none focus:border-[var(--accent)]">
                        </div>
                        <div class="relative pb-2">
                            <button onclick="toggleActionMenu(event, 'grRefSettingsMenu')" class="text-slate-600 hover:text-slate-800 transition-all">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                            </button>
                            <div id="grRefSettingsMenu" class="hidden absolute top-full left-0 mt-2 w-64 bg-white rounded shadow-xl p-4 z-[600] border border-slate-200">
                                <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t border-l border-slate-200 rotate-45"></div>
                                <div class="space-y-3 relative z-10">
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded-sm border-slate-300">
                                        <span class="text-[13px] text-slate-800">Show Reverse Charge</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded-sm border-slate-300">
                                        <span class="text-[13px] text-slate-800">Customs Duty Payable</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded-sm border-slate-300">
                                        <span class="text-[13px] text-slate-800">TCS Receivable</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" class="rounded-sm border-slate-300" disabled>
                                        <span class="text-[13px] text-slate-400">Tax Round Off</span>
                                    </label>
                                    
                                    <div class="text-[13px] pt-2 text-slate-800">
                                        Initial Focus <a href="#" class="text-blue-600 hover:underline">Date</a>
                                    </div>
                                    
                                    <label class="flex items-center gap-2 cursor-pointer mt-2">
                                        <input type="checkbox" class="rounded-sm border-slate-300">
                                        <span class="text-[13px] text-slate-800">Ignore Auto Select if multiple Attributes</span>
                                    </label>
                                    
                                    <div class="pt-2 pb-2">
                                        <a href="#" class="text-[13px] text-blue-600 hover:underline">Manage Custom Fields...</a>
                                    </div>
                                    
                                    <button class="px-6 py-2 bg-[#10b981] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Save</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 4. Supplier / Vendor -->
                    <div>
                        <label class="block text-[12px] font-bold text-red-700 mb-1">
                            Supplier / Vendor <span class="text-red-500">*</span>
                        </label>
                        <div class="relative">
                            <input type="text" placeholder="Select Contact (F9)" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold outline-none focus:border-[var(--accent)]">
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </div>
                    </div>
                    
                    <!-- 5. Supplier Delivery Chalan No -->
                    <div>
                        <label class="block text-[10px] text-slate-700 mb-1 leading-tight">Supplier Delivery Chalan No</label>
                        <input type="text" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold outline-none focus:border-[var(--accent)]">
                    </div>
                    
                    <!-- 6. Supplier Delivery Chalan Date -->
                    <div>
                        <label class="block text-[10px] text-slate-700 mb-1 leading-tight">Supplier Delivery Chalan Date</label>
                        <div class="relative">
                            <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold outline-none focus:border-[var(--accent)]">
                            <svg class="w-4 h-4 text-slate-300 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                        </div>
                    </div>
                </div>

                <!-- Items Table -->
                <div class="border border-slate-200 bg-white mb-6 relative z-[300]">
                    <table class="w-full text-left border-collapse">
                        <thead class="bg-white border-b border-slate-200 text-slate-800 text-[12px] font-bold">
                            <tr>
                                <th class="px-4 py-3 w-12 border-r border-slate-200">S.No</th>
                                <th class="px-4 py-3 border-r border-slate-200">Item</th>
                                <th class="px-4 py-3 w-24 border-r border-slate-200 text-center">Qty</th>
                                <th class="px-4 py-3 w-24 border-r border-slate-200 text-center">Unit</th>
                                <th class="px-4 py-3 w-32 border-r border-slate-200 text-right">Rate ₹</th>
                                <th class="px-4 py-3 w-32 border-r border-slate-200 text-right">Amount</th>
                                <th class="px-3 py-3 w-12 text-center relative z-[400]">
                                    <!-- Table Settings Dropdown -->
                                    <button onclick="toggleActionMenu(event, 'grTableSettingsMenu')" class="text-slate-600 hover:text-slate-800 transition-all">
                                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                    </button>
                                    <div id="grTableSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-56 bg-white rounded shadow-xl p-4 z-[600] border border-slate-200 text-left">
                                        <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t border-l border-slate-200 rotate-45"></div>
                                        <div class="space-y-1.5 relative z-10 text-[12px] text-slate-800">
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Description (Below Item)</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>SKU</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>HSN / SAC</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Account</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Tax</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Location</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Qty</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Rate</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" checked class="rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]"><span>Unit</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Net Rate</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>MRP</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Discount Per Item</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Discount Overall</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Group Similar Item</span></div>
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer hover:bg-slate-50 px-1 py-0.5 rounded">
                                                <div class="flex items-center gap-2"><input type="checkbox" class="rounded-sm border-slate-300"><span>Charges Amount</span></div>
                                                <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                                            </label>
                                            
                                            <div class="pt-1">
                                                <a href="#" class="text-[12px] text-blue-600 hover:underline">Manage Custom Fields...</a>
                                            </div>
                                            <label class="flex items-center gap-2 cursor-pointer pt-1">
                                                <input type="checkbox" class="rounded-sm border-slate-300">
                                                <span class="text-[12px]">Item Details in Popup</span>
                                            </label>
                                            
                                            <div class="flex gap-2 pt-2">
                                                <button class="px-5 py-1.5 bg-[#10b981] text-white rounded text-[12px] font-bold hover:brightness-110 transition-all">Save</button>
                                                <button class="px-5 py-1.5 bg-slate-200 text-slate-700 rounded text-[12px] font-bold hover:bg-slate-300 transition-all">Cancel</button>
                                            </div>
                                        </div>
                                    </div>
                                </th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <!-- Row 1 -->
                            <tr>
                                <td class="px-4 py-3 border-r border-slate-200 text-[13px] text-slate-600 text-center">1</td>
                                <td class="px-4 py-2 border-r border-slate-200">
                                    <div class="flex items-center gap-2 border border-blue-400 rounded p-1.5">
                                        <input type="text" placeholder="Search..." class="w-full bg-transparent text-[13px] outline-none">
                                        <svg class="w-4 h-4 text-slate-400" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                        <button class="text-blue-500 hover:text-blue-600"><svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg></button>
                                    </div>
                                </td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-3 py-3 text-center"></td>
                            </tr>
                            <!-- Row 2 -->
                            <tr>
                                <td class="px-4 py-3 border-r border-slate-200 text-[13px] text-slate-600 text-center">2</td>
                                <td class="px-4 py-3 border-r border-slate-200 relative">
                                    <svg class="w-4 h-4 text-slate-300 absolute right-3 top-4 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-3 py-3 text-center"></td>
                            </tr>
                            <!-- Row 3 -->
                            <tr>
                                <td class="px-4 py-3 border-r border-slate-200 text-[13px] text-slate-600 text-center">3</td>
                                <td class="px-4 py-3 border-r border-slate-200 relative">
                                    <svg class="w-4 h-4 text-slate-300 absolute right-3 top-4 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-4 py-3 border-r border-slate-200"></td>
                                <td class="px-3 py-3 text-center"></td>
                            </tr>
                            
                            <!-- Totals -->
                            <tr>
                                <td colspan="4" class="border-t border-slate-200 bg-white"></td>
                                <td class="px-4 py-3 border-r border-l border-t border-slate-200 text-right text-[12px] text-slate-600 bg-white">Sub Total</td>
                                <td class="px-4 py-3 border-r border-t border-slate-200 text-right text-[13px] text-slate-800 bg-white"></td>
                                <td class="border-t border-slate-200 bg-white"></td>
                            </tr>
                            <tr>
                                <td colspan="4" class="bg-white"></td>
                                <td class="px-4 py-3 border-r border-l border-t border-slate-200 text-right text-[12px] text-slate-600 bg-white">Round Off</td>
                                <td class="px-4 py-3 border-r border-t border-slate-200 text-right text-[13px] text-slate-400 bg-white">0.00</td>
                                <td class="bg-white"></td>
                            </tr>
                            <tr>
                                <td colspan="4" class="bg-white"></td>
                                <td class="px-4 py-3 border-r border-l border-t border-b border-slate-200 text-right text-[13px] text-slate-800 font-bold bg-white">Total</td>
                                <td class="px-4 py-3 border-r border-t border-b border-slate-200 text-right text-[14px] font-black text-slate-800 bg-white">₹0.00</td>
                                <td class="border-b border-slate-200 bg-white"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Footer Inputs -->
                <div class="grid grid-cols-3 gap-6">
                    <div>
                        <label class="block text-[12px] text-slate-700 mb-1">Notes</label>
                        <textarea class="w-full h-20 bg-white border border-slate-200 rounded px-3 py-2 text-[13px] outline-none focus:border-[var(--accent)] resize-none"></textarea>
                        <div class="mt-3 flex items-center gap-1 text-[13px] font-bold text-slate-700 cursor-pointer hover:text-slate-900">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21.44 11.05l-9.19 9.19a6 6 0 01-8.49-8.49l9.19-9.19a4 4 0 015.66 5.66l-9.2 9.19a2 2 0 01-2.83-2.83l8.49-8.48"/></svg>
                            Attach File
                        </div>
                    </div>
                    <div>
                        <label class="block text-[12px] text-slate-700 mb-1">Terms & Conditions</label>
                        <textarea class="w-full h-20 bg-white border border-slate-200 rounded px-3 py-2 text-[13px] outline-none focus:border-[var(--accent)] resize-none"></textarea>
                    </div>
                    <div>
                        <label class="block text-[12px] text-slate-700 mb-1">Project</label>
                        <div class="relative">
                            <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold text-slate-400 outline-none focus:border-[var(--accent)] appearance-none">
                                <option>Select Project</option>
                            </select>
                            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

# Insert modal HTML just before the <script> tag
content = content.replace("<script>", modal_html + "\n<script>")

# Add new modal IDs to the JS to close on click outside
content = content.replace(
    "const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu'];",
    "const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu', 'saveGRMenu', 'grRefSettingsMenu', 'grTableSettingsMenu'];"
)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Modal added and button colors updated in goods_receipt.html")
