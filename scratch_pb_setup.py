import os
import re

# 1. Create the template file
template_path = r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html"

html_content = """{% extends 'base.html' %}

{% block title %}Purchase Bill - Auraa Books{% endblock %}

{% block content %}
<div class="p-8 stagger-in max-w-[1600px] mx-auto">
    <!-- Header Row -->
    <div class="flex items-start justify-between mb-8">
        <div>
            <div class="flex items-center text-[18px] text-slate-500 font-medium">
                Purchase /
                <div class="relative group ml-1">
                    <button onclick="toggleActionMenu(event, 'titleDropdown')" class="flex items-center gap-1 text-[var(--accent)] font-bold hover:brightness-110">
                        Purchase Bill
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <!-- Title Dropdown -->
                    <div id="titleDropdown" class="hidden absolute top-full left-0 mt-2 w-48 bg-white rounded-lg shadow-xl border border-slate-100 py-2 z-[500]">
                        <a href="#" class="block px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-colors">Recent Bills</a>
                        <a href="#" class="block px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-colors">All Bills</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex items-center gap-2">
            <button class="px-5 py-2.5 bg-[#10b981] text-white rounded text-[14px] font-bold shadow-md shadow-green-500/20 hover:brightness-110 transition-all">
                New Purchase
            </button>
            <button class="px-5 py-2.5 bg-[#10b981] text-white rounded text-[14px] font-bold shadow-md shadow-green-500/20 hover:brightness-110 transition-all">
                New Cash Purchase
            </button>
        </div>
    </div>

    <!-- Summary Stats Row -->
    <div class="flex items-center gap-32 mb-10 pl-20">
        <div class="flex flex-col items-center">
            <div class="text-[22px] font-black text-slate-800 mb-2">(₹1,48,772.00)</div>
            <div class="text-[11px] font-medium text-slate-400 leading-none">Bill</div>
            <div class="text-[16px] font-bold text-slate-700">Outstanding</div>
        </div>
        <div class="flex flex-col items-center">
            <div class="text-[22px] font-black text-slate-800 mb-2">(₹1,48,772.00)</div>
            <div class="text-[11px] font-medium text-slate-400 leading-none">Bill</div>
            <div class="text-[16px] font-bold text-slate-700">Overdue</div>
        </div>
    </div>

    <!-- Action Buttons Row -->
    <div class="flex items-center justify-end mb-4 relative z-[200]">
        <div class="flex items-center gap-2">
            <!-- Export Split Button (Gray) -->
            <div class="relative group/export">
                <div class="flex items-center rounded-lg overflow-hidden h-9 bg-[#e2e8f0]">
                    <button class="px-3 h-full text-slate-600 hover:bg-slate-300 transition-all border-r border-slate-300 flex items-center justify-center">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
                    </button>
                    <button onclick="toggleActionMenu(event, 'exportMenu')" class="px-2 h-full text-slate-600 hover:bg-slate-300 transition-all flex items-center justify-center">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                    </button>
                </div>
                <!-- Export Dropdown -->
                <div id="exportMenu" class="hidden absolute top-full right-0 mt-1 w-40 bg-white rounded shadow-lg border border-slate-200 py-1 z-[500]">
                    <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Import XLS</button>
                    <button class="w-full text-left px-4 py-2 text-[13px] text-slate-700 hover:bg-slate-50 transition-all">Export XLS</button>
                </div>
            </div>

            <!-- Filter Button (Gray) -->
            <div class="relative group/filter">
                <button onclick="toggleActionMenu(event, 'filterMenu')" class="w-9 h-9 flex items-center justify-center bg-[#e2e8f0] text-slate-600 hover:bg-slate-300 rounded-lg transition-all">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
                </button>
                <!-- Filter Popup -->
                <div id="filterMenu" class="hidden absolute top-full right-0 mt-2 w-[400px] bg-white rounded-xl shadow-2xl border border-slate-200 p-6 z-[500]">
                    <div class="absolute -top-1.5 right-3 w-3 h-3 bg-white border-t border-l border-slate-200 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Transaction Type</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>All Transactions</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Contacts / Purchase Bill# / Ref# / Amount</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option></option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Status</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-400 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>Any</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        
                        <div class="flex items-center gap-4 pt-2">
                            <label class="text-[12px] font-bold text-slate-800">Date Range</label>
                            <label class="flex items-center gap-1.5 cursor-pointer">
                                <input type="radio" name="dateRange" checked class="w-3.5 h-3.5 accent-slate-800 text-slate-800">
                                <span class="text-[13px] text-slate-700">Transaction Date</span>
                            </label>
                            <label class="flex items-center gap-1.5 cursor-pointer">
                                <input type="radio" name="dateRange" class="w-3.5 h-3.5 accent-slate-800 text-slate-800 border-slate-300">
                                <span class="text-[13px] text-slate-700">Due Date</span>
                            </label>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-3 pt-1">
                            <div class="space-y-1.5">
                                <label class="text-[12px] font-bold text-slate-800">Start Date</label>
                                <div class="relative">
                                    <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-300 outline-none focus:border-[var(--accent)]">
                                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                                </div>
                            </div>
                            <div class="space-y-1.5">
                                <label class="text-[12px] font-bold text-slate-800">End Date</label>
                                <div class="relative">
                                    <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] text-slate-300 outline-none focus:border-[var(--accent)]">
                                    <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                                </div>
                            </div>
                        </div>

                        <div class="flex gap-2 justify-end pt-4">
                            <button class="px-6 py-2 bg-[#10b981] text-white rounded text-[13px] font-bold hover:brightness-110 transition-all">Search</button>
                            <button class="px-6 py-2 bg-slate-200 text-slate-700 rounded text-[13px] font-bold hover:bg-slate-300 transition-all">Clear</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Settings Button (Vertical Dots) -->
            <div class="relative group/settings">
                <button onclick="toggleActionMenu(event, 'settingsMenu')" class="w-9 h-9 flex items-center justify-center text-slate-500 hover:text-slate-700 transition-all">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>
                </button>
                <div id="settingsMenu" class="hidden absolute top-full right-0 mt-1 w-56 bg-white rounded shadow-xl border border-slate-200 p-4 z-[500]">
                    <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t border-l border-slate-200 rotate-45"></div>
                    <div class="space-y-3">
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-slate-300 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[#008f8f] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Ref.No</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-slate-300 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[#008f8f] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Due Days</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-[#008f8f] bg-[#008f8f] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Status</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-[#008f8f] bg-[#008f8f] rounded flex items-center justify-center transition-all">
                                <input type="checkbox" checked class="hidden">
                                <svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Due Amount</span>
                        </label>
                        
                        <div class="h-px bg-slate-100 my-2"></div>
                        
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-slate-300 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[#008f8f] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Invoice No</span>
                        </label>
                        <label class="flex items-center gap-2 cursor-pointer group/item">
                            <div class="w-4 h-4 border border-slate-300 rounded flex items-center justify-center transition-all">
                                <input type="checkbox" class="hidden">
                                <div class="w-2.5 h-2.5 bg-[#008f8f] rounded-sm opacity-0 transition-all"></div>
                            </div>
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Invoice Date</span>
                        </label>
                        
                        <div class="pt-2">
                            <button class="px-4 py-1.5 bg-slate-200 text-slate-700 rounded text-[13px] font-bold hover:bg-slate-300 transition-all">Apply</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Table Section -->
    <div class="bg-white border border-slate-200">
        <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
                <thead class="bg-white border-b border-slate-200">
                    <tr>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Date</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Purchase Bill No</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Contact</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Status</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Amount</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800">Due Amount</th>
                        <th class="px-4 py-4 text-[12px] font-black text-slate-800 text-right">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                    <!-- Row 1 (Highlighted) -->
                    <tr class="bg-[#dbeafe] hover:bg-blue-100/80 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">14/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">40</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">KARTHICK FLOWER POTS</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹19,650.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right relative">
                            <div class="inline-block">
                                <button onclick="toggleActionMenu(event, 'actionMenu1')" class="text-[13px] font-bold text-slate-500 hover:text-slate-800 flex items-center gap-1">
                                    Delete <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </button>
                                <div id="actionMenu1" class="hidden absolute top-full right-4 mt-1 w-48 bg-white rounded shadow-xl border border-slate-100 py-2 z-[500] text-left">
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Edit</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Delete</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Storage</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Print</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Send</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Send SMS</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Send WhatsApp</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Copy</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Print BarCode</button>
                                    <button class="w-full text-left px-4 py-1.5 text-[11px] text-slate-700 hover:bg-slate-50">Create Sup.credit Note</button>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 2 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">12/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">35</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">Tamil Arasan Wala</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹30,800.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right"></td>
                    </tr>
                    <!-- Row 3 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">10/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">42</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">Vesilin - Chotta Fancy</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹18,000.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right"></td>
                    </tr>
                    <!-- Row 4 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">10/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">34</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">Tamil Arasan Wala</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹39,600.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right"></td>
                    </tr>
                    <!-- Row 5 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">04/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">43</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">Rajkala Fireworks</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹72,080.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right"></td>
                    </tr>
                    <!-- Row 6 -->
                    <tr class="hover:bg-slate-50 transition-colors">
                        <td class="px-4 py-3 text-[13px] text-slate-700">03/10/2025</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">29</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">Arun Salvarpatti</td>
                        <td class="px-4 py-3">
                            <span class="inline-block px-2 py-0.5 bg-[#22c55e] text-white text-[11px] font-bold rounded">Paid</span>
                        </td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">₹1,425.00</td>
                        <td class="px-4 py-3 text-[13px] text-slate-700">-</td>
                        <td class="px-4 py-3 text-right"></td>
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
        const menus = ['titleDropdown', 'exportMenu', 'filterMenu', 'settingsMenu', 'actionMenu1'];
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
        const menus = ['titleDropdown', 'exportMenu', 'filterMenu', 'settingsMenu', 'actionMenu1'];
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
                    if (this.parentElement.classList.contains('border-slate-300')) {
                        this.parentElement.classList.replace('border-slate-300', 'border-[#008f8f]');
                        this.parentElement.classList.add('bg-[#008f8f]');
                        box.innerHTML = '<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>';
                    }
                }
            } else {
                if(box.tagName === 'DIV') {
                    box.classList.remove('opacity-100');
                    box.classList.add('opacity-0');
                    if (this.parentElement.classList.contains('border-[#008f8f]')) {
                        this.parentElement.classList.replace('border-[#008f8f]', 'border-slate-300');
                        this.parentElement.classList.remove('bg-[#008f8f]');
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


# 2. Add view to core/views.py
views_path = r"d:\AuraaZenAIProject\abproject\apps\core\views.py"
with open(views_path, "r", encoding="utf-8") as f:
    views_content = f.read()

if "class PurchaseBillView" not in views_content:
    new_view = """
class PurchaseBillView(TemplateView):
    template_name = 'purchase_bill.html'
"""
    views_content += new_view
    with open(views_path, "w", encoding="utf-8") as f:
        f.write(views_content)


# 3. Add url route to abproject/urls.py
urls_path = r"d:\AuraaZenAIProject\abproject\abproject\urls.py"
with open(urls_path, "r", encoding="utf-8") as f:
    urls_content = f.read()

if "PurchaseBillView" not in urls_content:
    urls_content = urls_content.replace(
        "from apps.core.views import",
        "from apps.core.views import PurchaseBillView,"
    )
    urls_content = urls_content.replace(
        "path('purchase_quotes/', PurchaseQuotesView.as_view(), name='purchase_quotes'),",
        "path('purchase_quotes/', PurchaseQuotesView.as_view(), name='purchase_quotes'),\n    path('purchase_bill/', PurchaseBillView.as_view(), name='purchase_bill'),"
    )
    with open(urls_path, "w", encoding="utf-8") as f:
        f.write(urls_content)

print("Created purchase_bill.html and updated routing successfully.")
