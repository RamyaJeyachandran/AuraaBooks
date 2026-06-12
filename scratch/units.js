        <form id="unitForm" onsubmit="event.preventDefault(); submitUnitForm();" class="p-6 space-y-5">
            <!-- Row 1: Name and Code -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-[12px] font-bold text-rose-500 mb-1.5">Unit Name *</label>
                    <input type="text" id="unitName" required placeholder="e.g. Box"
                           class="w-full h-10 px-3 border border-[var(--border)] rounded-xl bg-[var(--surface)] outline-none text-[13px] focus:border-accent">
                </div>
                <div>
                    <label class="block text-[12px] font-bold text-rose-500 mb-1.5">Code *</label>
                    <input type="text" id="unitCode" required placeholder="e.g. BOX"
                           class="w-full h-10 px-3 border border-[var(--border)] rounded-xl bg-[var(--surface)] outline-none text-[13px] focus:border-accent">
                </div>
            </div>

            <!-- Description -->
            <div>
                <label class="block text-[12px] font-bold text-[var(--text-secondary)] mb-1.5">Description</label>
                <textarea id="unitDescr" rows="2" class="w-full p-3 border border-[var(--border)] rounded-xl bg-[var(--surface)] outline-none text-[13px] focus:border-accent"></textarea>
            </div>

            <!-- Related Units Checkbox -->
            <div class="pt-2">
                <label class="flex items-center gap-2 cursor-pointer text-[13px] font-bold text-[var(--text-primary)]">
                    <input type="checkbox" id="hasRelatedUnits" onchange="toggleRelatedUnitsSection()" class="w-4 h-4 text-accent border-[var(--border)] rounded accent-[var(--accent)]">
                    <span>This unit has related units</span>
                </label>
            </div>

            <!-- Dynamic Related Units Container -->
            <div id="relatedUnitsContainer" class="hidden space-y-3 p-4 bg-[var(--bg)]/30 border border-[var(--border)] rounded-xl mt-3">
                <div class="flex items-center justify-between mb-2">
                    <h4 class="text-[12px] font-bold text-[var(--text-secondary)]">Related Units Configuration</h4>
                    <button type="button" onclick="addRelatedUnitRow()" class="px-3 py-1 bg-[var(--surface)] border border-[var(--border)] hover:bg-[var(--bg)] text-[var(--text-primary)] rounded text-[11px] font-bold transition-all shadow-sm cursor-pointer">
                        + Add Unit
                    </button>
                </div>
                
                <!-- Headers -->
                <div class="grid grid-cols-12 gap-2 px-1 pb-1 border-b border-[var(--border)] text-[11px] font-bold text-[var(--text-muted)] uppercase tracking-wider">
                    <div class="col-span-6">Related Unit</div>
                    <div class="col-span-5 text-center">Conversion Factor</div>
                    <div class="col-span-1 text-center"></div>
                </div>

                <div id="relatedUnitsList" class="space-y-2 max-h-[160px] overflow-y-auto no-scrollbar pb-1">
                    <!-- Rows injected here -->
                </div>
            </div>

            <!-- Footer Checkboxes & Actions -->
            <div class="pt-4 border-t border-[var(--border)] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div class="flex items-center gap-6">
                    <label class="flex items-center gap-2 cursor-pointer text-[12px] text-[var(--text-secondary)]">
                        <input type="checkbox" id="unitActive" checked class="w-4 h-4 text-accent border-[var(--border)] rounded accent-[var(--accent)]">
                        <span>Active</span>
                    </label>
                </div>

                <div class="flex items-center gap-2 self-end sm:self-auto">
                    <!-- Cancel button -->
                    <button type="button" onclick="closeUnitModal()" class="px-4 py-2 bg-slate-700 hover:bg-slate-800 text-white rounded-lg text-[12px] font-bold transition-all active:scale-[0.98] cursor-pointer">
                        Cancel
                    </button>
                    <!-- Save button -->
                    <button type="submit" class="px-4 py-2 bg-[var(--accent)] hover:brightness-110 text-white rounded-lg text-[12px] font-bold transition-all active:scale-[0.98] cursor-pointer">
                        Save
                    </button>
                </div>
            </div>
        </form>
    </div>
</div>

<!-- Delete Confirmation Modal -->
<div id="deleteConfirmModal" class="hidden fixed inset-0 z-[60] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
    <div class="bg-[var(--surface)] border border-[var(--border)] rounded-2xl shadow-xl w-full max-w-sm p-6 text-center">
        <div class="w-12 h-12 rounded-full bg-rose-100 text-rose-500 mx-auto flex items-center justify-center mb-4">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
        </div>
        <h3 class="text-[16px] font-extrabold text-[var(--text-primary)] mb-2">Delete Unit?</h3>
        <p class="text-[13px] text-[var(--text-muted)] mb-6">Are you sure you want to delete this unit? This action cannot be undone.</p>
        <div class="flex gap-3 justify-center">
            <button onclick="closeDeleteModal()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[13px] font-bold transition-all cursor-pointer">Cancel</button>
            <button onclick="confirmDelete()" class="px-4 py-2 bg-rose-500 hover:bg-rose-600 text-white rounded-lg text-[13px] font-bold transition-all cursor-pointer">Delete</button>
        </div>
    </div>
</div>

<!-- Global Loading Overlay -->
<div id="globalLoader" class="hidden fixed inset-0 z-[9999] bg-slate-900/40 backdrop-blur-sm flex items-center justify-center">
    <div class="bg-white px-6 py-4 rounded-xl shadow-2xl flex items-center gap-4">
        <div class="w-6 h-6 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
        <span class="text-sm font-bold text-slate-700">Processing...</span>
    </div>
</div>

<!-- Toast notifications -->
<div id="unitToast" class="fixed bottom-6 right-6 z-[9999] flex items-center gap-3 px-5 py-3.5 bg-slate-900 text-white rounded-xl shadow-2xl opacity-0 translate-y-4 pointer-events-none transition-all duration-300">
    <div id="unitToastIcon" class="flex items-center justify-center">
        <div class="w-4 h-4 border-2 border-white/20 border-t-white rounded-full animate-spin"></div>
    </div>
    <span id="unitToastText" class="text-[13px] font-semibold tracking-wide"></span>
</div>
{% endblock %}

{% block extra_js %}
<script>
    let unitsList = {{ units_data|safe|default:"[]" }};
    let currentEditingUnitId = null;
    let unitToDelete = null;

    window.addEventListener('DOMContentLoaded', () => {
        renderUnitsTable();
    });

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
    const csrftoken = getCookie('csrftoken');

    function renderUnitsTable() {
        const tbody = document.getElementById('unitsGridBody');
        tbody.innerHTML = '';

        unitsList.forEach(u => {
            const tr = document.createElement('tr');
            tr.className = 'hover:bg-[var(--bg)]/20 transition-colors duration-150 align-middle';

            const activeText = u.isActive ? 'Active' : 'Inactive';
            const activeColor = u.isActive ? 'text-emerald-500' : 'text-slate-400';

            tr.innerHTML = `
                <td class="px-6 py-4 border border-[var(--border)] font-bold text-[var(--text-secondary)]">${u.name} (${u.code})</td>
                <td class="px-6 py-4 border border-[var(--border)] text-[var(--text-muted)]">${u.descr || '-'}</td>
                <td class="px-6 py-4 border border-[var(--border)] text-center ${activeColor} font-bold">${activeText}</td>
                <td class="px-6 py-4 border border-[var(--border)] text-center">
                    <div class="inline-flex items-center justify-center gap-3">
                        <button onclick="editUnit(${u.id})" class="text-[var(--accent)] hover:brightness-110 cursor-pointer" title="Edit">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.89 1.14l-2.812.938.938-2.812a4.5 4.5 0 011.14-1.89l12.654-12.653z"/></svg>
                        </button>
                        <button onclick="deleteUnit(${u.id})" class="text-rose-500 hover:brightness-110 cursor-pointer" title="Delete">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"/></svg>
                        </button>
                    </div>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    // Modal Handling
    function openUnitModal(id = null) {
        currentEditingUnitId = id;
        const modal = document.getElementById('unitModalOverlay');
        const form = document.getElementById('unitForm');
        form.reset();
        
        document.getElementById('relatedUnitsList').innerHTML = '';
        document.getElementById('hasRelatedUnits').checked = false;
        toggleRelatedUnitsSection();

        if (id) {
            document.getElementById('modalTitle').innerText = 'Edit Unit Details';
            const u = unitsList.find(x => x.id === id);
            document.getElementById('unitName').value = u.name;
            document.getElementById('unitCode').value = u.code;
            document.getElementById('unitDescr').value = u.descr || '';
            document.getElementById('unitActive').checked = u.isActive;
            
            if (u.relatedUnits && u.relatedUnits.length > 0) {
                document.getElementById('hasRelatedUnits').checked = true;
                toggleRelatedUnitsSection();
                u.relatedUnits.forEach(ru => {
                    addRelatedUnitRow(ru.relatedUnitId, ru.convFactor);
                });
            }
        } else {
            document.getElementById('modalTitle').innerText = 'New Unit';
            document.getElementById('unitActive').checked = true;
            addRelatedUnitRow(); // Add one empty row by default
        }

        modal.classList.remove('hidden');
    }

    function closeUnitModal() {
        document.getElementById('unitModalOverlay').classList.add('hidden');
    }

    function toggleRelatedUnitsSection() {
        const isChecked = document.getElementById('hasRelatedUnits').checked;
        const container = document.getElementById('relatedUnitsContainer');
        if (isChecked) {
            container.classList.remove('hidden');
            if (document.getElementById('relatedUnitsList').children.length === 0) {
                addRelatedUnitRow();
            }
        } else {
            container.classList.add('hidden');
        }
    }

    function addRelatedUnitRow(relatedUnitId = '', convFactor = '') {
        const list = document.getElementById('relatedUnitsList');
        const rowId = 'ru_row_' + Date.now() + Math.random().toString(36).substr(2, 5);
        
        // Build dropdown options
        let optionsHtml = '<option value="">Select Unit</option>';
        unitsList.forEach(u => {
            if (u.isActive && u.id !== currentEditingUnitId) {
                const selected = (u.id.toString() === relatedUnitId.toString()) ? 'selected' : '';
                optionsHtml += \`<option value="\${u.id}" \${selected}>\${u.name} (\${u.code})</option>\`;
            }
        });

        const row = document.createElement('div');
        row.id = rowId;
        row.className = 'grid grid-cols-12 gap-2 items-center';
        
        row.innerHTML = \`
            <div class="col-span-6">
                <select class="ru-select w-full h-9 px-2 border border-[var(--border)] rounded bg-[var(--surface)] text-[12px] outline-none focus:border-accent" required>
                    \${optionsHtml}
                </select>
            </div>
            <div class="col-span-5 flex items-center justify-center gap-2">
                <span class="text-[12px] font-bold text-[var(--text-secondary)]">=</span>
                <input type="number" step="0.000001" min="0.000001" class="ru-factor w-full h-9 px-2 border border-[var(--border)] rounded bg-[var(--surface)] text-[12px] outline-none focus:border-accent text-center" value="\${convFactor}" placeholder="Factor" required>
            </div>
            <div class="col-span-1 flex justify-center">
                <button type="button" onclick="removeRelatedUnitRow('\${rowId}')" class="p-1.5 text-rose-500 hover:bg-rose-50 rounded transition-colors cursor-pointer" title="Remove">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
        \`;
        list.appendChild(row);
    }

    function removeRelatedUnitRow(rowId) {
        document.getElementById(rowId).remove();
    }

    function deleteUnit(id) {
        unitToDelete = id;
        document.getElementById('deleteConfirmModal').classList.remove('hidden');
    }
    
    function closeDeleteModal() {
        document.getElementById('deleteConfirmModal').classList.add('hidden');
        unitToDelete = null;
    }

    async function confirmDelete() {
        if (!unitToDelete) return;
        closeDeleteModal();
        showLoader();

        try {
            const res = await fetch("{% url 'units-settings' %}", {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
                body: JSON.stringify({ action: 'delete_unit', id: unitToDelete })
            });
            const data = await res.json();
            hideLoader();
            if (data.status === 'success') {
                unitsList = unitsList.filter(u => u.id !== unitToDelete);
                renderUnitsTable();
                showToast(data.message, false);
            } else {
                showToast(data.message, false, true);
            }
        } catch (err) {
            hideLoader();
            showToast('Error deleting unit.', false, true);
        }
        hideToast();
    }

    async function submitUnitForm() {
        const name = document.getElementById('unitName').value.trim();
        const code = document.getElementById('unitCode').value.trim();
        const descr = document.getElementById('unitDescr').value.trim();
        const isActive = document.getElementById('unitActive').checked;
        const hasRelatedUnits = document.getElementById('hasRelatedUnits').checked;

        let relatedUnits = [];
        if (hasRelatedUnits) {
            const rows = document.getElementById('relatedUnitsList').children;
            for (let row of rows) {
                const select = row.querySelector('.ru-select').value;
                const factor = row.querySelector('.ru-factor').value;
                if (select && factor) {
                    relatedUnits.push({
                        relatedUnitId: parseInt(select),
                        convFactor: parseFloat(factor)
                    });
                }
            }
        }

        const payload = {
            action: 'save_unit',
            id: currentEditingUnitId,
            name: name,
            code: code,
            descr: descr,
            isActive: isActive,
            relatedUnits: relatedUnits
        };

        showLoader();
        try {
            const res = await fetch("{% url 'units-settings' %}", {
                method: "POST",
                headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            hideLoader();
            
            if (data.status === 'success') {
                showToast(data.message, false);
                setTimeout(() => window.location.reload(), 1000);
            } else {
                showToast(data.message, false, true);
                hideToast();
            }
        } catch (err) {
            hideLoader();
            showToast('An error occurred while saving.', false, true);
            hideToast();
        }
    }

    // Loader & Toast helpers
    function showLoader() { document.getElementById('globalLoader').classList.remove('hidden'); }
    function hideLoader() { document.getElementById('globalLoader').classList.add('hidden'); }

    let unitToastTimeout = null;
    function showToast(text, isLoader = true, isError = false) {
        const toast = document.getElementById('unitToast');
        const toastText = document.getElementById('unitToastText');
        const toastIcon = document.getElementById('unitToastIcon');

        if (unitToastTimeout) clearTimeout(unitToastTimeout);

        if (isLoader) {
            toastIcon.innerHTML = '<div class="w-4 h-4 border-2 border-white/20 border-t-white rounded-full animate-spin"></div>';
            toast.classList.remove('bg-rose-500');
            toast.classList.add('bg-slate-900');
        } else if (isError) {
            toastIcon.innerHTML = '<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12"/></svg>';
            toast.classList.remove('bg-slate-900');
            toast.classList.add('bg-rose-500');
        } else {
            toastIcon.innerHTML = '<svg class="w-4.5 h-4.5 text-emerald-400" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>';
            toast.classList.remove('bg-rose-500');
            toast.classList.add('bg-slate-900');
        }

        toastText.innerText = text;
        toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
        toast.classList.add('opacity-100', 'translate-y-0');
    }

    function hideToast(delay = 1500) {
        const toast = document.getElementById('unitToast');
        unitToastTimeout = setTimeout(() => {
            toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
            toast.classList.remove('opacity-100', 'translate-y-0');
        }, delay);
    }
</script>
{% endblock %}
