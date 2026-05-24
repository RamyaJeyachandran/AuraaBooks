
    function openModal(type) {
        document.getElementById('modalTitle').textContent = 'New ' + type;
        const overlay = document.getElementById('modalOverlay');
        overlay.classList.remove('hidden');
        overlay.classList.add('flex');
    }

    function closeModal() {
        const overlay = document.getElementById('modalOverlay');
        overlay.classList.remove('flex');
        overlay.classList.add('hidden');
    }

    function toggleActionMenu(event, menuId) {
        event.stopPropagation();
        const menu = document.getElementById(menuId);
        if (!menu) return;
        const wasHidden = menu.classList.contains('hidden');
        
        // Hide all active popup menus first
        const allMenus = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'quoteSettingsPopover',
            'itemSelectMenu_1', 'itemSelectMenu_2', 'newSplitMenu'
        ];
        allMenus.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        });

        if (wasHidden) {
            menu.classList.remove('hidden');
        }
    }

    function selectValidTill(val) {
        document.getElementById('validTillLabel').textContent = val;
        document.getElementById('validTillMenu').classList.add('hidden');
    }

    function selectCustomer(name) {
        document.getElementById('customerSearch').value = name;
        document.getElementById('customerDropdownMenu').classList.add('hidden');
    }

    function closeSettingsPopover() {
        document.getElementById('quoteSettingsPopover').classList.add('hidden');
    }

    function filterGridItems() {
        const query = document.getElementById('gridItemSearch').value.toLowerCase();
        const rows = document.querySelectorAll('#quoteGridBody tr');
        rows.forEach(row => {
            const input = row.querySelector('input[id^="itemName_"]');
            if (input) {
                const text = input.value.toLowerCase();
                if (text.includes(query) || query === '') {
                    row.classList.remove('hidden');
                } else {
                    row.classList.add('hidden');
                }
            }
        });
    }

    function selectGridItem(rowId, name, unit, rate) {
        document.getElementById('itemName_' + rowId).value = name;
        document.getElementById('itemUnit_' + rowId).textContent = unit;
        document.getElementById('itemRate_' + rowId).value = rate.toFixed(2);
        document.getElementById('itemSelectMenu_' + rowId).classList.add('hidden');
        updateQuoteTotals();
    }

    function applyCoupon() {
        const code = document.getElementById('couponCode').value.trim();
        const discInput = document.getElementById('couponDiscountVal');
        if (code.toLowerCase() === 'welcome10') {
            discInput.value = "10.00";
            discInput.classList.remove('text-slate-400');
            discInput.classList.add('text-rose-500');
        } else if (code === '') {
            discInput.value = "0.00";
            discInput.classList.add('text-slate-400');
            discInput.classList.remove('text-rose-500');
        }
        updateQuoteTotals();
    }

    function removeCoupon() {
        document.getElementById('couponCode').value = '';
        const discInput = document.getElementById('couponDiscountVal');
        discInput.value = "0.00";
        discInput.classList.add('text-slate-400');
        discInput.classList.remove('text-rose-500');
        updateQuoteTotals();
    }

    function updateQuoteTotals() {
        let subtotal = 0;
        for (let i = 1; i <= 2; i++) {
            const qtyInput = document.getElementById('itemQty_' + i);
            const rateInput = document.getElementById('itemRate_' + i);
            const amountCell = document.getElementById('itemAmount_' + i);
            if (qtyInput && rateInput) {
                const qty = parseFloat(qtyInput.value) || 0;
                const rate = parseFloat(rateInput.value) || 0;
                const amount = qty * rate;
                if (amountCell) {
                    amountCell.textContent = '₹ ' + amount.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                }
                subtotal += amount;
            }
        }
        
        const subTotalCell = document.getElementById('quoteSubTotal');
        if (subTotalCell) {
            subTotalCell.textContent = subtotal.toFixed(2);
        }

        const couponDisc = parseFloat(document.getElementById('couponDiscountVal').value) || 0;
        const packing = parseFloat(document.getElementById('packingCharges').value) || 0;
        const roundOff = parseFloat(document.getElementById('quoteRoundOff').value) || 0;

        const totalAmount = subtotal - couponDisc + packing + roundOff;
        
        const totalCell = document.getElementById('quoteTotalAmount');
        if (totalCell) {
            totalCell.textContent = '₹' + totalAmount.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        }
    }

    function saveQuote(opt) {
        const optionName = opt || 'Save';
        alert('Estimate saved successfully via: ' + optionName);
        closeModal();
    }

    function selectSaveOption(opt) {
        saveQuote(opt);
        const menus = ['saveSplitMenu', 'saveFooterSplitMenu'];
        menus.forEach(id => {
            const m = document.getElementById(id);
            if (m) m.classList.add('hidden');
        });
    }

    function printQuote() {
        alert('Estimate print process initiated!');
    }

    function closeSettingsPopover() {
        const popover = document.getElementById('quoteSettingsPopover');
        if (popover) popover.classList.add('hidden');
    }

    function closeGridSettingsPopover() {
        const popover = document.getElementById('gridSettingsPopover');
        if (popover) popover.classList.add('hidden');
    }

    function setViewMode(mode) {
        const btnIcon = document.getElementById('viewToggleIcon');
        const normalOpt = document.getElementById('viewNormalOption');
        const quickOpt = document.getElementById('viewQuickOption');
        
        if (mode === 'Normal') {
            btnIcon.textContent = '🏢';
            normalOpt.className = "w-full text-left px-4 py-2.5 text-[13px] font-black flex items-center gap-2.5 text-white bg-[#1e73be] transition-all cursor-pointer border-none outline-none";
            quickOpt.className = "w-full text-left px-4 py-2.5 text-[13px] font-bold flex items-center gap-2.5 text-slate-700 hover:bg-slate-50 transition-all cursor-pointer border-none bg-transparent outline-none";
            
            const quickOverlay = document.getElementById('quickQuoteModalOverlay');
            if (quickOverlay && !quickOverlay.classList.contains('hidden')) {
                switchToNormalMode();
            }
        } else {
            btnIcon.textContent = '🚀';
            quickOpt.className = "w-full text-left px-4 py-2.5 text-[13px] font-black flex items-center gap-2.5 text-white bg-[#1e73be] transition-all cursor-pointer border-none outline-none";
            normalOpt.className = "w-full text-left px-4 py-2.5 text-[13px] font-bold flex items-center gap-2.5 text-slate-700 hover:bg-slate-50 transition-all cursor-pointer border-none bg-transparent outline-none";
            
            const overlay = document.getElementById('modalOverlay');
            if (overlay && !overlay.classList.contains('hidden')) {
                switchToQuickMode();
            }
        }
        const menu = document.getElementById('viewSplitMenu');
        if (menu) menu.classList.add('hidden');
    }

    function switchToNormalMode() {
        const overlay = document.getElementById('modalOverlay');
        const quickOverlay = document.getElementById('quickQuoteModalOverlay');
        if (quickOverlay) {
            quickOverlay.classList.add('hidden');
            quickOverlay.classList.remove('flex');
        }
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
        }
        const btnIcon = document.getElementById('viewToggleIcon');
        if (btnIcon) btnIcon.textContent = '🏢';
    }

    function switchToQuickMode() {
        const overlay = document.getElementById('modalOverlay');
        const quickOverlay = document.getElementById('quickQuoteModalOverlay');
        if (overlay) {
            overlay.classList.add('hidden');
            overlay.classList.remove('flex');
        }
        if (quickOverlay) {
            quickOverlay.classList.remove('hidden');
            quickOverlay.classList.add('flex');
        }
        const btnIcon = document.getElementById('viewToggleIcon');
        if (btnIcon) btnIcon.textContent = '🚀';
    }

    function closeQuickModal() {
        const quickOverlay = document.getElementById('quickQuoteModalOverlay');
        if (quickOverlay) {
            quickOverlay.classList.add('hidden');
            quickOverlay.classList.remove('flex');
        }
    }

    function selectQuickSaveOption(opt) {
        alert('Estimate saved successfully via: ' + opt);
        closeQuickModal();
    }

    function setQuickSearchCategory(cat) {
        alert('Quick search category set to: ' + cat);
        const menu = document.getElementById('quickCustomerFilterMenu');
        if (menu) menu.classList.add('hidden');
    }

    window.onclick = function(event) {
        const allMenus = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'quoteSettingsPopover', 'gridSettingsPopover',
            'itemSelectMenu_1', 'itemSelectMenu_2', 'newSplitMenu', 'printSplitMenu', 'viewSplitMenu',
            'quickViewSplitMenu', 'quickSaveSplitMenu', 'quickSettingsPopover', 'quickCustomerFilterMenu',
            'premiumSaveSplitMenu', 'premiumFooterSaveSplitMenu', 'premiumEstimateTypeMenu', 
            'premiumValidTillMenu', 'premiumCustomerDropdownMenu', 'premiumSettingsPopover', 'premiumGridSettingsPopover'
        ];
        // Hide row item selector menus dynamically
        for (let i = 1; i <= premiumRowCount; i++) {
            allMenus.push('premiumItemSelectMenu_' + i);
        }

        allMenus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });
    };

    window.addEventListener('keydown', function(e) {
        if (e.key === 'F9') {
            const overlay = document.getElementById('modalOverlay');
            if (overlay && !overlay.classList.contains('hidden')) {
                e.preventDefault();
                toggleActionMenu(e, 'customerDropdownMenu');
                return;
            }
            const premiumOverlay = document.getElementById('premiumQuoteModalOverlay');
            if (premiumOverlay && !premiumOverlay.classList.contains('hidden')) {
                e.preventDefault();
                togglePremiumActionMenu(e, 'premiumCustomerDropdownMenu');
                return;
            }
        }
    });

    // --- Premium Quote Modal Functionality ---
    let premiumRowCount = 3;

    function openPremiumQuoteModal() {
        // Hide triggering split menu
        const splitMenu = document.getElementById('newSplitMenu');
        if (splitMenu) splitMenu.classList.add('hidden');

        const overlay = document.getElementById('premiumQuoteModalOverlay');
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
            updatePremiumQuoteTotals();
        }
    }

    function closePremiumQuoteModal() {
        const overlay = document.getElementById('premiumQuoteModalOverlay');
        if (overlay) {
            overlay.classList.add('hidden');
            overlay.classList.remove('flex');
        }
    }

    function togglePremiumActionMenu(event, menuId) {
        event.stopPropagation();
        const menu = document.getElementById(menuId);
        if (!menu) return;
        const wasHidden = menu.classList.contains('hidden');

        // Hide all active popup menus
        const allMenus = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'quoteSettingsPopover', 'gridSettingsPopover',
            'itemSelectMenu_1', 'itemSelectMenu_2', 'newSplitMenu', 'printSplitMenu', 'viewSplitMenu',
            'quickViewSplitMenu', 'quickSaveSplitMenu', 'quickSettingsPopover', 'quickCustomerFilterMenu',
            'premiumSaveSplitMenu', 'premiumFooterSaveSplitMenu', 'premiumEstimateTypeMenu', 
            'premiumValidTillMenu', 'premiumCustomerDropdownMenu', 'premiumSettingsPopover', 'premiumGridSettingsPopover'
        ];
        // Hide row item selector menus dynamically
        for (let i = 1; i <= premiumRowCount; i++) {
            allMenus.push('premiumItemSelectMenu_' + i);
        }

        allMenus.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        });

        if (wasHidden) {
            menu.classList.remove('hidden');
        }
    }

    function selectPremiumEstimateType(val) {
        const label = document.getElementById('premiumEstimateTypeLabel');
        if (label) label.textContent = val;

        const optDefault = document.getElementById('premiumOptTypeDefault');
        const optEstimate = document.getElementById('premiumOptTypeEstimate');
        if (optDefault && optEstimate) {
            if (val === 'Default') {
                optDefault.className = "w-full text-left px-4 py-2 text-[12px] font-bold text-white bg-accent border-none outline-none cursor-pointer";
                optEstimate.className = "w-full text-left px-4 py-2 text-[12px] font-bold text-slate-700 hover:bg-slate-50 border-none bg-transparent outline-none cursor-pointer";
            } else {
                optDefault.className = "w-full text-left px-4 py-2 text-[12px] font-bold text-slate-700 hover:bg-slate-50 border-none bg-transparent outline-none cursor-pointer";
                optEstimate.className = "w-full text-left px-4 py-2 text-[12px] font-bold text-white bg-accent border-none outline-none cursor-pointer";
            }
        }
        
        const menu = document.getElementById('premiumEstimateTypeMenu');
        if (menu) menu.classList.add('hidden');
    }

    function selectPremiumValidTill(val) {
        const label = document.getElementById('premiumValidTillLabel');
        if (label) label.textContent = val;
        
        // Calculate date logic based on selection if desired, or leave placeholder
        const dateInput = document.getElementById('premiumValidTillDate');
        if (dateInput) {
            const today = new Date();
            if (val === '7 Days') {
                today.setDate(today.getDate() + 7);
            } else if (val === '15 Days') {
                today.setDate(today.getDate() + 15);
            } else if (val === '30 Days') {
                today.setDate(today.getDate() + 30);
            }
            // Format DD/MM/YYYY
            const dd = String(today.getDate()).padStart(2, '0');
            const mm = String(today.getMonth() + 1).padStart(2, '0');
            const yyyy = today.getFullYear();
            dateInput.value = dd + '/' + mm + '/' + yyyy;
        }

        const menu = document.getElementById('premiumValidTillMenu');
        if (menu) menu.classList.add('hidden');
    }

    function selectPremiumCustomer(name) {
        const searchInput = document.getElementById('premiumCustomerSearch');
        if (searchInput) searchInput.value = name;

        const menu = document.getElementById('premiumCustomerDropdownMenu');
        if (menu) menu.classList.add('hidden');
    }

    function togglePremiumDiscountType(rowId) {
        const typeButton = document.getElementById('premiumItemDiscountType_' + rowId);
        if (typeButton) {
            if (typeButton.textContent.trim() === '%') {
                typeButton.textContent = '₹';
            } else {
                typeButton.textContent = '%';
            }
            updatePremiumQuoteTotals();
        }
    }

    // Pre-declare qty/rate flags to avoid reference errors when creating dynamic rows
    const isQtyHidden = false;
    const isRateHidden = false;

    function selectPremiumGridItem(rowId, name, unit, rate) {
        const nameInput = document.getElementById('premiumItemName_' + rowId);
        const unitDisplay = document.getElementById('premiumItemUnit_' + rowId);
        const rateInput = document.getElementById('premiumItemRate_' + rowId);
        
        if (nameInput) nameInput.value = name;
        if (unitDisplay) unitDisplay.textContent = unit;
        if (rateInput) rateInput.value = rate.toFixed(2);

        const menu = document.getElementById('premiumItemSelectMenu_' + rowId);
        if (menu) menu.classList.add('hidden');

        updatePremiumQuoteTotals();
    }

    function deletePremiumRow(rowId) {
        const row = document.getElementById('premiumRow_' + rowId);
        if (row) {
            row.remove();
            updatePremiumQuoteTotals();
        }
    }

    function addPremiumGridRow() {
        premiumRowCount++;
        const tbody = document.getElementById('premiumQuoteGridBody');
        if (!tbody) return;

        const tr = document.createElement('tr');
        tr.id = 'premiumRow_' + premiumRowCount;
        tr.className = 'hover:bg-slate-50/50 transition-all';
        
        // Check which columns are currently hidden/visible
        const isDescHidden = document.getElementById('premiumGridColDesc') ? !document.getElementById('premiumGridColDesc').checked : true;
        const isSkuHidden = document.getElementById('premiumGridColSku') ? !document.getElementById('premiumGridColSku').checked : true;
        const isHsnHidden = document.getElementById('premiumGridColHsn') ? !document.getElementById('premiumGridColHsn').checked : true;
        const isAccountHidden = document.getElementById('premiumGridColAccount') ? !document.getElementById('premiumGridColAccount').checked : true;
        const isTaxHidden = document.getElementById('premiumGridColTax') ? !document.getElementById('premiumGridColTax').checked : true;
        const isLocationHidden = document.getElementById('premiumGridColLocation') ? !document.getElementById('premiumGridColLocation').checked : true;
        const isUnitHidden = document.getElementById('premiumGridColUnit') ? !document.getElementById('premiumGridColUnit').checked : false;
        const isNetRateHidden = document.getElementById('premiumGridColNetRate') ? !document.getElementById('premiumGridColNetRate').checked : true;
        const isMrpHidden = document.getElementById('premiumGridColMrp') ? !document.getElementById('premiumGridColMrp').checked : true;
        const isDiscountHidden = document.getElementById('premiumGridColDiscount') ? !document.getElementById('premiumGridColDiscount').checked : false;
        const isDiscOverallHidden = document.getElementById('premiumGridColDiscOverall') ? !document.getElementById('premiumGridColDiscOverall').checked : true;
        const isSaleRateHidden = document.getElementById('premiumGridColSaleRate') ? !document.getElementById('premiumGridColSaleRate').checked : true;
        const isGroupHidden = document.getElementById('premiumGridColGroup') ? !document.getElementById('premiumGridColGroup').checked : true;
        const isCostHidden = document.getElementById('premiumGridColCost') ? !document.getElementById('premiumGridColCost').checked : true;
        const isProfitHidden = document.getElementById('premiumGridColProfit') ? !document.getElementById('premiumGridColProfit').checked : true;

        tr.innerHTML = `
            <td class="px-3 py-1.5 text-center text-[12px] font-bold text-slate-400 border-r border-slate-200/60 w-12">${premiumRowCount}</td>
            <td class="px-3 py-1.5 border-r border-slate-200/60 relative min-w-[250px]">
                <input type="text" id="premiumItemName_${premiumRowCount}" onclick="togglePremiumActionMenu(event, 'premiumItemSelectMenu_${premiumRowCount}')" placeholder="Select or type item" class="w-full bg-transparent text-[13px] font-bold text-slate-700 outline-none">
                <div id="premiumItemSelectMenu_${premiumRowCount}" class="hidden absolute top-full left-0 mt-1 w-72 bg-white rounded-xl shadow-xl border border-slate-200 py-1.5 z-[700]">
                    <div onclick="selectPremiumGridItem(${premiumRowCount}, 'Premium Paper Pack', 'Pack', 450.00)" class="px-4 py-2.5 text-[12.5px] font-bold text-slate-600 hover:bg-slate-50 cursor-pointer text-left">Premium Paper Pack (₹ 450.00)</div>
                    <div onclick="selectPremiumGridItem(${premiumRowCount}, 'Color Binder A4', 'PCS', 180.00)" class="px-4 py-2.5 text-[12.5px] font-bold text-slate-600 hover:bg-slate-50 cursor-pointer text-left">Color Binder A4 (₹ 180.00)</div>
                    <div onclick="selectPremiumGridItem(${premiumRowCount}, 'Standard Card Holder', 'Box', 1200.00)" class="px-4 py-2.5 text-[12.5px] font-bold text-slate-600 hover:bg-slate-50 cursor-pointer text-left">Standard Card Holder (₹ 1200.00)</div>
                </div>
                <div class="col-desc ${isDescHidden ? 'hidden' : ''} mt-1 border-t border-slate-100 pt-1">
                    <input type="text" id="premiumItemDesc_${premiumRowCount}" placeholder="Enter Item Description" class="w-full bg-transparent text-[11px] font-medium text-slate-500 outline-none">
                </div>
            </td>
            <td class="col-sku ${isSkuHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <input type="text" id="premiumItemSku_${premiumRowCount}" placeholder="SKU" class="w-full bg-transparent text-[12px] font-bold text-slate-700 outline-none">
            </td>
            <td class="col-hsn ${isHsnHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <input type="text" id="premiumItemHsn_${premiumRowCount}" placeholder="HSN/SAC" class="w-full bg-transparent text-[12px] font-bold text-slate-700 outline-none">
            </td>
            <td class="col-account ${isAccountHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-32">
                <select id="premiumItemAccount_${premiumRowCount}" class="w-full bg-transparent text-[12px] font-bold text-slate-700 outline-none">
                    <option>Sales Account</option>
                    <option>Other Income</option>
                </select>
            </td>
            <td class="col-tax ${isTaxHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <select id="premiumItemTax_${premiumRowCount}" onchange="updatePremiumQuoteTotals()" class="w-full bg-transparent text-[12px] font-bold text-slate-700 outline-none">
                    <option value="0">0% GST</option>
                    <option value="5">5% GST</option>
                    <option value="12">12% GST</option>
                    <option value="18" selected>18% GST</option>
                    <option value="28">28% GST</option>
                </select>
            </td>
            <td class="col-location ${isLocationHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-32">
                <select id="premiumItemLocation_${premiumRowCount}" class="w-full bg-transparent text-[12px] font-bold text-slate-700 outline-none">
                    <option>Main Warehouse</option>
                    <option>Branch Office</option>
                </select>
            </td>
            <td class="col-qty ${isQtyHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-20">
                <input type="number" id="premiumItemQty_${premiumRowCount}" oninput="updatePremiumQuoteTotals()" value="1" class="w-full bg-transparent text-[13px] font-bold text-slate-700 text-center outline-none">
            </td>
            <td class="col-unit ${isUnitHidden ? 'hidden' : ''} px-3 py-1.5 text-[12px] font-bold text-slate-600 border-r border-slate-200/60 w-20 text-center">
                <span id="premiumItemUnit_${premiumRowCount}">PCS</span>
            </td>
            <td class="col-rate ${isRateHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-28">
                <input type="number" id="premiumItemRate_${premiumRowCount}" oninput="updatePremiumQuoteTotals()" value="0.00" class="w-full bg-transparent text-[13px] font-bold text-slate-700 text-right outline-none">
            </td>
            <td class="col-netrate ${isNetRateHidden ? 'hidden' : ''} px-3 py-1.5 text-right text-[12px] font-bold text-slate-600 border-r border-slate-200/60 w-28">
                <span id="premiumItemNetRate_${premiumRowCount}">0.00</span>
            </td>
            <td class="col-mrp ${isMrpHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <input type="number" id="premiumItemMrp_${premiumRowCount}" value="0.00" class="w-full bg-transparent text-[12px] font-bold text-slate-700 text-right outline-none">
            </td>
            <td class="col-discount ${isDiscountHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-36">
                <div class="flex items-center border border-slate-200 rounded-lg overflow-hidden bg-slate-50 h-8">
                    <input type="number" id="premiumItemDiscount_${premiumRowCount}" oninput="updatePremiumQuoteTotals()" value="0" class="w-16 bg-transparent text-right text-[12px] font-bold text-slate-700 outline-none px-1">
                    <button type="button" id="premiumItemDiscountType_${premiumRowCount}" onclick="togglePremiumDiscountType(${premiumRowCount})" class="bg-slate-200 px-2 h-full text-[11px] font-black border-l border-slate-200 hover:bg-slate-300 transition-colors select-none cursor-pointer">%</button>
                </div>
            </td>
            <td class="col-disc-overall ${isDiscOverallHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <input type="number" id="premiumItemDiscOverall_${premiumRowCount}" oninput="updatePremiumQuoteTotals()" value="0" class="w-full bg-transparent text-[12px] font-bold text-slate-700 text-right outline-none">
            </td>
            <td class="col-salerate ${isSaleRateHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-28">
                <input type="number" id="premiumItemSaleRate_${premiumRowCount}" value="0.00" class="w-full bg-transparent text-[12px] font-bold text-slate-700 text-right outline-none">
            </td>
            <td class="col-group ${isGroupHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 text-center w-24">
                <input type="checkbox" id="premiumItemGroup_${premiumRowCount}" class="w-4 h-4 text-[#1cb054] border-slate-300 rounded focus:ring-[#1cb054]">
            </td>
            <td class="col-cost ${isCostHidden ? 'hidden' : ''} px-3 py-1.5 border-r border-slate-200/60 w-24">
                <input type="number" id="premiumItemCost_${premiumRowCount}" value="0.00" class="w-full bg-transparent text-[12px] font-bold text-slate-700 text-right outline-none">
            </td>
            <td class="col-profit ${isProfitHidden ? 'hidden' : ''} px-3 py-1.5 text-right text-[12px] font-bold text-slate-600 border-r border-slate-200/60 w-24">
                <span id="premiumItemProfit_${premiumRowCount}">0.00</span>
            </td>
            <td class="px-3 py-1.5 text-right text-[13px] font-black text-slate-700 w-36" id="premiumItemAmount_${premiumRowCount}">₹ 0.00</td>
            <td class="px-3 py-1.5 text-center border-l border-slate-200/60 w-12">
                <button type="button" onclick="deletePremiumRow(${premiumRowCount})" class="text-slate-300 hover:text-rose-500 transition-all font-black text-[16px] cursor-pointer">&times;</button>
            </td>
        `;
        
        tbody.appendChild(tr);
        updatePremiumQuoteTotals();
    }

    function updatePremiumQuoteTotals() {
        let subtotal = 0;
        const rows = document.querySelectorAll('#premiumQuoteGridBody tr');
        
        rows.forEach(row => {
            const rowId = row.id.split('_')[1];
            if (!rowId) return;

            const qtyEl = document.getElementById('premiumItemQty_' + rowId);
            const rateEl = document.getElementById('premiumItemRate_' + rowId);
            const discountEl = document.getElementById('premiumItemDiscount_' + rowId);
            const discTypeButton = document.getElementById('premiumItemDiscountType_' + rowId);
            const amountEl = document.getElementById('premiumItemAmount_' + rowId);

            // Optional columns calculation
            const taxSelect = document.getElementById('premiumItemTax_' + rowId);
            const netRateEl = document.getElementById('premiumItemNetRate_' + rowId);
            const discOverallEl = document.getElementById('premiumItemDiscOverall_' + rowId);
            const costEl = document.getElementById('premiumItemCost_' + rowId);
            const profitEl = document.getElementById('premiumItemProfit_' + rowId);

            if (qtyEl && rateEl) {
                const qty = parseFloat(qtyEl.value) || 0;
                const rate = parseFloat(rateEl.value) || 0;
                const baseAmount = qty * rate;

                let discountVal = 0;
                if (discountEl) {
                    discountVal = parseFloat(discountEl.value) || 0;
                }

                let discountAmt = 0;
                const isPercent = discTypeButton && discTypeButton.textContent.trim() === '%';
                if (isPercent) {
                    discountAmt = baseAmount * (discountVal / 100);
                } else {
                    discountAmt = discountVal;
                }

                // If Discount Overall is present and visible
                let discOverallVal = 0;
                if (discOverallEl && !discOverallEl.closest('td').classList.contains('hidden')) {
                    discOverallVal = parseFloat(discOverallEl.value) || 0;
                }
                const totalDiscount = discountAmt + discOverallVal;

                let netAmount = baseAmount - totalDiscount;
                if (netAmount < 0) netAmount = 0;

                // Net Rate column
                if (netRateEl) {
                    const netRate = qty > 0 ? (netAmount / qty) : 0;
                    netRateEl.textContent = netRate.toFixed(2);
                }

                // Profit column
                if (profitEl && costEl) {
                    const costVal = parseFloat(costEl.value) || 0;
                    const profitVal = netAmount - (costVal * qty);
                    profitEl.textContent = profitVal.toFixed(2);
                }

                // Tax calculation if tax is active
                let taxRate = 0;
                if (taxSelect && !taxSelect.closest('td').classList.contains('hidden')) {
                    taxRate = parseFloat(taxSelect.value) || 0;
                }
                const taxAmount = netAmount * (taxRate / 100);
                const finalRowAmt = netAmount + taxAmount;

                subtotal += netAmount;

                if (amountEl) {
                    amountEl.textContent = '₹ ' + finalRowAmt.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                }
            }
        });

        // Set subtotal
        const subtotalDisplay = document.getElementById('premiumQuoteSubTotal');
        if (subtotalDisplay) {
            subtotalDisplay.textContent = '₹ ' + subtotal.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        }

        // Additional Charges
        let freight = 0;
        const freightRow = document.getElementById('premiumTotalFreightRow');
        const freightInput = document.getElementById('premiumFreightCharges');
        if (freightRow && !freightRow.classList.contains('hidden') && freightInput) {
            freight = parseFloat(freightInput.value) || 0;
        }

        let packing = 0;
        const packingRow = document.getElementById('premiumTotalPackingRow');
        const packingInput = document.getElementById('premiumPackingCharges');
        if (packingRow && !packingRow.classList.contains('hidden') && packingInput) {
            packing = parseFloat(packingInput.value) || 0;
        }

        let insurance = 0;
        const insuranceRow = document.getElementById('premiumTotalInsuranceRow');
        const insuranceInput = document.getElementById('premiumInsuranceCharges');
        if (insuranceRow && !insuranceRow.classList.contains('hidden') && insuranceInput) {
            insurance = parseFloat(insuranceInput.value) || 0;
        }

        let tcs = 0;
        const tcsRow = document.getElementById('premiumTotalTCSRow');
        const tcsInput = document.getElementById('premiumTCSCharges');
        if (tcsRow && !tcsRow.classList.contains('hidden') && tcsInput) {
            tcs = parseFloat(tcsInput.value) || 0;
        }

        let roundoff = 0;
        const roundoffInput = document.getElementById('premiumQuoteRoundOff');
        if (roundoffInput) {
            roundoff = parseFloat(roundoffInput.value) || 0;
        }

        const totalAmount = subtotal + freight + packing + insurance + tcs + roundoff;

        const totalDisplay = document.getElementById('premiumQuoteTotalAmount');
        if (totalDisplay) {
            totalDisplay.textContent = '₹ ' + totalAmount.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        }
    }

    function togglePremiumGridColumn(colName) {
        const checkbox = document.getElementById('premiumGridCol' + colName.charAt(0).toUpperCase() + colName.slice(1));
        const show = checkbox ? checkbox.checked : false;
        
        const elements = document.querySelectorAll('.col-' + colName);
        elements.forEach(el => {
            if (show) {
                el.classList.remove('hidden');
            } else {
                el.classList.add('hidden');
            }
        });
        updatePremiumQuoteTotals();
    }

    function togglePremiumBuyerOrderRow() {
        const chk = document.getElementById('premiumSettingBuyerOrder');
        const row = document.getElementById('premiumBuyerOrderRow');
        if (row && chk) {
            if (chk.checked) {
                row.classList.remove('hidden');
            } else {
                row.classList.add('hidden');
            }
        }
    }

    function togglePremiumFreightRow() {
        const chk = document.getElementById('premiumSettingFreight');
        const row = document.getElementById('premiumTotalFreightRow');
        if (row && chk) {
            if (chk.checked) {
                row.classList.remove('hidden');
            } else {
                row.classList.add('hidden');
            }
            updatePremiumQuoteTotals();
        }
    }

    function togglePremiumPackingRow() {
        const chk = document.getElementById('premiumSettingPacking');
        const row = document.getElementById('premiumTotalPackingRow');
        if (row && chk) {
            if (chk.checked) {
                row.classList.remove('hidden');
            } else {
                row.classList.add('hidden');
            }
            updatePremiumQuoteTotals();
        }
    }

    function togglePremiumInsuranceRow() {
        const chk = document.getElementById('premiumSettingInsurance');
        const row = document.getElementById('premiumTotalInsuranceRow');
        if (row && chk) {
            if (chk.checked) {
                row.classList.remove('hidden');
            } else {
                row.classList.add('hidden');
            }
            updatePremiumQuoteTotals();
        }
    }

    function togglePremiumTCSRow() {
        const chk = document.getElementById('premiumSettingTCS');
        const row = document.getElementById('premiumTotalTCSRow');
        if (row && chk) {
            if (chk.checked) {
                row.classList.remove('hidden');
            } else {
                row.classList.add('hidden');
            }
            updatePremiumQuoteTotals();
        }
    }

    function togglePremiumReverseCharge() {
        const chk = document.getElementById('premiumSettingReverseCharge');
        const badge = document.getElementById('premiumReverseChargeBadge');
        if (badge && chk) {
            if (chk.checked) {
                badge.classList.remove('hidden');
            } else {
                badge.classList.add('hidden');
            }
        }
    }

    function closePremiumSettingsPopover() {
        const popover = document.getElementById('premiumSettingsPopover');
        if (popover) popover.classList.add('hidden');
    }

    function closePremiumGridSettingsPopover() {
        const popover = document.getElementById('premiumGridSettingsPopover');
        if (popover) popover.classList.add('hidden');
    }

    // --- Premium Quote Autocomplete & REST API Integration ---
    let premiumCustomers = [];
    let premiumItems = [];

    async function loadPremiumAutocompleteData() {
        try {
            const customerRes = await fetch('/api/customers/');
            if (customerRes.ok) {
                premiumCustomers = await customerRes.json();
                renderPremiumCustomerDropdown(premiumCustomers);
            }
            const itemRes = await fetch('/api/items/');
            if (itemRes.ok) {
                premiumItems = await itemRes.json();
                // Render item dropdowns for existing rows
                for (let i = 1; i <= premiumRowCount; i++) {
                    renderPremiumItemDropdown(i, premiumItems);
                }
            }
            
            // Generate sequence number
            const quotesRes = await fetch('/api/premium-quotes/');
            if (quotesRes.ok) {
                const quotes = await quotesRes.json();
                const nextNum = quotes.length + 1;
                document.getElementById('premiumEstimateNo').value = "PRE-EST-" + String(nextNum).padStart(3, '0');
            }
        } catch (err) {
            console.error("Failed to load autocomplete data:", err);
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function escapeHtml(str) {
        if (!str) return '';
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
    }

    function renderPremiumCustomerDropdown(customers) {
        const menu = document.getElementById('premiumCustomerDropdownMenu');
        if (!menu) return;
        
        let html = `<div class="px-5 py-2 text-[10px] font-black text-slate-400 uppercase tracking-widest border-b border-slate-100">Select Customer</div>`;
        if (customers.length === 0) {
            html += `<div class="px-5 py-3 text-[13px] font-bold text-slate-400 text-center">No customers found</div>`;
        } else {
            customers.forEach(c => {
                html += `<div onclick="selectPremiumCustomer(${c.id}, '${escapeHtml(c.name)}')" class="px-5 py-3 text-[13px] font-bold text-slate-700 hover:bg-slate-50 hover:text-accent cursor-pointer transition-all">${escapeHtml(c.name)}</div>`;
            });
        }
        menu.innerHTML = html;
    }

    function filterPremiumCustomers() {
        const query = document.getElementById('premiumCustomerSearch').value.toLowerCase();
        const filtered = premiumCustomers.filter(c => c.name.toLowerCase().includes(query));
        renderPremiumCustomerDropdown(filtered);
        // Show dropdown if not already visible
        const menu = document.getElementById('premiumCustomerDropdownMenu');
        if (menu) menu.classList.remove('hidden');
    }

    function selectPremiumCustomer(id, name) {
        const idInput = document.getElementById('premiumCustomerId');
        if (idInput) idInput.value = id;
        
        const searchInput = document.getElementById('premiumCustomerSearch');
        if (searchInput) searchInput.value = name;
        
        const menu = document.getElementById('premiumCustomerDropdownMenu');
        if (menu) menu.classList.add('hidden');
    }

    function renderPremiumItemDropdown(rowId, items) {
        const menu = document.getElementById(`premiumItemSelectMenu_${rowId}`);
        if (!menu) return;

        let html = '';
        if (items.length === 0) {
            html += `<div class="px-4 py-2.5 text-[12.5px] font-bold text-slate-400 text-center">No items found</div>`;
        } else {
            items.forEach(it => {
                html += `<div onclick="selectPremiumGridItem(${rowId}, '${escapeHtml(it.name)}', 'PCS', 0.00, '${escapeHtml(it.sku || '')}', '${escapeHtml(it.hsn || '')}')" class="px-4 py-2.5 text-[12.5px] font-bold text-slate-600 hover:bg-slate-50 cursor-pointer text-left">${escapeHtml(it.name)} (${it.sku || 'No SKU'})</div>`;
            });
        }
        menu.innerHTML = html;
    }

    function filterPremiumItems(rowId) {
        const query = document.getElementById(`premiumItemName_${rowId}`).value.toLowerCase();
        const filtered = premiumItems.filter(it => it.name.toLowerCase().includes(query) || (it.sku && it.sku.toLowerCase().includes(query)));
        renderPremiumItemDropdown(rowId, filtered);
        const menu = document.getElementById(`premiumItemSelectMenu_${rowId}`);
        if (menu) menu.classList.remove('hidden');
    }

    function selectPremiumGridItem(rowId, name, unit, rate, sku, hsn) {
        const nameInput = document.getElementById('premiumItemName_' + rowId);
        const unitDisplay = document.getElementById('premiumItemUnit_' + rowId);
        const rateInput = document.getElementById('premiumItemRate_' + rowId);
        const skuInput = document.getElementById('premiumItemSku_' + rowId);
        const hsnInput = document.getElementById('premiumItemHsn_' + rowId);
        
        if (nameInput) nameInput.value = name;
        if (unitDisplay) unitDisplay.textContent = unit || 'PCS';
        if (rateInput) rateInput.value = (rate || 0.00).toFixed(2);
        if (skuInput) skuInput.value = sku || '';
        if (hsnInput) hsnInput.value = hsn || '';

        const menu = document.getElementById('premiumItemSelectMenu_' + rowId);
        if (menu) menu.classList.add('hidden');

        updatePremiumQuoteTotals();
    }

    function showNotification(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `fixed bottom-5 right-5 z-[2000] flex items-center gap-3 px-5 py-3.5 rounded-2xl shadow-2xl border text-white transition-all transform translate-y-10 opacity-0 duration-300 ${
            type === 'success' 
                ? 'bg-emerald-500 border-emerald-400' 
                : 'bg-rose-500 border-rose-400'
        }`;
        
        const icon = type === 'success' ? '✓' : '✗';
        toast.innerHTML = `
            <span class="font-black text-[16px]">${icon}</span>
            <span class="text-[13px] font-black uppercase tracking-wider">${message}</span>
        `;
        
        document.body.appendChild(toast);
        
        // Trigger animation
        setTimeout(() => {
            toast.classList.remove('translate-y-10', 'opacity-0');
        }, 10);
        
        // Hide after 3 seconds
        setTimeout(() => {
            toast.classList.add('translate-y-10', 'opacity-0');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    function parseDateToISO(dateStr) {
        if (!dateStr) return null;
        const parts = dateStr.split('/');
        if (parts.length === 3) {
            const day = parts[0].padStart(2, '0');
            const month = parts[1].padStart(2, '0');
            const year = parts[2];
            return `${year}-${month}-${day}`;
        }
        if (dateStr.match(/^\d{4}-\d{2}-\d{2}$/)) {
            return dateStr;
        }
        return null;
    }

    async function savePremiumQuote(action) {
        // Validation
        const customerIdVal = document.getElementById('premiumCustomerId').value;
        const customerName = document.getElementById('premiumCustomerSearch').value;
        
        if (!customerIdVal || !customerName) {
            showNotification('Please select a valid Customer from the dropdown.', 'error');
            return;
        }

        // Validate items
        const itemRows = [];
        let validationError = null;

        for (let i = 1; i <= premiumRowCount; i++) {
            const nameInput = document.getElementById('premiumItemName_' + i);
            if (nameInput && nameInput.value.trim() !== '') {
                const qtyInput = document.getElementById('premiumItemQty_' + i);
                const rateInput = document.getElementById('premiumItemRate_' + i);
                const discInput = document.getElementById('premiumItemDiscount_' + i);
                const discTypeBtn = document.getElementById('premiumItemDiscountType_' + i);
                const skuInput = document.getElementById('premiumItemSku_' + i);
                const hsnInput = document.getElementById('premiumItemHsn_' + i);
                const descInput = document.getElementById('premiumItemDesc_' + i);
                const amtDisplay = document.getElementById('premiumItemAmount_' + i);

                const qty = parseFloat(qtyInput ? qtyInput.value : 0) || 0;
                const rate = parseFloat(rateInput ? rateInput.value : 0) || 0;
                const discountValue = parseFloat(discInput ? discInput.value : 0) || 0;
                const discountType = discTypeBtn ? discTypeBtn.textContent.trim() : '%';
                const sku = skuInput ? skuInput.value : '';
                const hsn = hsnInput ? hsnInput.value : '';
                const description = descInput ? descInput.value : '';
                const amount = parseFloat(amtDisplay ? amtDisplay.textContent.replace(/[^\d.-]/g, '') : 0) || 0;

                if (qty <= 0) {
                    validationError = `Row ${i}: Quantity must be greater than 0.`;
                    break;
                }
                if (rate < 0) {
                    validationError = `Row ${i}: Rate cannot be negative.`;
                    break;
                }
                if (discountType === '%' && discountValue > 100) {
                    validationError = `Row ${i}: Discount percentage cannot be greater than 100.`;
                    break;
                }

                itemRows.push({
                    item_name: nameInput.value.trim(),
                    qty: qty,
                    rate: rate,
                    discount_type: discountType,
                    discount_value: discountValue,
                    sku: sku,
                    hsn: hsn,
                    description: description,
                    amount: amount
                });
            }
        }

        if (validationError) {
            showNotification(validationError, 'error');
            return;
        }

        if (itemRows.length === 0) {
            showNotification('Please add at least one item to the quote.', 'error');
            return;
        }

        // Get totals
        const subTotalText = document.getElementById('premiumQuoteSubTotal').textContent.replace(/[^\d.-]/g, '');
        const totalText = document.getElementById('premiumQuoteTotalAmount').textContent.replace(/[^\d.-]/g, '');
        
        const subTotal = parseFloat(subTotalText) || 0;
        const totalAmount = parseFloat(totalText) || 0;

        const freightInput = document.getElementById('premiumFreightCharges');
        const packingInput = document.getElementById('premiumPackingCharges');
        const insuranceInput = document.getElementById('premiumInsuranceCharges');
        const tcsInput = document.getElementById('premiumTCSCharges');
        const roundOffInput = document.getElementById('premiumQuoteRoundOff');

        const freight = parseFloat(freightInput ? freightInput.value : 0) || 0;
        const packing = parseFloat(packingInput ? packingInput.value : 0) || 0;
        const insurance = parseFloat(insuranceInput ? insuranceInput.value : 0) || 0;
        const tcs = parseFloat(tcsInput ? tcsInput.value : 0) || 0;
        const roundOff = parseFloat(roundOffInput ? roundOffInput.value : 0) || 0;

        // Build Payload
        const payload = {
            estimate_no: document.getElementById('premiumEstimateNo').value,
            estimate_type: document.getElementById('premiumEstimateTypeLabel').textContent,
            estimate_date: parseDateToISO(document.getElementById('premiumEstimateDate').value),
            valid_till: parseDateToISO(document.getElementById('premiumValidTillDate').value),
            reference_no: document.getElementById('premiumReferenceNo').value || '',
            customer: parseInt(customerIdVal),
            buyer_order_no: document.getElementById('premiumBuyerOrderNo').value || '',
            buyer_order_date: parseDateToISO(document.getElementById('premiumBuyerOrderDate').value),
            section_name: document.getElementById('premiumSectionName').value || '',
            sub_total: subTotal,
            freight: freight,
            packing: packing,
            insurance: insurance,
            tcs: tcs,
            round_off: roundOff,
            total_amount: totalAmount,
            notes: document.getElementById('premiumNotes').value || '',
            terms: document.getElementById('premiumTerms').value || '',
            bank: document.getElementById('premiumBank').value || '',
            sales_rep: document.getElementById('premiumSalesRep').value || '',
            project: document.getElementById('premiumProject').value || '',
            items: itemRows
        };

        try {
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || getCookie('csrftoken') || '';
            const response = await fetch('/api/premium-quotes/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                showNotification('Premium Quote saved successfully!');
                setTimeout(() => {
                    window.location.reload();
                }, 1000);
            } else {
                const errData = await response.json();
                console.error("Save failure:", errData);
                showNotification('Failed to save Premium Quote. Check input fields.', 'error');
            }
        } catch (err) {
            console.error("Error saving:", err);
            showNotification('Server communication error.', 'error');
        }
    }

    function selectPremiumSaveOption(opt) {
        savePremiumQuote(opt);
    }

    function printPremiumQuote() {
        alert('Printing Premium Quote...');
    }
