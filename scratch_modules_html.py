import re

def update_modules_settings():
    filepath = 'd:/AuraaZenAIProject/abproject/templates/modules_settings.html'
    with open(filepath, 'r') as f:
        content = f.read()

    # The grid starts at <div class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-[var(--surface)] border border-[var(--border)] rounded-2xl p-8 shadow-sm">
    grid_start_idx = content.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-6')
    grid_end_idx = content.find('<!-- Status Toast -->')

    # We'll replace everything between grid_start_idx and grid_end_idx with our dynamic loop

    new_grid = """<div class="bg-[var(--surface)] border border-[var(--border)] rounded-2xl p-8 shadow-sm">
        
        <!-- Modules Options Grid Layout -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-2">
            {% for module in modules_list %}
            <div class="flex items-center justify-between py-2 border-b border-[var(--border)]/40 hover:bg-slate-50/5 transition-colors px-2 rounded-lg {% if module.menu_type == 'submenu' %}pl-8 border-l-2 border-l-[var(--border)]{% endif %}">
                <div class="flex items-center gap-3">
                    <span class="text-[13px] font-bold text-[var(--text-primary)]">{{ module.module_name }}</span>
                    <!-- Edit Button -->
                    <button type="button" onclick="openEditModal({{ module.id }}, '{{ module.module_name|escapejs }}', '{{ module.route_path|default_if_none:""|escapejs }}', '{{ module.icon_name|default_if_none:""|escapejs }}')" class="text-slate-400 hover:text-[var(--accent)] transition-colors" title="Edit Module">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                    </button>
                </div>
                <label class="switch-container">
                    <input type="checkbox" onchange="toggleModuleStatus({{ module.id }}, this.checked)" {% if module.is_active %}checked{% endif %} class="switch-input">
                    <span class="switch-slider"><span class="on-txt hidden">ON</span><span class="off-txt">OFF</span></span>
                </label>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- Edit Module Modal -->
    <div id="editModuleModal" class="fixed inset-0 z-[100] hidden items-center justify-center">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm transition-opacity" onclick="closeEditModal()"></div>
        
        <!-- Modal Content -->
        <div class="relative bg-[var(--surface)] w-full max-w-md rounded-2xl shadow-2xl border border-[var(--border)] p-6 transform scale-95 transition-all">
            <h3 class="text-lg font-bold text-[var(--text-primary)] mb-4">Edit Module</h3>
            
            <form id="editModuleForm" onsubmit="saveModuleEdit(event)">
                <input type="hidden" id="editModuleId">
                
                <div class="space-y-4">
                    <div>
                        <label class="block text-[12px] font-semibold text-[var(--text-secondary)] mb-1">Module Name</label>
                        <input type="text" id="editModuleName" required class="w-full px-3 py-2 bg-transparent border border-[var(--border)] rounded-xl text-[13px] text-[var(--text-primary)] focus:border-[var(--accent)] focus:ring-1 focus:ring-[var(--accent)] outline-none transition-all">
                    </div>
                    
                    <div>
                        <label class="block text-[12px] font-semibold text-[var(--text-secondary)] mb-1">Route Path</label>
                        <input type="text" id="editModuleRoute" class="w-full px-3 py-2 bg-transparent border border-[var(--border)] rounded-xl text-[13px] text-[var(--text-primary)] focus:border-[var(--accent)] focus:ring-1 focus:ring-[var(--accent)] outline-none transition-all">
                    </div>

                    <div>
                        <label class="block text-[12px] font-semibold text-[var(--text-secondary)] mb-1">Icon Name</label>
                        <input type="text" id="editModuleIcon" class="w-full px-3 py-2 bg-transparent border border-[var(--border)] rounded-xl text-[13px] text-[var(--text-primary)] focus:border-[var(--accent)] focus:ring-1 focus:ring-[var(--accent)] outline-none transition-all">
                    </div>
                </div>

                <div class="mt-6 flex items-center justify-end gap-3">
                    <button type="button" onclick="closeEditModal()" class="px-4 py-2 rounded-xl text-[13px] font-semibold text-[var(--text-secondary)] hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Cancel</button>
                    <button type="submit" class="px-6 py-2 bg-[var(--accent)] hover:brightness-110 text-white rounded-xl text-[13px] font-extrabold transition-all shadow-md active:scale-[0.98]">Save Changes</button>
                </div>
            </form>
        </div>
    </div>
</div>

"""

    # We need to add Toastr CSS/JS. We'll add them to the top and bottom.
    head_addition = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
    <style>
        /* Toastr primary color override */
        #toast-container > div {
            background-color: var(--accent) !important;
            opacity: 1 !important;
            border-radius: 8px !important;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
        }
    </style>
"""

    script_addition = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
<script>
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": true,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "3000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };

    window.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.switch-input').forEach(input => {
            syncSwitchLabels(input);
        });
    });

    function syncSwitchLabels(input) {
        const slider = input.nextElementSibling;
        const onTxt = slider.querySelector('.on-txt');
        const offTxt = slider.querySelector('.off-txt');
        
        if (input.checked) {
            onTxt.classList.remove('hidden');
            offTxt.classList.add('hidden');
        } else {
            onTxt.classList.add('hidden');
            offTxt.classList.remove('hidden');
        }
    }

    function toggleModuleStatus(moduleId, isActive) {
        fetch("{% url 'modules-settings' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                action: 'toggle_status',
                module_id: moduleId,
                is_active: isActive
            })
        })
        .then(res => res.json())
        .then(data => {
            if(data.status === 'success') {
                toastr.success("Module status updated successfully!");
                // Sync the label visually
                const input = event.target;
                syncSwitchLabels(input);
            } else {
                toastr.error("Failed to update status: " + data.message);
            }
        })
        .catch(err => {
            toastr.error("An error occurred");
            console.error(err);
        });
    }

    // Modal logic
    function openEditModal(id, name, route, icon) {
        document.getElementById('editModuleId').value = id;
        document.getElementById('editModuleName').value = name;
        document.getElementById('editModuleRoute').value = route;
        document.getElementById('editModuleIcon').value = icon;
        
        const modal = document.getElementById('editModuleModal');
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        
        // Add a small delay for the animation
        setTimeout(() => {
            modal.querySelector('.transform').classList.remove('scale-95');
            modal.querySelector('.transform').classList.add('scale-100');
        }, 10);
    }

    function closeEditModal() {
        const modal = document.getElementById('editModuleModal');
        modal.querySelector('.transform').classList.remove('scale-100');
        modal.querySelector('.transform').classList.add('scale-95');
        
        setTimeout(() => {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
        }, 200);
    }

    function saveModuleEdit(e) {
        e.preventDefault();
        const id = document.getElementById('editModuleId').value;
        const name = document.getElementById('editModuleName').value;
        const route = document.getElementById('editModuleRoute').value;
        const icon = document.getElementById('editModuleIcon').value;

        fetch("{% url 'modules-settings' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                action: 'edit_module',
                module_id: id,
                module_name: name,
                route_path: route,
                icon_name: icon
            })
        })
        .then(res => res.json())
        .then(data => {
            if(data.status === 'success') {
                toastr.success("Module updated successfully!");
                closeEditModal();
                // Reload the page to reflect changes
                setTimeout(() => window.location.reload(), 1000);
            } else {
                toastr.error("Failed to update module: " + data.message);
            }
        })
        .catch(err => {
            toastr.error("An error occurred");
            console.error(err);
        });
    }
</script>
"""

    # We need to replace the scripts at the bottom
    # The bottom scripts start at {% block extra_js %}
    
    script_start_idx = content.find('{% block extra_js %}')
    script_end_idx = content.find('{% endblock %}', script_start_idx) + 14

    head_start_idx = content.find('{% block extra_head %}')
    
    new_content = content[:grid_start_idx] + new_grid + content[grid_end_idx:script_start_idx] + '{% block extra_js %}\n' + script_addition + '\n{% endblock %}\n'
    
    # insert head addition
    if head_start_idx != -1:
        insert_point = content.find('</style>', head_start_idx) + 8
        new_content = new_content[:insert_point] + head_addition + new_content[insert_point:]

    # Remove the old Save button since save happens via AJAX now, but we'll leave it or change it to just trigger a toast
    new_content = new_content.replace('onclick="saveModulesSettings()"', 'onclick="toastr.success(\'Changes saved successfully!\')"')

    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_modules_settings()
