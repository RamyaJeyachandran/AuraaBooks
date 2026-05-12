const THEMES = {
    sky: {
        name: 'Sky blue',
        colors: {
            '--accent': '#2F80ED',
            '--accent2': '#56a0f5',
            '--accent-light': '#eaf2ff',
            '--accent-text': '#1a5fb5',
            '--sidebar-bg': 'linear-gradient(160deg, #56a0f5, #2F80ED, #1a5fb5)',
        }
    },
    violet: {
        name: 'Violet dream',
        colors: {
            '--accent': '#7c3aed',
            '--accent2': '#a78bda',
            '--accent-light': '#f5f3ff',
            '--accent-text': '#5b21b6',
            '--sidebar-bg': 'linear-gradient(160deg, #a78bda, #7c3aed, #5b21b6)',
        }
    },
    teal: {
        name: 'Forest teal',
        colors: {
            '--accent': '#0d9488',
            '--accent2': '#5eead4',
            '--accent-light': '#f0fdfa',
            '--accent-text': '#0f766e',
            '--sidebar-bg': 'linear-gradient(160deg, #5eead4, #0d9488, #0f766e)',
        }
    },
    coral: {
        name: 'Coral rose',
        colors: {
            '--accent': '#e11d48',
            '--accent2': '#fb7185',
            '--accent-light': '#fff1f2',
            '--accent-text': '#9f1239',
            '--sidebar-bg': 'linear-gradient(160deg, #fb7185, #e11d48, #9f1239)',
        }
    },
    green: {
        name: 'Forest green',
        colors: {
            '--accent': '#16a34a',
            '--accent2': '#86efac',
            '--accent-light': '#f0fdf4',
            '--accent-text': '#15803d',
            '--sidebar-bg': 'linear-gradient(160deg, #86efac, #16a34a, #15803d)',
        }
    },
    amber: {
        name: 'Golden amber',
        colors: {
            '--accent': '#d97706',
            '--accent2': '#fcd34d',
            '--accent-light': '#fffbeb',
            '--accent-text': '#b45309',
            '--sidebar-bg': 'linear-gradient(160deg, #fcd34d, #d97706, #b45309)',
        }
    }
};

function adjustColor(hex, amount) {
    let col = hex.replace('#', '');
    let r = parseInt(col.substring(0, 2), 16);
    let g = parseInt(col.substring(2, 4), 16);
    let b = parseInt(col.substring(4, 6), 16);
    r = Math.max(0, Math.min(255, r + amount));
    g = Math.max(0, Math.min(255, g + amount));
    b = Math.max(0, Math.min(255, b + amount));
    return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
}

function applyTheme(themeKey, customColor = null) {
    const root = document.documentElement;
    let colors = {};

    if (customColor) {
        colors = {
            '--accent': customColor,
            '--accent2': adjustColor(customColor, 40),
            '--accent-light': adjustColor(customColor, 180),
            '--accent-text': adjustColor(customColor, -60),
            '--sidebar-bg': `linear-gradient(160deg, ${adjustColor(customColor, 40)}, ${customColor}, ${adjustColor(customColor, -60)})`,
        };
    } else if (THEMES[themeKey]) {
        colors = THEMES[themeKey].colors;
    }

    Object.entries(colors).forEach(([key, value]) => {
        root.style.setProperty(key, value);
    });
    
    localStorage.setItem('activeTheme', themeKey);
    if (customColor) localStorage.setItem('customColor', customColor);
}

function toggleDark(isDark) {
    if (isDark) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('isDark', isDark);
    
    // Update Icons
    document.querySelector('.sun-icon').classList.toggle('hidden', !isDark);
    document.querySelector('.moon-icon').classList.toggle('hidden', isDark);
}

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('activeTheme') || 'sky';
    const savedCustomColor = localStorage.getItem('customColor');
    const savedIsDark = localStorage.getItem('isDark') === 'true';

    applyTheme(savedTheme, savedTheme === 'custom' ? savedCustomColor : null);
    toggleDark(savedIsDark);

    // Theme Toggle Click
    document.getElementById('themeToggle').addEventListener('click', () => {
        const isDark = !document.documentElement.classList.contains('dark');
        toggleDark(isDark);
    });

    // Palette Toggle Click
    const paletteToggle = document.getElementById('paletteToggle');
    const themePanel = document.getElementById('themePanel');

    if (paletteToggle && themePanel) {
        paletteToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            themePanel.classList.toggle('hidden');
        });

        // Close when clicking outside
        window.addEventListener('click', (e) => {
            if (!themePanel.contains(e.target) && !paletteToggle.contains(e.target)) {
                themePanel.classList.add('hidden');
            }
        });
    }
});
