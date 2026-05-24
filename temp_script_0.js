
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
        
        const allMenus = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'orderSettingsPopover', 'branchStockMenu',
            'itemSelectMenu_1', 'newSplitMenu', 'orderLinkContactDropdown', 'orderLinkCategoryDropdown',
            'rowActionMenu_ORD1', 'rowActionMenu_ORD2', 'rowActionMenu_ORD3', 'tableColMenu', 'viewModeMenu'
        ];
        allMenus.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        });

        if (wasHidden) {
            menu.classList.remove('hidden');

            if (menuId === 'tableColMenu' || menuId.startsWith('itemSelectMenu_')) {
                menu.style.position = 'fixed';
                const rect = event.currentTarget.getBoundingClientRect();
                menu.style.top = (rect.bottom + 4) + 'px';
                if (menuId === 'tableColMenu') {
                    menu.style.left = 'auto';
                    menu.style.right = (window.innerWidth - rect.right) + 'px';
                } else {
                    menu.style.left = rect.left + 'px';
                    menu.style.right = 'auto';
                }
                menu.style.zIndex = '99999';
            }
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
        document.getElementById('orderSettingsPopover').classList.add('hidden');
    }

    function filterGridItems() {
        const query = document.getElementById('gridItemSearch').value.toLowerCase();
        const rows = document.querySelectorAll('#orderGridBody tr');
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
        updateOrderTotals();
    }

    function updateOrderTotals() {
        let subtotal = 0;
        const qtyInput = document.getElementById('itemQty_1');
        const rateInput = document.getElementById('itemRate_1');
        const amountCell = document.getElementById('itemAmount_1');
        if (qtyInput && rateInput) {
            const qty = parseFloat(qtyInput.value) || 0;
            const rate = parseFloat(rateInput.value) || 0;
            const amount = qty * rate;
            if (amountCell) {
                amountCell.textContent = '₹ ' + amount.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
            }
            subtotal += amount;
        }
        document.getElementById('orderSubTotal').textContent = '₹ ' + subtotal.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        document.getElementById('orderTotalAmount').textContent = '₹ ' + subtotal.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function saveOrder() {
        alert('Order saved successfully!');
        closeModal();
    }

    function selectSaveOption(opt) {
        alert('Option selected: ' + opt);
        const menus = ['saveSplitMenu', 'saveFooterSplitMenu'];
        menus.forEach(id => {
            const m = document.getElementById(id);
            if (m) m.classList.add('hidden');
        });
    }

    function openQuickViewModal() {
        const modal = document.getElementById('quickViewModal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
        }
    }

    function closeQuickViewModal() {
        const modal = document.getElementById('quickViewModal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            selectViewMode('Normal View', true);
        }
    }

    function selectViewMode(mode, skipModal = false) {
        const icon = document.getElementById('viewModeIcon');
        if (icon) {
            if (mode === 'Normal View') {
                icon.innerHTML = `<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>`;
                if (!skipModal) {
                    const qvModal = document.getElementById('quickViewModal');
                    if (qvModal) {
                        qvModal.classList.add('hidden');
                        qvModal.classList.remove('flex');
                    }
                }
            } else if (mode === 'Quick View') {
                icon.innerHTML = `<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>`;
                if (!skipModal) {
                    openQuickViewModal();
                }
            }
        }
        const menu = document.getElementById('viewModeMenu');
        if (menu) menu.classList.add('hidden');
    }

    /* Status Filter */
    function filterByStatus(status) {
        const tbody = document.querySelector('tbody.divide-y');
        if (!tbody) return;
        const rows = tbody.querySelectorAll('tr');
        rows.forEach(row => {
            const rowStatus = row.getAttribute('data-status');
            if (status === 'All' || rowStatus === status) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    /* Order Link Modal Functions */
    function openOrderLinkModal() {
        const overlay = document.getElementById('orderLinkModalOverlay');
        if (overlay) {
            overlay.classList.remove('hidden');
            overlay.classList.add('flex');
        }
    }

    function closeOrderLinkModal() {
        const overlay = document.getElementById('orderLinkModalOverlay');
        if (overlay) {
            overlay.classList.remove('flex');
            overlay.classList.add('hidden');
        }
    }

    function selectOrderLinkContact(name) {
        document.getElementById('orderLinkContact').value = name;
        document.getElementById('orderLinkContactDropdown').classList.add('hidden');
    }

    function selectOrderLinkCategory(category) {
        document.getElementById('orderLinkCategory').value = category;
        document.getElementById('orderLinkCategoryDropdown').classList.add('hidden');
    }

    function saveOrderLink() {
        const name = document.getElementById('orderLinkName').value;
        const contact = document.getElementById('orderLinkContact').value;
        const category = document.getElementById('orderLinkCategory').value;
        
        if (!name || !contact) {
            alert('Please fill in Name and Contact fields.');
            return;
        }
        
        alert('Order Link saved successfully!\nName: ' + name + '\nContact: ' + contact + '\nCategory: ' + category);
        closeOrderLinkModal();
    }

    /* Apply Table Columns Settings */
    function applyTableSettings() {
        const showRef = document.getElementById('checkbox_Ref').checked;
        const showStatus = document.getElementById('checkbox_Status').checked;
        
        // Toggle Ref.No column (index 3 in header/rows)
        toggleTableColumn(3, showRef);
        
        // Toggle Status column (index 5 in header/rows)
        toggleTableColumn(5, showStatus);

        document.getElementById('settingsMenu').classList.add('hidden');
    }

    function toggleTableColumn(colIndex, show) {
        const table = document.querySelector('table');
        if (!table) return;
        
        // Toggle header cell
        const th = table.querySelectorAll('thead th')[colIndex];
        if (th) {
            th.style.display = show ? '' : 'none';
        }
        
        // Toggle body cells
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach(row => {
            const td = row.querySelectorAll('td')[colIndex];
            if (td) {
                td.style.display = show ? '' : 'none';
            }
        });
    }

    /* Row Action Dropdowns */
    function resetRowZIndex() {
        // Reset all table rows and action cells to default stacking
        document.querySelectorAll('tbody tr').forEach(row => {
            row.style.position = '';
            row.style.zIndex = '';
        });
        document.querySelectorAll('.action-cell').forEach(cell => {
            cell.style.zIndex = '';
        });
    }

    function toggleRowActionMenu(event, menuId) {
        event.stopPropagation();
        const menu = document.getElementById(menuId);
        if (!menu) return;
        const wasHidden = menu.classList.contains('hidden');
        
        // Close all dropdowns
        const allDropdowns = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'orderSettingsPopover', 'branchStockMenu',
            'itemSelectMenu_1', 'newSplitMenu', 'orderLinkContactDropdown', 'orderLinkCategoryDropdown',
            'rowActionMenu_ORD1', 'rowActionMenu_ORD2', 'rowActionMenu_ORD3'
        ];
        allDropdowns.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        });

        // Reset ALL row/cell z-indexes using inline styles (Tailwind dynamic classes don't work)
        resetRowZIndex();

        if (wasHidden) {
            menu.classList.remove('hidden');
            // Hoist this row and its action cell above sibling rows using inline styles
            const td = menu.closest('.action-cell');
            if (td) {
                td.style.zIndex = '9999';
            }
            const tr = menu.closest('tr');
            if (tr) {
                tr.style.position = 'relative';
                tr.style.zIndex = '9998';
            }
        }
    }

    const actionLabels = {
        'create_invoice': 'Create Invoice',
        'create_delivery_challan': 'Delivery Challan',
        'receipt': 'Receipt',
        'print': 'Print',
        'send': 'Send Email',
        'send_sms': 'SMS',
        'send_whatsapp': 'WhatsApp',
        'copy': 'Copy',
        'delete': 'Delete'
    };

    function handleRowAction(action, rowId) {
        // Update the button label to reflect the selected action
        const label = document.getElementById('actionLabel_' + rowId);
        if (label) {
            label.textContent = actionLabels[action] || action;
        }
        // Hide all action menus
        ['rowActionMenu_ORD1', 'rowActionMenu_ORD2', 'rowActionMenu_ORD3'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.add('hidden');
        });
        resetRowZIndex();
    }

    window.onclick = function(event) {
        const allMenus = [
            'exportMenu', 'filterMenu', 'settingsMenu', 'saveSplitMenu', 'saveFooterSplitMenu',
            'customerDropdownMenu', 'validTillMenu', 'orderSettingsPopover', 'branchStockMenu',
            'itemSelectMenu_1', 'newSplitMenu', 'orderLinkContactDropdown', 'orderLinkCategoryDropdown',
            'rowActionMenu_ORD1', 'rowActionMenu_ORD2', 'rowActionMenu_ORD3'
        ];
        allMenus.forEach(id => {
            const menu = document.getElementById(id);
            if (menu && !menu.contains(event.target)) {
                menu.classList.add('hidden');
            }
        });

        // Clean up inline z-index styles if no row action dropdown is visible
        setTimeout(() => {
            const anyRowMenuOpen = ['rowActionMenu_ORD1', 'rowActionMenu_ORD2', 'rowActionMenu_ORD3']
                .some(id => {
                    const el = document.getElementById(id);
                    return el && !el.classList.contains('hidden');
                });
            if (!anyRowMenuOpen) {
                resetRowZIndex();
            }
        }, 50);
    };

    window.addEventListener('keydown', function(e) {
        if (e.key === 'F9') {
            const overlay = document.getElementById('modalOverlay');
            if (overlay && !overlay.classList.contains('hidden')) {
                e.preventDefault();
                toggleActionMenu(e, 'customerDropdownMenu');
            }
        }
    });
