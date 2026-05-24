import os

with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_modal = content.find('<div id="posViewModal"')
if start_modal == -1:
    print('posViewModal not found')
    exit()

# We need to replace the body of posViewModal. The body starts after:
# <div class="px-8 py-4 border-b border-white/10 flex items-center justify-between bg-[var(--accent)] h-[72px] shrink-0"> ... </div>
# The body is: <div class="p-8 overflow-y-auto custom-scrollbar flex-1 bg-slate-50 relative">

header_str = 'bg-[var(--accent)] h-[72px] shrink-0">'
header_end = content.find('</div>', content.find('</div>', content.find(header_str, start_modal)) + 10) 
# wait, it's easier to find the exact comment:
body_start = content.find('<!-- Modal Body -->', start_modal)
end_modal = content.find('<script>', start_modal)

# We want to replace from body_start to end_modal (excluding the trailing closing divs of the modal itself).
# Specifically, we replace from '<!-- Modal Body -->' to the end of the modal body div.

pos_body_html = """        <!-- Modal Body (POS View Layout) -->
        <div class="flex-1 flex overflow-hidden bg-slate-50">
            
            <!-- Left Panel: Products -->
            <div class="flex-1 flex flex-col border-r border-slate-200">
                <!-- Search Bar -->
                <div class="p-4 border-b border-slate-200 bg-white shadow-sm z-10 flex gap-4">
                    <div class="relative flex-1">
                        <svg class="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                        <input type="text" placeholder="Scan Barcode or Search Items (F3)..." class="w-full h-12 pl-12 pr-4 bg-slate-100/50 border border-slate-200 rounded-xl text-[14px] font-bold text-slate-700 outline-none focus:border-accent focus:bg-white focus:ring-4 focus:ring-accent/10 transition-all">
                    </div>
                    <button class="px-6 h-12 bg-white border border-slate-200 text-slate-600 rounded-xl font-bold text-[13px] hover:bg-slate-50 hover:text-accent hover:border-accent transition-all flex items-center gap-2 shadow-sm">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path></svg>
                        Filter
                    </button>
                </div>
                
                <!-- Product Grid -->
                <div class="flex-1 p-6 overflow-y-auto custom-scrollbar bg-slate-50">
                    <div class="grid grid-cols-2 lg:grid-cols-3 gap-4">
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center">
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Premium Widget</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: WID-001</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 1,299.00</div>
                        </div>
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center relative overflow-hidden">
                            <div class="absolute top-3 right-3 w-2 h-2 rounded-full bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"></div>
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Super Gadget</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: GAD-002</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 899.00</div>
                        </div>
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center relative overflow-hidden">
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Basic Tool</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: TOL-003</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 349.00</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel: Cart -->
            <div class="w-[380px] bg-white flex flex-col shrink-0">
                <!-- Customer Selection -->
                <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-accent/10 text-accent flex items-center justify-center">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                        </div>
                        <div>
                            <div class="text-[13px] font-black text-slate-800 leading-tight">Walk-in Customer</div>
                            <div class="text-[11px] font-bold text-slate-400">Cash Sale</div>
                        </div>
                    </div>
                    <button class="w-8 h-8 rounded-lg text-slate-400 hover:text-accent hover:bg-accent/10 flex items-center justify-center transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                </div>

                <!-- Cart Items -->
                <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-4">
                    
                    <!-- Cart Item -->
                    <div class="flex items-start gap-4">
                        <div class="w-16 h-16 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-center shrink-0">
                            <svg class="w-6 h-6 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                        </div>
                        <div class="flex-1">
                            <div class="flex justify-between items-start mb-2">
                                <h4 class="text-[13px] font-black text-slate-800 leading-tight">Premium Widget</h4>
                                <button class="text-slate-300 hover:text-red-500 transition-colors">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                                </button>
                            </div>
                            <div class="flex items-center justify-between">
                                <div class="text-[14px] font-black text-accent">₹ 1,299.00</div>
                                <div class="flex items-center gap-3 bg-slate-50 border border-slate-200 rounded-lg px-2 py-1">
                                    <button class="text-slate-400 hover:text-accent"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M20 12H4"></path></svg></button>
                                    <span class="text-[13px] font-black text-slate-800 min-w-[20px] text-center">1</span>
                                    <button class="text-slate-400 hover:text-accent"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 4v16m8-8H4"></path></svg></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>

                <!-- Totals -->
                <div class="bg-slate-50 p-6 border-t border-slate-200 space-y-3">
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Sub Total</span>
                        <span class="font-black text-slate-700">₹ 1,299.00</span>
                    </div>
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Tax</span>
                        <span class="font-black text-slate-700">₹ 0.00</span>
                    </div>
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Discount</span>
                        <span class="font-black text-green-600">- ₹ 0.00</span>
                    </div>
                    <div class="border-t border-slate-200/60 pt-3 flex justify-between items-end mt-2">
                        <span class="text-[12px] font-black text-slate-400 uppercase tracking-widest">Total Amount</span>
                        <span class="text-[28px] font-black text-slate-800 leading-none">₹ 1,299</span>
                    </div>
                    <button class="w-full h-14 bg-accent hover:brightness-110 text-white rounded-[16px] text-[15px] font-black tracking-wide uppercase transition-all shadow-lg shadow-accent/20 mt-4 flex items-center justify-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Save Challan
                    </button>
                </div>
            </div>
            
        </div>
    </div>
</div>
"""

# Let's completely replace posViewModal
end_div_pos = content.find('</div>', end_modal)
while True:
    if content[end_div_pos-10:end_div_pos] == '</div>':
        end_div_pos = content.find('</div>', end_div_pos + 6)
    else:
        # just replace up to <script>
        break

start_idx = content.find('<div id="posViewModal"')
end_idx = content.find('<script>', start_idx)

# Find the end of the modal by looking backward from <script>
real_end = content.rfind('</div>', start_idx, end_idx) + 6

content = content[:start_idx] + pos_body_html + content[real_end:]

# Wait, pos_body_html doesn't include <div id="posViewModal"> header! I just overwrote the whole modal!
# I need to include the header in pos_body_html.

pos_full_html = """<div id="posViewModal" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-[9999] hidden items-center justify-center p-4 md:p-8">
    <div class="bg-white w-full max-w-[1200px] h-[95vh] rounded-[24px] shadow-2xl overflow-hidden flex flex-col relative mx-auto my-auto scale-in-center animate-erp-fade">
        <!-- Modal Header / Sticky Top Toolbar -->
        <div class="px-8 py-4 border-b border-white/10 flex items-center justify-between bg-[var(--accent)] h-[72px] shrink-0">
            <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center border border-white/30">
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="18" rx="2" ry="2"/><line x1="2" y1="8" x2="22" y2="8"/><line x1="8" y1="18" x2="8" y2="8"/></svg>
                </div>
                <div class="flex flex-col">
                    <div class="flex items-center gap-3">
                        <h3 class="text-[20px] font-black text-white leading-none">New Delivery Challan</h3>
                        <div class="px-3 py-1 bg-white/20 rounded-lg text-[11px] font-black text-white uppercase tracking-widest border border-white/10 backdrop-blur-md">
                            POS View
                        </div>
                    </div>
                    <div class="flex items-center gap-2 mt-1.5 opacity-80">
                        <span class="w-1.5 h-1.5 rounded-full bg-green-400 shadow-[0_0_8px_rgba(74,222,128,0.8)]"></span>
                        <span class="text-[11px] font-bold text-white uppercase tracking-wider">Main Branch</span>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-4">
                <button onclick="closePosViewModal()" class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 text-white transition-all">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
        </div>

        <!-- Modal Body (POS View Layout) -->
        <div class="flex-1 flex overflow-hidden bg-slate-50">
            
            <!-- Left Panel: Products -->
            <div class="flex-1 flex flex-col border-r border-slate-200">
                <!-- Search Bar -->
                <div class="p-4 border-b border-slate-200 bg-white shadow-sm z-10 flex gap-4">
                    <div class="relative flex-1">
                        <svg class="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                        <input type="text" placeholder="Scan Barcode or Search Items (F3)..." class="w-full h-12 pl-12 pr-4 bg-slate-100/50 border border-slate-200 rounded-xl text-[14px] font-bold text-slate-700 outline-none focus:border-accent focus:bg-white focus:ring-4 focus:ring-accent/10 transition-all">
                    </div>
                    <button class="px-6 h-12 bg-white border border-slate-200 text-slate-600 rounded-xl font-bold text-[13px] hover:bg-slate-50 hover:text-accent hover:border-accent transition-all flex items-center gap-2 shadow-sm">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path></svg>
                        Filter
                    </button>
                </div>
                
                <!-- Product Grid -->
                <div class="flex-1 p-6 overflow-y-auto custom-scrollbar bg-slate-50">
                    <div class="grid grid-cols-2 lg:grid-cols-3 gap-4">
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center">
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Premium Widget</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: WID-001</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 1,299.00</div>
                        </div>
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center relative overflow-hidden">
                            <div class="absolute top-3 right-3 w-2 h-2 rounded-full bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"></div>
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Super Gadget</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: GAD-002</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 899.00</div>
                        </div>
                        <!-- Product Card -->
                        <div class="bg-white rounded-[20px] p-4 border border-slate-200 hover:border-accent hover:shadow-lg hover:shadow-accent/5 transition-all cursor-pointer group flex flex-col items-center text-center relative overflow-hidden">
                            <div class="w-24 h-24 bg-slate-100 rounded-2xl mb-4 flex items-center justify-center text-slate-400 group-hover:bg-accent/5 group-hover:text-accent transition-colors">
                                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                            </div>
                            <h4 class="text-[14px] font-black text-slate-800 mb-1 leading-tight group-hover:text-accent transition-colors">Basic Tool</h4>
                            <p class="text-[11px] font-bold text-slate-400 mb-3">SKU: TOL-003</p>
                            <div class="text-[16px] font-black text-slate-800">₹ 349.00</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel: Cart -->
            <div class="w-[380px] bg-white flex flex-col shrink-0">
                <!-- Customer Selection -->
                <div class="p-4 border-b border-slate-100 flex items-center justify-between">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-accent/10 text-accent flex items-center justify-center">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                        </div>
                        <div>
                            <div class="text-[13px] font-black text-slate-800 leading-tight">Walk-in Customer</div>
                            <div class="text-[11px] font-bold text-slate-400">Cash Sale</div>
                        </div>
                    </div>
                    <button class="w-8 h-8 rounded-lg text-slate-400 hover:text-accent hover:bg-accent/10 flex items-center justify-center transition-colors">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                </div>

                <!-- Cart Items -->
                <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-4">
                    
                    <!-- Cart Item -->
                    <div class="flex items-start gap-4">
                        <div class="w-16 h-16 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-center shrink-0">
                            <svg class="w-6 h-6 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                        </div>
                        <div class="flex-1">
                            <div class="flex justify-between items-start mb-2">
                                <h4 class="text-[13px] font-black text-slate-800 leading-tight">Premium Widget</h4>
                                <button class="text-slate-300 hover:text-red-500 transition-colors">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                                </button>
                            </div>
                            <div class="flex items-center justify-between">
                                <div class="text-[14px] font-black text-accent">₹ 1,299.00</div>
                                <div class="flex items-center gap-3 bg-slate-50 border border-slate-200 rounded-lg px-2 py-1">
                                    <button class="text-slate-400 hover:text-accent"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M20 12H4"></path></svg></button>
                                    <span class="text-[13px] font-black text-slate-800 min-w-[20px] text-center">1</span>
                                    <button class="text-slate-400 hover:text-accent"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 4v16m8-8H4"></path></svg></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>

                <!-- Totals -->
                <div class="bg-slate-50 p-6 border-t border-slate-200 space-y-3">
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Sub Total</span>
                        <span class="font-black text-slate-700">₹ 1,299.00</span>
                    </div>
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Tax</span>
                        <span class="font-black text-slate-700">₹ 0.00</span>
                    </div>
                    <div class="flex justify-between items-center text-[13px]">
                        <span class="font-bold text-slate-500">Discount</span>
                        <span class="font-black text-green-600">- ₹ 0.00</span>
                    </div>
                    <div class="border-t border-slate-200/60 pt-3 flex justify-between items-end mt-2">
                        <span class="text-[12px] font-black text-slate-400 uppercase tracking-widest">Total Amount</span>
                        <span class="text-[28px] font-black text-slate-800 leading-none">₹ 1,299</span>
                    </div>
                    <button class="w-full h-14 bg-accent hover:brightness-110 text-white rounded-[16px] text-[15px] font-black tracking-wide uppercase transition-all shadow-lg shadow-accent/20 mt-4 flex items-center justify-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Save Challan
                    </button>
                </div>
            </div>
            
        </div>
    </div>
</div>
"""

content = content[:start_idx] + pos_full_html + content[real_end:]

with open('d:/AuraaZenAIProject/abproject/templates/sales_delivery_challan.html', 'w', encoding='utf-8') as f2:
    f2.write(content)

print('POS layout correctly injected into posViewModal.')
