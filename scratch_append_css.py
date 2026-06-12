import os

css_to_append = """
/* ============================================================
   PREMIUM SIDEBAR REDESIGN — AuraaBooks 2026
   ============================================================ */

/* Sidebar glow container */
.sidebar-premium {
    background: linear-gradient(180deg, #4D93FF 0%, #2F6DDA 100%) !important;
    box-shadow:
        4px 0 40px rgba(30, 80, 200, 0.28),
        inset -1px 0 0 rgba(255,255,255,0.15);
    position: relative;
}

/* Sidebar top-left glass reflection */
.sidebar-premium .sb-glass-reflect {
    position: absolute;
    inset: 0;
    background: linear-gradient(140deg, rgba(255,255,255,0.1) 0%, transparent 55%);
    pointer-events: none;
    z-index: 0;
}

/* Sidebar right-edge highlight line */
.sidebar-premium .sb-edge-line {
    position: absolute;
    inset-block: 0;
    right: 0;
    width: 1px;
    background: linear-gradient(180deg, rgba(255,255,255,0.28) 0%, rgba(255,255,255,0.04) 100%);
    pointer-events: none;
    z-index: 0;
}

/* ── Nav item / nav parent base ── */
.nav-item,
.nav-parent {
    border-radius: 12px;
    transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
    position: relative;
    overflow: hidden;
}

/* ── Hover state ── */
.nav-item:hover,
.nav-parent:hover {
    background: rgba(255,255,255,0.12) !important;
    transform: translateY(-1px);
    box-shadow:
        0 4px 18px rgba(0,0,0,0.12),
        inset 0 1px 0 rgba(255,255,255,0.2);
}

.nav-item:hover .nav-icon,
.nav-parent:hover .nav-icon {
    background: rgba(255,255,255,0.22) !important;
    box-shadow: 0 0 12px rgba(255,255,255,0.15);
    transform: scale(1.06) rotate(2deg);
}

/* ── Active nav-item ── */
.nav-item.active {
    background: rgba(255,255,255,0.18) !important;
    border: 1px solid rgba(255,255,255,0.28) !important;
    border-radius: 14px !important;
    box-shadow:
        0 8px 28px rgba(0,0,0,0.18),
        inset 0 1px 0 rgba(255,255,255,0.32),
        inset 0 -1px 0 rgba(0,0,0,0.04);
    transform: translateY(-1px);
    font-weight: 700;
}

.nav-item.active .nav-icon {
    background: rgba(255,255,255,0.28) !important;
    box-shadow: 0 0 14px rgba(255,255,255,0.22);
}

/* Glowing animated left bar on active */
.nav-item.active::before {
    content: '';
    position: absolute;
    left: 0;
    top: 22%;
    bottom: 22%;
    width: 3px;
    background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.65) 100%);
    border-radius: 0 3px 3px 0;
    box-shadow: 0 0 10px rgba(255,255,255,0.9), 0 0 22px rgba(255,255,255,0.45);
    animation: nav-bar-pulse 2.2s ease-in-out infinite;
}

/* Subtle shine sweep overlay on active */
.nav-item.active::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        108deg,
        transparent 30%,
        rgba(255,255,255,0.06) 50%,
        transparent 70%
    );
    pointer-events: none;
}

/* ── Active nav-parent ── */
.nav-parent.active-parent {
    background: rgba(255,255,255,0.18) !important;
    border: 1px solid rgba(255,255,255,0.28) !important;
    border-radius: 14px !important;
    box-shadow:
        0 8px 28px rgba(0,0,0,0.18),
        inset 0 1px 0 rgba(255,255,255,0.32);
    transform: translateY(-1px);
    font-weight: 700;
}

.nav-parent.active-parent::before {
    content: '';
    position: absolute;
    left: 0;
    top: 22%;
    bottom: 22%;
    width: 3px;
    background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.65) 100%);
    border-radius: 0 3px 3px 0;
    box-shadow: 0 0 10px rgba(255,255,255,0.9), 0 0 22px rgba(255,255,255,0.45);
    animation: nav-bar-pulse 2.2s ease-in-out infinite;
}

/* ── Nav Icon Container ── */
.nav-icon {
    width: 30px !important;
    height: 30px !important;
    min-width: 30px !important;
    border-radius: 9px !important;
    background: rgba(255,255,255,0.13) !important;
    transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* ── Active child submenu item ── */
.active-child {
    color: white !important;
    background: rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.12) !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    transform: none !important;
    position: relative;
}

.active-child::before {
    content: '';
    position: absolute;
    left: 0;
    top: 25%;
    bottom: 25%;
    width: 2px;
    background: white;
    border-radius: 0 2px 2px 0;
    box-shadow: 0 0 7px rgba(255,255,255,0.85);
}

/* ── Submenu child links ── */
.nav-children a {
    transition: all 0.18s ease-out;
    opacity: 0.8;
}

.nav-children a:hover {
    opacity: 1;
    background: rgba(255,255,255,0.1) !important;
    transform: translateX(2px);
}

/* ── Chevron smooth rotation ── */
.chevron {
    transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    opacity: 0.65;
}

/* ── Sidebar logo avatar ── */
.sidebar-logo-avatar {
    background: linear-gradient(135deg, rgba(255,255,255,0.38) 0%, rgba(255,255,255,0.14) 100%);
    border: 1px solid rgba(255,255,255,0.45);
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.14), inset 0 1px 0 rgba(255,255,255,0.5);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.sidebar-logo-avatar:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 24px rgba(0,0,0,0.2), 0 0 20px rgba(255,255,255,0.2);
}

/* ── Sidebar user card ── */
.sidebar-user-card {
    background: rgba(0,0,0,0.13);
    border-top: 1px solid rgba(255,255,255,0.12);
    transition: background 0.2s ease;
}

.sidebar-user-card:hover {
    background: rgba(0,0,0,0.2);
}

.sidebar-user-avatar {
    background: linear-gradient(135deg, rgba(255,255,255,0.32) 0%, rgba(255,255,255,0.14) 100%);
    border: 1px solid rgba(255,255,255,0.32);
    box-shadow: 0 2px 8px rgba(0,0,0,0.14);
    transition: box-shadow 0.25s ease;
}

.sidebar-user-avatar:hover {
    box-shadow: 0 0 18px rgba(255,255,255,0.22);
}

/* ============================================================
   PREMIUM TOPBAR REDESIGN — AuraaBooks 2026
   ============================================================ */

.topbar-premium {
    background: rgba(255,255,255,0.82) !important;
    backdrop-filter: blur(24px) saturate(1.6) !important;
    -webkit-backdrop-filter: blur(24px) saturate(1.6) !important;
    border-bottom: 1px solid rgba(0,0,0,0.07) !important;
    box-shadow:
        0 1px 0 rgba(255,255,255,0.9) inset,
        0 4px 24px rgba(0,0,0,0.04);
}

.dark .topbar-premium {
    background: rgba(11, 24, 41, 0.86) !important;
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.25);
}

/* ── Floating glass search capsule ── */
.search-capsule {
    background: rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

.dark .search-capsule {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
}

.search-capsule:focus-within {
    background: rgba(255,255,255,1);
    border-color: var(--accent);
    box-shadow:
        0 0 0 3px rgba(var(--accent-rgb), 0.12),
        0 4px 16px rgba(var(--accent-rgb), 0.08);
    transform: translateY(-1px);
}

.dark .search-capsule:focus-within {
    background: rgba(18, 32, 64, 1);
}

/* ── Glass topbar icon buttons ── */
.topbar-btn {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: transparent;
    border: 1px solid transparent;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
    position: relative;
    color: var(--text-muted);
}

.topbar-btn:hover {
    background: rgba(0,0,0,0.05);
    border-color: rgba(0,0,0,0.08);
    color: var(--text-secondary);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.07);
}

.dark .topbar-btn:hover {
    background: rgba(255,255,255,0.07);
    border-color: rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.8);
}

.topbar-btn:active {
    transform: translateY(0);
    box-shadow: none;
    background: rgba(0,0,0,0.08);
}

/* ── Animated notification dot ── */
.notif-dot {
    width: 7px;
    height: 7px;
    background: #EF4444;
    border-radius: 9999px;
    border: 1.5px solid white;
    position: absolute;
    top: 5px;
    right: 5px;
    animation: notif-pulse 2.5s ease-in-out infinite;
}

/* ============================================================
   KEYFRAMES
   ============================================================ */

@keyframes nav-bar-pulse {
    0%, 100% {
        box-shadow: 0 0 8px rgba(255,255,255,0.9), 0 0 18px rgba(255,255,255,0.4);
        opacity: 1;
    }
    50% {
        box-shadow: 0 0 16px rgba(255,255,255,1), 0 0 32px rgba(255,255,255,0.6);
        opacity: 0.8;
    }
}

@keyframes notif-pulse {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(239,68,68,0.45);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 0 0 5px rgba(239,68,68,0);
        transform: scale(1.15);
    }
}
"""

with open('static/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)
print("CSS appended successfully!")
