function toggleNavGroup(el) {
    const sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('sidebar-collapsed')) {
        // Expand sidebar first
        sidebar.classList.remove('sidebar-collapsed');
        localStorage.setItem('sidebarState', 'expanded');
        // Give it a tiny delay to allow CSS transition to start before expanding the submenu
        setTimeout(() => {
            toggleNavGroupLogic(el);
        }, 150);
        return;
    }
    toggleNavGroupLogic(el);
}

function toggleNavGroupLogic(el) {
    const group = el.closest('.nav-group');
    const children = group.querySelector('.nav-children');
    const chevron = el.querySelector('.chevron');
    
    // Check current state
    const isCurrentlyClosed = children.classList.contains('max-h-0') || (children.style.maxHeight === '0px');
    
    if (isCurrentlyClosed) {
        // Open
        children.classList.remove('max-h-0');
        children.style.maxHeight = children.scrollHeight + 'px';
        chevron.classList.add('rotate-90');
    } else {
        // Close
        children.style.maxHeight = '0px';
        children.classList.add('max-h-0');
        chevron.classList.remove('rotate-90');
    }
}

function openModal(title) {
    const overlay = document.getElementById('modalOverlay');
    overlay.classList.remove('hidden');
    // Ensure Billing Address tab is selected by default
    setModalTab('Billing Address');
}

function closeModal() {
    const overlay = document.getElementById('modalOverlay');
    overlay.classList.add('hidden');
}

// Global interactions
document.addEventListener('DOMContentLoaded', () => {
    // Check for openModal URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('openModal')) {
        // Delay slightly to ensure everything is rendered
        setTimeout(() => {
            if (typeof openModal === 'function') {
                openModal();
            }
        }, 100);
    }

    // Close modal on escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    // Handle background click to close modal
    const overlay = document.getElementById('modalOverlay');
    if (overlay) {
        overlay.addEventListener('click', (e) => {
            if (e.target.id === 'modalOverlay') closeModal();
        });
    }
});

function setModalTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('.modal-tab').forEach(btn => {
        if (btn.getAttribute('data-tab') === tabName) {
            btn.classList.add('bg-white', 'text-[var(--accent)]', 'shadow-md');
            btn.classList.remove('text-white', 'hover:bg-white/10');
            btn.style.color = 'var(--accent)';
        } else {
            btn.classList.remove('bg-white', 'text-[var(--accent)]', 'shadow-md');
            btn.classList.add('text-white', 'hover:bg-white/10');
            btn.style.color = 'white';
        }
    });

    // Update panes - use consistent ID logic (remove spaces)
    const targetId = 'modalTab-' + tabName.replace(/\s+/g, '');
    document.querySelectorAll('.modal-pane').forEach(pane => {
        if (pane.id === targetId) {
            pane.style.display = 'block';
            pane.classList.remove('hidden');
        } else {
            pane.style.display = 'none';
            pane.classList.add('hidden');
        }
    });
}

function toggleHelpTooltip(el) {
    event.stopPropagation();
    const tooltip = el.nextElementSibling;
    const isHidden = tooltip.classList.contains('hidden');
    
    // Close all other help tooltips first
    document.querySelectorAll('.help-tooltip').forEach(t => t.classList.add('hidden'));
    
    if (isHidden) {
        tooltip.classList.remove('hidden');
    }
}

// Global click handler to close tooltips and menus
document.addEventListener('click', (e) => {
    // Close tooltips
    document.querySelectorAll('.help-tooltip').forEach(t => t.classList.add('hidden'));
    
    // Close header menu if clicking outside
    const headerMenu = document.getElementById('headerNavMenu');
    if (headerMenu && !headerMenu.parentElement.contains(e.target)) {
        headerMenu.classList.add('hidden');
    }

    // Close save dropdown if clicking outside
    const saveMenu = document.getElementById('saveDropdownMenu');
    if (saveMenu && !saveMenu.closest('#saveActionGroup')?.contains(e.target)) {
        saveMenu.classList.add('hidden');
    }
});

function toggleHeaderMenu(e) {
    if (e) e.stopPropagation();
    const menu = document.getElementById('headerNavMenu');
    if (menu) menu.classList.toggle('hidden');
}
