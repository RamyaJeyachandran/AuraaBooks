html_code = '''
<!-- Quick View Modal -->
<div id="quickViewModal" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-[1000] hidden items-center justify-center p-4 md:p-8">
    <div class="bg-white w-full max-w-[1000px] md:h-[90vh] rounded-[16px] shadow-2xl overflow-hidden flex flex-col relative mx-auto my-auto scale-in-center animate-erp-fade">
        <!-- Top Toolbar -->
        <div class="bg-slate-100 px-6 py-4 flex items-center justify-between border-b border-slate-200 shrink-0">
            <!-- Left: Settings/View Dropdown -->
            <div class="relative flex items-center">
                <button type="button" onclick="toggleActionMenu(event, 'qvTopDropdown')" class="flex items-center gap-2 bg-slate-200 hover:bg-slate-300 text-slate-700 px-3 py-1.5 rounded-md font-bold text-[13px] transition-all">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h2m-2 4h2m-6 4h6"/></svg>
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                </button>
                <div id="qvTopDropdown" class="hidden absolute top-full left-0 mt-2 w-56 bg-white rounded-lg shadow-xl border border-slate-200 py-1.5 z-[1100]">
                    <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Invoice No</div>
                    <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Date</div>
                    <div class="px-4 py-2 text-[13px] text-white bg-blue-600 font-bold cursor-pointer">Contact/Item</div>
                    <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Buyer's Order No#</div>
                    <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Buyer's Order Date</div>
                    <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Item</div>
                </div>
            </div>

            <!-- Right: Save & Cancel -->
            <div class="flex items-center gap-3">
                <div class="relative flex items-center h-9 select-none">
                    <div class="flex items-stretch rounded-md overflow-hidden bg-[#1cb054] shadow-sm">
                        <button type="button" class="px-5 text-white font-bold text-[13px] hover:bg-[#158f43] transition-all">Save</button>
                        <div class="w-[1px] bg-white/20"></div>
                        <button type="button" onclick="toggleActionMenu(event, 'qvSaveMenu')" class="px-2 text-white hover:bg-[#158f43] transition-all flex items-center justify-center">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                    </div>
                    <div id="qvSaveMenu" class="hidden absolute top-full right-0 mt-1.5 w-40 bg-white rounded-lg shadow-xl border border-slate-200 py-1.5 z-[1100]">
                        <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Save</div>
                        <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Save &amp; New</div>
                        <div class="px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 cursor-pointer">Save &amp; Print</div>
                    </div>
                </div>
                <button type="button" onclick="closeQuickViewModal()" class="px-5 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 rounded-md text-[13px] font-bold transition-all border-none focus:outline-none">Cancel</button>
            </div>
        </div>

        <!-- Body -->
        <div class="flex-1 overflow-y-auto bg-white">
            <div class="p-8">
                <!-- Header Info -->
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h2 class="text-2xl font-black text-slate-800">ORD1</h2>
                        <div class="text-[13px] font-medium text-slate-600 mt-1">21/05/2026</div>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="text-3xl font-black text-slate-800">?0.00</div>
                        <div class="relative">
                            <button type="button" onclick="toggleActionMenu(event, 'qvSettingsMenu')" class="text-slate-500 hover:text-slate-700 focus:outline-none">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/></svg>
                            </button>
                            <div id="qvSettingsMenu" class="hidden absolute top-full right-0 mt-3 w-[300px] bg-white rounded-lg shadow-xl border border-slate-200 py-2 z-[1100]">
                                <div class="absolute -top-1.5 right-1.5 w-3 h-3 bg-white border-l border-t border-slate-200 transform rotate-45"></div>
                                <div class="px-4 py-2.5 text-[14px] text-slate-700 hover:bg-slate-50 cursor-pointer relative z-10">Skip Rate if defined in Item</div>
                                <div class="px-4 py-2.5 text-[14px] text-slate-700 hover:bg-slate-50 cursor-pointer relative z-10">Skip Quantity with value as 1</div>
                                <div class="px-4 py-2.5 text-[14px] text-slate-700 hover:bg-slate-50 cursor-pointer relative z-10 border-b border-slate-200 mb-1">Skip / Hide Discount if defined in Item</div>
                                <div class="px-4 py-2.5 text-[14px] text-slate-700 hover:bg-slate-50 cursor-pointer relative z-10 flex items-center gap-2">
                                    <svg class="w-4 h-4 text-[#1cb054]" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                    Discount Overall
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Customer Selection -->
                <div class="mb-10 relative">
                    <div class="flex items-center gap-1.5 mb-2">
                        <span class="text-[15px] text-slate-700">Enter</span>
                        <div class="flex items-center gap-1 text-blue-600 font-bold cursor-pointer hover:underline select-none" onclick="toggleActionMenu(event, 'qvCustomerTypeMenu')">
                            <span class="text-[17px]">Customer</span>
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                        </div>
                    </div>
                    <div class="w-[500px] relative">
                        <input type="text" placeholder="Search" class="w-full px-4 py-2 rounded border border-slate-200 focus:outline-none focus:border-blue-500 text-[14px] text-slate-700">
                    </div>
                </div>

                <!-- Table -->
                <div class="border border-slate-200 rounded-sm mb-8">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-50/50 border-b border-slate-200">
                                <th class="px-4 py-3.5 text-[13px] font-bold text-slate-700 w-full">Item</th>
                                <th class="px-3 py-3.5 text-[13px] font-bold text-slate-700 whitespace-nowrap text-center border-l border-slate-200 min-w-[70px]">
                                    <div class="flex items-center justify-center gap-1.5 relative">
                                        <svg class="w-[18px] h-[18px] text-blue-600 cursor-pointer hover:text-blue-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                                        <div class="group">
                                            <svg class="w-[15px] h-[15px] text-slate-400 cursor-help hover:text-slate-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                            <div class="hidden group-hover:block absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[180px] bg-white border border-slate-200 shadow-xl p-3 text-[12px] text-slate-700 z-[1200] leading-snug rounded shadow-md font-normal whitespace-normal text-left">
                                                Click it to enter Detailed information about the item
                                                <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-l border-t border-slate-200 transform rotate-45"></div>
                                            </div>
                                        </div>
                                    </div>
                                </th>
                                <th class="px-4 py-3.5 text-[13px] font-bold text-slate-700 w-24 text-center border-l border-slate-200">Qty</th>
                                <th class="px-4 py-3.5 text-[13px] font-bold text-slate-700 w-[100px] text-center border-l border-slate-200">Rate ?</th>
                                <th class="px-4 py-3.5 text-[13px] font-bold text-slate-700 w-[90px] text-center border-l border-slate-200">Discount</th>
                                <th class="px-4 py-3.5 text-[13px] font-bold text-slate-700 w-[110px] text-center border-l border-slate-200">Amount</th>
                                <th class="w-10 border-l border-slate-200"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Empty Item Row for exact match with screenshot -->
                            <tr class="border-b border-slate-200 h-10">
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td class="px-4 py-2 border-r border-slate-200"></td>
                                <td></td>
                            </tr>
                            
                            <!-- Sub Total -->
                            <tr class="border-b border-slate-200">
                                <td colspan="5" class="px-4 py-3 text-[12px] font-bold text-slate-700 text-right">Sub Total</td>
                                <td class="px-4 py-3 border-l border-r border-slate-200 text-right"></td>
                                <td></td>
                            </tr>

                            <!-- less Discount -->
                            <tr class="border-b border-slate-200">
                                <td colspan="5" class="px-4 py-0 text-right border-0 bg-white">
                                    <div class="h-10 flex items-center justify-end pr-4 text-[12px]">
                                        <span class="italic text-slate-500 mr-1">less</span><span class="font-bold text-slate-700">Discount</span>
                                    </div>
                                </td>
                                <td class="px-0 py-0 border-l border-r border-slate-200 bg-white h-10">
                                    <input type="text" value="0" class="w-full h-full px-4 text-right outline-none text-[13px] text-slate-700">
                                </td>
                                <td></td>
                            </tr>

                            <!-- Total -->
                            <tr>
                                <td colspan="5" class="px-4 py-3 text-[12px] font-bold text-slate-700 text-right">Total</td>
                                <td class="px-4 py-3 border-l border-r border-slate-200 text-[13px] font-black text-slate-800 text-right bg-white">?0.00</td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
'''

content = open('templates/sales_orders.html', encoding='utf-8').read()
new_content = content.replace('<script>', html_code + '\n<script>')
with open('templates/sales_orders.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
