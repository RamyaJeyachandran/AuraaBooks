import os
import re

html_file = r"d:\AuraaZenAIProject\abproject\templates\goods_receipt.html"

# I will recreate goods_receipt.html cleanly using the purchase_quotes structure.
# This fixes the duplicate block issue.
new_content = """{% extends 'base.html' %}

{% block title %}Goods Receipt - Auraa Books{% endblock %}

{% block breadcrumb_active %}Goods Receipt{% endblock %}

{% block content %}
<div class="px-8 py-6 max-w-[1600px] mx-auto pb-32">
    <!-- Header Section -->
    <div class="flex items-center justify-between mb-8">
        <div>
            <h1 class="text-[32px] font-black text-slate-800 tracking-tight flex items-center gap-3">
                Goods Receipt
                <div class="relative group">
                    <svg class="w-6 h-6 text-slate-400 hover:text-slate-600 transition-colors cursor-pointer" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                    <!-- Title Dropdown Menu -->
                    <div id="grTitleDropdownMenu" class="hidden absolute top-full left-0 mt-2 w-64 bg-white rounded-xl shadow-2xl border border-slate-100 p-2 z-[500]">
                        <div class="px-3 py-2 text-[11px] font-black text-slate-400 uppercase tracking-widest mb-1">Recent Quotes</div>
                        <a href="#" class="block px-3 py-2 hover:bg-slate-50 rounded-lg transition-colors">
                            <div class="flex items-center justify-between">
                                <span class="text-[13px] font-bold text-slate-700">PQ-2024-001</span>
                                <span class="text-[11px] font-medium text-slate-400">2 mins ago</span>
                            </div>
                        </a>
                        <a href="#" class="block px-3 py-2 hover:bg-slate-50 rounded-lg transition-colors">
                            <div class="flex items-center justify-between">
                                <span class="text-[13px] font-bold text-slate-700">PQ-2024-002</span>
                                <span class="text-[11px] font-medium text-slate-400">1 hr ago</span>
                            </div>
                        </a>
                        <div class="h-px bg-slate-100 my-2"></div>
                        <a href="#" class="block px-3 py-2 text-[12px] font-bold text-[var(--accent)] hover:bg-slate-50 rounded-lg transition-colors text-center">
                            View All Quotes
                        </a>
                    </div>
                </div>
            </h1>
            <div class="flex items-center gap-3 mt-2 text-[13px] font-medium text-slate-500">
                <a href="#" class="hover:text-[var(--accent)] transition-colors">Purchase</a>
                <span class="w-1.5 h-1.5 rounded-full bg-slate-300"></span>
                <span class="text-slate-700 font-bold">Goods Receipt</span>
            </div>
        </div>

        <div class="flex items-center gap-4">
            <!-- Summary Pills -->
            <div class="flex bg-white rounded-xl shadow-sm border border-slate-200 p-1.5">
                <div class="px-4 border-r border-slate-100 text-center">
                    <div class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-0.5">Total</div>
                    <div class="text-[16px] font-black text-slate-800">0</div>
                </div>
                <div class="px-4 border-r border-slate-100 text-center">
                    <div class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-0.5">Active</div>
                    <div class="text-[16px] font-black text-[#10b981]">0</div>
                </div>
                <div class="px-4 text-center">
                    <div class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-0.5">Void</div>
                    <div class="text-[16px] font-black text-[#f59e0b]">0</div>
                </div>
            </div>

            <!-- Recent Navigator -->
            <div class="flex items-center bg-white rounded-xl shadow-sm border border-slate-200 p-1.5 h-[52px]">
                <button class="w-8 h-full flex items-center justify-center text-slate-400 hover:text-[var(--accent)] hover:bg-slate-50 rounded-lg transition-all">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M15 19l-7-7 7-7"/></svg>
                </button>
                <div class="px-4 text-center border-x border-slate-100 h-full flex flex-col justify-center min-w-[120px]">
                    <div class="text-[10px] font-black text-slate-400 uppercase tracking-widest">Recent</div>
                    <div class="text-[14px] font-bold text-slate-700">-</div>
                </div>
                <button class="w-8 h-full flex items-center justify-center text-slate-400 hover:text-[var(--accent)] hover:bg-slate-50 rounded-lg transition-all">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

            <!-- New Button -->
            <button type="button" onclick="toggleModal('newGoodsReceiptModal')" class="px-8 py-3.5 bg-[var(--accent)] text-white rounded-xl text-[14px] font-black flex items-center gap-2 shadow-xl shadow-[var(--accent)]/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all uppercase tracking-widest">
                New Goods Receipt
            </button>
        </div>
    </div>

    <!-- Actions Row -->
    <div class="flex items-center justify-between mb-6 bg-white p-3 rounded-2xl shadow-sm border border-slate-200">
        <div class="flex items-center gap-2">
            <!-- Export Split Button -->
            <div class="relative flex items-center h-10 rounded-xl overflow-hidden group/export" style="box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.1);">
                <button onclick="toggleActionMenu(event, 'grExportFormMenu')" class="px-4 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all border-r border-white/20 flex items-center justify-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
                    <span class="text-[13px] font-bold uppercase tracking-wider">Export</span>
                </button>
                <!-- Export Form Dropdown (Left Click) -->
                <div id="grExportFormMenu" class="hidden absolute top-full right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-slate-100 p-5 z-[500]">
                    <div class="absolute -top-1.5 right-10 w-3 h-3 bg-white border-t border-l border-slate-100 rotate-45"></div>
                    <div class="space-y-4">
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Method</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>List</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[12px] font-bold text-slate-800">Export Type</label>
                            <div class="relative">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 pl-8 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] appearance-none">
                                    <option>PDF</option>
                                </select>
                                <svg class="w-4 h-4 text-slate-500 absolute left-3 top-3 pointer-events-none" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg>
                                <svg class="w-4 h-4 text-slate-500 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 pt-1">
                            <div class="relative w-1/2">
                                <select class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] font-medium text-slate-700 outline-none appearance-none">
                                    <option>This Fiscal Year</option>
                                </select>
                                <svg class="w-3.5 h-3.5 text-slate-500 absolute right-2 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                            </div>
                            <div class="flex items-center gap-1">
                                <span class="text-[12px] font-medium text-slate-600">Apr 1, 2026 - Mar 31, 2027</span>
                                <div class="flex flex-col">
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 14l5-5 5 5z"/></svg>
                                    <svg class="w-3 h-3 text-slate-400 cursor-pointer hover:text-slate-600" fill="currentColor" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-center gap-2 pt-4">
                            <button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Export</button>
                            <button class="px-6 py-2 bg-slate-700 text-white rounded font-bold text-[13px] hover:bg-slate-800 transition-all">Cancel</button>
                        </div>
                    </div>
                </div>

                <button onclick="toggleActionMenu(event, 'grExportMenu')" class="px-3 h-full bg-[var(--accent)] text-white hover:brightness-110 transition-all flex items-center justify-center">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
                </button>
                <div id="grExportMenu" class="hidden absolute top-full right-0 mt-2 w-48 bg-white rounded-2xl shadow-2xl border border-slate-100 py-2 z-[500]">
                    <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:text-[var(--accent)] hover:bg-blue-50/50 transition-all">
                        <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
                        Import XLS
                    </a>
                    <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-[13px] font-bold text-slate-600 hover:text-[var(--accent)] hover:bg-blue-50/50 transition-all">
                        <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                        Export XLS
                    </a>
                </div>
            </div>

            <!-- Filter Dropdown -->
            <div class="relative">
                <button onclick="toggleActionMenu(event, 'grFilterMenu')" class="w-10 h-10 flex items-center justify-center bg-[var(--accent)] text-white hover:brightness-110 rounded-xl transition-all shadow-sm">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg>
                </button>
                <div id="grFilterMenu" class="hidden absolute top-full left-0 mt-2 w-[400px] bg-white rounded-2xl shadow-2xl border border-slate-100 p-5 z-[500]">
                    <div class="flex items-center gap-2 mb-4">
                        <svg class="w-4 h-4 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg>
                        <h3 class="text-[14px] font-black text-slate-800">Advanced Filter</h3>
                    </div>
                    <div class="space-y-4">
                        <div>
                            <input type="text" placeholder="Contacts / Goods Receipt# / Ref# / Amount" class="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] focus:bg-white transition-all">
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div class="relative">
                                <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1.5 pl-1">Start Date</label>
                                <input type="text" placeholder="DD/MM/YYYY" class="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] focus:bg-white transition-all">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-[26px]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                            </div>
                            <div class="relative">
                                <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1.5 pl-1">End Date</label>
                                <input type="text" placeholder="DD/MM/YYYY" class="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] focus:bg-white transition-all">
                                <svg class="w-4 h-4 text-slate-400 absolute right-3 top-[26px]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                            </div>
                        </div>
                        <div class="flex gap-2 pt-2">
                            <button class="flex-1 py-3 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold hover:brightness-110 transition-all shadow-md shadow-[var(--accent)]/20">Search</button>
                            <button class="px-6 py-3 bg-slate-700 text-white rounded-xl text-[13px] font-bold hover:bg-slate-800 transition-all">Clear</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex items-center gap-4">
            <!-- Search -->
            <div class="relative group/search">
                <input type="text" placeholder="Search..." class="w-64 h-10 bg-slate-50 border border-slate-200 rounded-xl pl-10 pr-4 text-[13px] font-medium text-slate-700 outline-none focus:border-[var(--accent)] focus:bg-white focus:ring-4 focus:ring-[var(--accent)]/10 transition-all">
                <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-3 group-focus-within/search:text-[var(--accent)] transition-colors" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>

            <!-- Settings -->
            <div class="relative">
                <button onclick="toggleActionMenu(event, 'grSettingsMenu')" class="w-10 h-10 flex items-center justify-center bg-slate-700 text-white hover:bg-slate-800 rounded-xl transition-all shadow-sm">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                </button>
                <div id="grSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded shadow-xl border border-slate-200 p-4 z-[500]">
                    <div class="space-y-3">
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Ref.No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Due Days</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" checked class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Status</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" checked class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Due Amount</span>
                        </label>
                        
                        <div class="h-px bg-slate-200 my-2"></div>
                        
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Delivery Chalan No</span>
                        </label>
                        <label class="flex items-center gap-3 cursor-pointer">
                            <input type="checkbox" class="w-4 h-4 rounded-sm border-slate-300 text-[#008f8f] focus:ring-[#008f8f]">
                            <span class="text-[13px] font-semibold text-slate-800">Supplier Delivery Chalan Date</span>
                        </label>
                        
                        <div class="pt-2">
                            <button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Apply</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Table Section -->
    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="overflow-x-auto custom-scrollbar">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-slate-50/80 border-b border-slate-200">
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest whitespace-nowrap">Date</th>
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest whitespace-nowrap">Receipt No</th>
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest whitespace-nowrap">Contact</th>
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest whitespace-nowrap">Status</th>
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest text-right whitespace-nowrap">Amount</th>
                        <th class="px-5 py-4 text-[11px] font-black text-slate-500 uppercase tracking-widest text-center w-24">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                    <tr>
                        <td colspan="6">
                            <div class="py-20 flex flex-col items-center justify-center text-center">
                                <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mb-4 border border-slate-100 shadow-inner">
                                    <svg class="w-8 h-8 text-slate-300" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/></svg>
                                </div>
                                <h3 class="text-[16px] font-black text-slate-700 mb-1">No Records Found</h3>
                                <p class="text-[13px] font-medium text-slate-400 max-w-[250px]">There are no goods receipts available for the selected criteria.</p>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- New Goods Receipt Modal -->
    <!-- Fixing the Modal Header: primary color matching other modals -->
    <div id="newGoodsReceiptModal" class="hidden fixed inset-0 z-[1000] flex items-center justify-center">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" onclick="toggleModal('newGoodsReceiptModal')"></div>
        
        <!-- Modal Content -->
        <div class="relative bg-white w-[98vw] h-[95vh] rounded-xl shadow-2xl flex flex-col overflow-hidden">
            
            <!-- Modal Header (Primary Background) -->
            <div class="flex items-center justify-between px-6 py-4 bg-[var(--accent)] text-white border-b border-white/20">
                <div>
                    <h2 class="text-[18px] font-black tracking-tight">New Goods Receipt</h2>
                    <div class="flex items-center gap-1 text-[12px] opacity-90 font-medium">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                        Main Branch
                    </div>
                </div>
                
                <div class="flex items-center gap-3">
                    <!-- Save Split Button (White with Primary Border) -->
                    <div class="relative group/saveModal">
                        <div class="flex items-center bg-white text-[var(--accent)] rounded overflow-hidden h-[36px] shadow-sm border border-[var(--accent)]">
                            <button type="button" class="px-6 h-full text-[13px] font-bold hover:bg-slate-50 transition-all border-r border-[var(--accent)]">
                                Save
                            </button>
                            <button onclick="toggleActionMenu(event, 'saveGRMenu')" class="px-2 h-full hover:bg-slate-50 transition-all flex items-center justify-center">
                                <svg class="w-4 h-4 text-[var(--accent)]" fill="none" stroke="currentColor" stroke-width="4" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg>
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

                    <!-- Close X Button (Red) -->
                    <button type="button" onclick="toggleModal('newGoodsReceiptModal')" class="w-8 h-8 flex items-center justify-center bg-red-500 text-white hover:bg-red-600 rounded transition-all ml-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg>
                    </button>
                </div>
            </div>

            <!-- Modal Body (Scrollable) -->
            <div class="flex-1 overflow-y-auto bg-slate-50 p-6 custom-scrollbar">
                
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
                    
                    <!-- 3. Reference # -->
                    <div class="relative z-[500]">
                        <label class="flex items-center gap-1 text-[12px] font-bold text-slate-700 mb-1">
                            Reference #
                            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
                        </label>
                        <input type="text" placeholder="Purc.quote,Purc.order,Sup.credit" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[12px] text-slate-400 outline-none focus:border-[var(--accent)]">
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
                    
                    <!-- 6. Supplier Delivery Chalan Date + Gear Icon -->
                    <div class="flex items-end gap-2">
                        <div class="flex-1">
                            <label class="block text-[10px] text-slate-700 mb-1 leading-tight">Supplier Delivery Chalan Date</label>
                            <div class="relative">
                                <input type="text" placeholder="DD/MM/YYYY" class="w-full h-10 bg-white border border-slate-200 rounded px-3 text-[13px] font-bold outline-none focus:border-[var(--accent)]">
                                <svg class="w-4 h-4 text-slate-300 absolute right-3 top-3 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 002 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zM5 8V6h14v2H5z"/></svg>
                            </div>
                        </div>
                        
                        <!-- Settings Gear Icon moved here -->
                        <div class="relative pb-1">
                            <button onclick="toggleActionMenu(event, 'grRefSettingsMenu')" class="w-8 h-8 flex items-center justify-center bg-[var(--accent)] text-white hover:brightness-110 rounded transition-all shadow-md">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                            </button>
                            <div id="grRefSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-64 bg-white rounded shadow-xl p-4 z-[600] border border-slate-200">
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
                                    
                                    <button class="px-6 py-2 bg-[var(--accent)] text-white rounded font-bold text-[13px] hover:brightness-110 transition-all">Save</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Items Table -->
                <div class="border border-slate-200 bg-white rounded-xl shadow-sm mb-6 relative z-[300] overflow-hidden">
                    <table class="w-full text-left border-collapse">
                        <thead class="bg-[var(--accent)] text-white text-[12px] font-bold">
                            <tr>
                                <th class="px-4 py-3 w-12 border-r border-white/20">S.No</th>
                                <th class="px-4 py-3 border-r border-white/20 flex items-center justify-between">
                                    Item
                                    <div class="flex items-center gap-2">
                                        <input type="text" placeholder="Search..." class="h-6 w-32 px-2 text-[11px] rounded border-none text-slate-800 focus:outline-none">
                                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                                    </div>
                                </th>
                                <th class="px-4 py-3 w-24 border-r border-white/20 text-center">Qty</th>
                                <th class="px-4 py-3 w-24 border-r border-white/20 text-center">Unit</th>
                                <th class="px-4 py-3 w-32 border-r border-white/20 text-right">Rate ₹</th>
                                <th class="px-4 py-3 w-32 border-r border-white/20 text-right">Amount</th>
                                <th class="px-3 py-3 w-12 text-center relative z-[400]">
                                    <!-- Table Settings Dropdown -->
                                    <button onclick="toggleActionMenu(event, 'grTableSettingsMenu')" class="text-white hover:text-slate-200 transition-all">
                                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.06-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.73,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.06,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.43-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.49-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z"/></svg>
                                    </button>
                                    <div id="grTableSettingsMenu" class="hidden absolute top-full right-0 mt-2 w-56 bg-white rounded shadow-xl p-4 z-[600] border-2 border-[var(--accent)] text-left text-slate-800">
                                        <div class="absolute -top-1.5 right-2 w-3 h-3 bg-white border-t-2 border-l-2 border-[var(--accent)] rotate-45"></div>
                                        <div class="space-y-1.5 relative z-10 text-[12px]">
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
                                                <button class="px-5 py-1.5 bg-[var(--accent)] text-white rounded text-[12px] font-bold hover:brightness-110 transition-all">Save</button>
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
                                    <div class="flex items-center gap-2 border border-blue-400 rounded p-1.5 bg-white">
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
</div>

<script>
    function toggleModal(modalId) {
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

    function toggleActionMenu(event, menuId) {
        event.stopPropagation();
        
        // Close all other menus
        const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu', 'saveGRMenu', 'grRefSettingsMenu', 'grTableSettingsMenu'];
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
        const menus = ['grTitleDropdownMenu', 'grExportFormMenu', 'grExportMenu', 'grFilterMenu', 'grSettingsMenu', 'saveGRMenu', 'grRefSettingsMenu', 'grTableSettingsMenu'];
        menus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.classList.contains('hidden') && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    });
</script>
{% endblock %}
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("goods_receipt.html rewritten correctly.")
