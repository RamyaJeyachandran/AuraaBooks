import os

template_path = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

html_content = """{% extends 'base.html' %}

{% block title %}Purchase Bill - Auraa Books{% endblock %}
{% block breadcrumb_active %}Purchase Bill{% endblock %}
{% block breadcrumb_parent %}Purchase <span class="opacity-50">/</span>{% endblock %}

{% block content %}
<div class="p-8 stagger-in max-w-[1600px] mx-auto">
    <!-- Header Section -->
    <div class="flex items-center justify-between mb-8 relative z-[300]">
        <div class="flex items-center gap-4 flex-1 mr-6">
            <h1 class="text-[32px] font-black text-slate-800 tracking-tight">Purchase Bill</h1>

            <!-- Compact Count Pills (Similar to Purchase Quote) -->
            <div class="flex-1 flex items-center justify-around bg-white border border-slate-200 rounded-2xl px-8 py-4 shadow-sm max-w-[800px] ml-4">
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Bill Outstanding</span>
                    <span class="text-[30px] font-black text-slate-700 leading-none">(₹1,48,772.00)</span>
                </div>
                <div class="w-px h-12 bg-slate-200"></div>
                <div class="flex flex-col items-center">
                    <span class="text-[10px] font-black text-slate-400 uppercase tracking-widest leading-none mb-2">Bill Overdue</span>
                    <span class="text-[30px] font-black text-amber-500 leading-none">(₹1,48,772.00)</span>
                </div>
            </div>
        </div>
        <div class="flex items-center gap-3">
            <button class="px-6 py-3 bg-[#10b981] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-green-500/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Purchase
            </button>
            <button class="px-6 py-3 bg-[#10b981] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-green-500/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Cash Purchase
            </button>
        </div>
    </div>

    <!-- Actions Section (Similar to Purchase Quote) -->
    <div class="flex items-center justify-end mb-6 relative z-[200]">
        <div class="flex items-center gap-4">
            <!-- Export Split Button -->
            <div class="relative group/export">
                <div class="flex items-center rounded-xl overflow-hidden shadow-sm h-10">
                    <button onclick="toggleActionMenu(event, 'pbExportFormMenu')" class="px-4 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all border-r border-white/20 flex items-center justify-center">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                    </button>
                    <button onclick="toggleActionMenu(event, 'pbExportMenu')" class="px-3 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all flex items-center justify-center">
                        <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </button>
                </div>
                <!-- Export Dropdown -->
                <div id="pbExportMenu" class="hidden absolute top-full right-0 mt-2 w-48 bg-white rounded-2xl shadow-2xl border border-slate-100 py-2 z-[500]">
                    <button class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all">Import XLS</button>
                    <button class="w-full text-left px-6 py-3 text-[13px] font-bold text-slate-600 hover:bg-slate-50 transition-all">Export XLS</button>
                </div>
            </div>

            <!-- Filter Button -->
            <div class="relative group/filter">
                <button onclick="toggleActionMenu(event, 'pbFilterMenu')" class="w-10 h-10 flex items-center justify-center bg-[var(--accent)] text-white hover:brightness-110 rounded-xl transition-all shadow-sm">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
                </button>
                <!-- Filter Popup -->
                <div id="pbFilterMenu" class="hidden absolute top-full right-0 mt-2 w-[400px] bg-white rounded-[32px] shadow-2xl border border-slate-100 p-8 z-[500]">
                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-2">
                            <h4 class="text-[13px] font-black text-slate-800">Transaction Type</h4>
                            <div class="relative">
                                <select class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>All Transactions</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-4 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-2">
                            <h4 class="text-[13px] font-black text-slate-800">Contacts / Purchase Bill# / Ref# / Amount</h4>
                            <div class="relative">
                                <select class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold outline-none focus:border-[var(--accent)] appearance-none">
                                    <option></option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-4 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-2">
                            <h4 class="text-[13px] font-black text-slate-800">Status</h4>
                            <div class="relative">
                                <select class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold text-slate-400 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>Any</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-4 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        
                        <div class="flex items-center gap-4 pt-2">
                            <h4 class="text-[13px] font-black text-slate-800">Date Range</h4>
                            <label class="flex items-center gap-1.5 cursor-pointer">
                                <input type="radio" name="dateRange" checked class="w-4 h-4 accent-slate-800 text-slate-800">
                                <span class="text-[13px] font-bold text-slate-700">Transaction Date</span>
                            </label>
                            <label class="flex items-center gap-1.5 cursor-pointer">
                                <input type="radio" name="dateRange" class="w-4 h-4 accent-slate-800 text-slate-800 border-slate-300">
                                <span class="text-[13px] font-bold text-slate-700">Due Date</span>
                            </label>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-3 pt-1">
                            <div class="space-y-2">
                                <h4 class="text-[13px] font-black text-slate-800">Start Date</h4>
                                <div class="relative">
                                    <input type="text" placeholder="DD/MM/YYYY" class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold text-slate-400 outline-none focus:border-[var(--accent)]">
                                    <svg class="w-4 h-4 text-slate-400 absolute right-4 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                                </div>
                            </div>
                            <div class="space-y-2">
                                <h4 class="text-[13px] font-black text-slate-800">End Date</h4>
                                <div class="relative">
                                    <input type="text" placeholder="DD/MM/YYYY" class="w-full h-11 bg-white border border-slate-200 rounded-xl px-4 text-[13px] font-bold text-slate-400 outline-none focus:border-[var(--accent)]">
                                    <svg class="w-4 h-4 text-slate-400 absolute right-4 top-3.5 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                                </div>
                            </div>
                        </div>

                        <div class="flex gap-3 justify-end pt-4">
                            <button class="px-6 py-3 bg-[#10b981] text-white rounded-xl text-[13px] font-bold hover:brightness-110 transition-all">Search</button>
                            <button class="px-6 py-3 bg-slate-200 text-slate-600 rounded-xl text-[13px] font-bold hover:bg-slate-300 transition-all">Clear</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Settings Button -->
            <div class="relative group/settings">
                <button onclick="toggleActionMenu(event, 'pbSettingsMenu')" class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>
                </button>
                <div id="pbSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded-2xl shadow-2xl border border-slate-100 p-4 z-[500]">
                    <div class="absolute -top-1.5 right-4 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-3">
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Ref.No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Due Days</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-[var(--accent)] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-100 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Status</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-[var(--accent)] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-100 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Due Amount</span>
                        </label>
                        
                        <div class="h-px bg-slate-100 my-3"></div>
                        
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Supplier Invoice No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer group/item">
                            <div class="w-5 h-5 border-2 border-slate-200 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[var(--accent)] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-bold text-slate-700">Supplier Invoice Date</span>
                        </label>
                        
                        <button class="w-full mt-2 py-2.5 bg-[var(--accent)] text-white rounded-lg text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Apply</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Table Section (Similar to Purchase Quote) -->
    <div class="bg-white rounded-3xl border border-slate-100 shadow-sm overflow-hidden mb-6">
        <div class="overflow-x-auto custom-scrollbar">
            <table class="w-full text-left border-collapse">
                <thead class="bg-[var(--accent)] border-b border-slate-200">
                    <tr>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Date</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Purchase Bill No</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Contact</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Status</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Amount</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap border-r border-white/20">Due Amount</th>
                        <th class="px-6 py-4 text-[13px] font-bold text-white whitespace-nowrap text-right">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                    <!-- Row 1 (Highlighted) -->
                    <tr class="bg-blue-50/50 hover:bg-blue-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">14/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">40</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">KARTHICK FLOWER POTS</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹19,650.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right relative">
                            <div class="inline-block">
                                <button onclick="toggleActionMenu(event, 'actionMenu1')" class="text-[13px] font-bold text-[var(--accent)] hover:text-blue-700 flex items-center gap-1 ml-auto">
                                    Delete <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </button>
                                <div id="actionMenu1" class="hidden absolute top-full right-6 mt-1 w-52 bg-white rounded-2xl shadow-xl border border-slate-100 py-3 z-[500] text-left">
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Edit</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Delete</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Storage</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Print</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Send</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Send SMS</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Send WhatsApp</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Copy</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Print BarCode</button>
                                    <button class="w-full text-left px-6 py-2 text-[13px] font-bold text-slate-600 hover:bg-slate-50">Create Sup.credit Note</button>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 2 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">12/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">35</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">Tamil Arasan Wala</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹30,800.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right"></td>
                    </tr>
                    <!-- Row 3 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">10/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">42</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">Vesilin - Chotta Fancy</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹18,000.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right"></td>
                    </tr>
                    <!-- Row 4 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">10/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">34</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">Tamil Arasan Wala</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹39,600.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right"></td>
                    </tr>
                    <!-- Row 5 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">04/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">43</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">Rajkala Fireworks</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹72,080.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right"></td>
                    </tr>
                    <!-- Row 6 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">03/10/2025</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">29</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">Arun Salvarpatti</td>
                        <td class="px-6 py-4">
                            <span class="inline-block px-2.5 py-1 bg-[#10b981] text-white text-[11px] font-black rounded-lg uppercase tracking-wider">Paid</span>
                        </td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-700">₹1,425.00</td>
                        <td class="px-6 py-4 text-[13px] font-bold text-slate-400">-</td>
                        <td class="px-6 py-4 text-right"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
    function toggleActionMenu(event, menuId) {
        event.stopPropagation();
        
        // Close all other menus
        const menus = ['pbExportFormMenu', 'pbExportMenu', 'pbFilterMenu', 'pbSettingsMenu', 'actionMenu1'];
        menus.forEach(id => {
            if (id !== menuId) {
                const el = document.getElementById(id);
                if (el && !el.classList.contains('hidden')) {
                    el.classList.add('hidden');
                }
            }
        });

        // Toggle the clicked menu
        const menu = document.getElementById(menuId);
        if (menu) {
            menu.classList.toggle('hidden');
        }
    }

    // Close menus when clicking outside
    document.addEventListener('click', function(event) {
        const menus = ['pbExportFormMenu', 'pbExportMenu', 'pbFilterMenu', 'pbSettingsMenu', 'actionMenu1'];
        menus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.classList.contains('hidden') && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    });

    // Handle checkboxes styling on click
    document.querySelectorAll('.group\\\\/item input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const box = this.nextElementSibling || this.parentElement;
            if (this.checked) {
                if(box.tagName === 'DIV') {
                    box.classList.remove('opacity-0');
                    box.classList.add('opacity-100');
                    if (this.parentElement.classList.contains('border-slate-200')) {
                        this.parentElement.classList.replace('border-slate-200', 'border-[var(--accent)]');
                        this.parentElement.classList.add('bg-[var(--accent)]');
                        box.innerHTML = '<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>';
                    }
                }
            } else {
                if(box.tagName === 'DIV') {
                    box.classList.remove('opacity-100');
                    box.classList.add('opacity-0');
                    if (this.parentElement.classList.contains('border-[var(--accent)]')) {
                        this.parentElement.classList.replace('border-[var(--accent)]', 'border-slate-200');
                        this.parentElement.classList.remove('bg-[var(--accent)]');
                        box.innerHTML = '';
                    }
                }
            }
        });
    });
</script>
{% endblock %}
"""

with open(template_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated purchase_bill.html layout to match Purchase Quote UX/UI.")
