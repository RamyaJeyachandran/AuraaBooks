import os

files = [
    r"d:\AuraaZenAIProject\abproject\templates\purchase_bill.html",
    r"d:\AuraaZenAIProject\abproject\templates\purchase_payment.html"
]

old_switch = """    function switchPbView(viewType) {
        document.getElementById('pbViewMenu').classList.add('hidden');
        
        const normalView = document.getElementById('pbNormalViewContent');
        const quickView = document.getElementById('pbQuickViewContent');
        
        const normalBtn = document.getElementById('pbViewNormalBtn');
        const quickBtn = document.getElementById('pbViewQuickBtn');
        
        // Reset buttons
        [normalBtn, quickBtn].forEach(btn => {
            if(btn) {
                btn.classList.remove('bg-[var(--accent)]', 'text-white');
                btn.classList.add('text-slate-600');
            }
        });
        
        if (viewType === 'Normal View') {
            if(normalView) {
                normalView.classList.remove('hidden');
                normalView.classList.add('flex-1');
            }
            if(quickView) {
                quickView.classList.add('hidden');
                quickView.classList.remove('flex-1');
            }
            if(normalBtn) {
                normalBtn.classList.add('bg-[var(--accent)]', 'text-white');
                normalBtn.classList.remove('text-slate-600');
            }
        } else if (viewType === 'Quick View') {
            if(normalView) {
                normalView.classList.add('hidden');
                normalView.classList.remove('flex-1');
            }
            if(quickView) {
                quickView.classList.remove('hidden');
                quickView.classList.add('flex-1');
            }
            if(quickBtn) {
                quickBtn.classList.add('bg-[var(--accent)]', 'text-white');
                quickBtn.classList.remove('text-slate-600');
            }
        }
    }"""

new_switch = """    function switchPbView(viewType) {
        document.getElementById('pbViewMenu').classList.add('hidden');
        
        const normalView = document.getElementById('pbNormalViewContent');
        const quickView = document.getElementById('pbQuickViewContent');
        
        const normalBtn = document.getElementById('pbViewNormalBtn');
        const quickBtn = document.getElementById('pbViewQuickBtn');
        
        // Reset buttons
        [normalBtn, quickBtn].forEach(btn => {
            if(btn) {
                btn.classList.remove('bg-[var(--accent)]', 'text-white');
                btn.classList.add('text-slate-600');
            }
        });
        
        if (viewType === 'Normal View') {
            if(normalView) {
                normalView.classList.remove('hidden');
                normalView.classList.add('flex', 'flex-1');
            }
            if(quickView) {
                quickView.classList.add('hidden');
                quickView.classList.remove('flex', 'flex-1');
            }
            if(normalBtn) {
                normalBtn.classList.add('bg-[var(--accent)]', 'text-white');
                normalBtn.classList.remove('text-slate-600');
            }
        } else if (viewType === 'Quick View') {
            if(normalView) {
                normalView.classList.add('hidden');
                normalView.classList.remove('flex', 'flex-1');
            }
            if(quickView) {
                quickView.classList.remove('hidden');
                quickView.classList.add('flex', 'flex-1');
            }
            if(quickBtn) {
                quickBtn.classList.add('bg-[var(--accent)]', 'text-white');
                quickBtn.classList.remove('text-slate-600');
            }
        }
    }"""

for html_file in files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply the replacement
    content = content.replace(old_switch, new_switch)
    
    # Also replace it directly in the element just in case it is rendered dynamically
    content = content.replace('id="pbQuickViewContent" class="hidden flex-1', 'id="pbQuickViewContent" class="hidden flex flex-1')
    content = content.replace('id="pbNormalViewContent" class="flex-1', 'id="pbNormalViewContent" class="flex flex-1')
    content = content.replace('id="pbNormalViewContent" class="flex flex-1', 'id="pbNormalViewContent" class="flex flex-1') # deduplicate
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated {html_file}")
