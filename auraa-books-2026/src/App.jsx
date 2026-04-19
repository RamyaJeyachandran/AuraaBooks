import React, { useState, useEffect } from 'react'

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
}

const Icon = ({ name, className = "w-4 h-4" }) => {
  const icons = {
    dashboard: <path d="M3 3h7v7H3V3zm11 0h7v7h-7V3zm0 11h7v7h-7v-7zm-11 0h7v7H3v-7z" />,
    masters: <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />,
    sales: <path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2m4 0v2m0 4v.01M8 4h8a2 2 0 012 2v2H6V6a2 2 0 012-2z" />,
    purchase: <path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />,
    expenses: <path d="M12 8c-1.657 0-3 1.343-3 3s1.343 3 3 3 3-1.343 3-3-1.343-3-3-3zM12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2z" />,
    settings: <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />,
    search: <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />,
    sun: <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.343l-.707-.707M12 7a5 5 0 100 10 5 5 0 000-10z" />,
    moon: <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />,
    palette: <path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9a1 1 0 001-1v-1.17c0-.64.53-1.17 1.17-1.17h1.17a1 1 0 001-1c0-4.97-4.03-9-9-9zm-6 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm2-4c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 4c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z" />,
    bell: <path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />,
    chevron: <path d="M9 5l7 7-7 7" />,
    plus: <path d="M12 4v16m8-8H4" />,
    close: <path d="M6 18L18 6M6 6l12 12" />,
    pin: <><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><circle cx="12" cy="11" r="3" /></>,
    info: <><circle cx="12" cy="12" r="10" /><line x1="12" y1="16" x2="12" y2="12" /><line x1="12" y1="8" x2="12.01" y2="8" /></>,
    attach: <path d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.414a4 4 0 00-5.656-5.656l-6.415 6.415a6 6 0 108.486 8.486L20.5 13" />,
    users: <><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 00-3-3.87" /><path d="M16 3.13a4 4 0 010 7.75" /></>,
    userCheck: <><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M17 11l2 2 4-4" /></>,
    userX: <><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M18 8l5 5m0-5l-5 5" /></>,
    factory: <><path d="M2 20V9l9-2 10 2v11" /><path d="M9 20V15l3-1 3 1v5" /><path d="M17 13l4-1v2l-4 1" /><path d="M17 17l4-1v2l-4 1" /></>,
    package: <><path d="M16.5 9.4 7.5 4.21" /><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" /><polyline points="3.29 7 12 12 20.71 7" /><line x1="12" y1="22" x2="12" y2="12" /></>,
    link: <><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" /><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" /></>,
    warehouse: <><path d="M22 20V10a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v10" /><path d="M11 18V9" /><path d="M7 18V8" /><path d="M15 18V10" /><path d="M19 18V11" /><path d="M2 10l10-8 10 8" /></>,
    calendar: <><rect x="3" y="4" width="18" height="18" rx="2" ry="2" /><line x1="16" y1="2" x2="16" y2="6" /><line x1="8" y1="2" x2="8" y2="6" /><line x1="3" y1="10" x2="21" y2="10" /></>,
  }
  return (
    <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      {icons[name]}
    </svg>
  )
}

const App = () => {
  const [activeTheme, setActiveTheme] = useState('sky')
  const [customColor, setCustomColor] = useState('#2F80ED')
  const [isDark, setIsDark] = useState(false)
  const [showThemePanel, setShowThemePanel] = useState(false)
  const [activeNav, setActiveNav] = useState('Dashboard')
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [modalTab, setModalTab] = useState('Billing Address')
  const [showSaveDropdown, setShowSaveDropdown] = useState(false)
  const [showTagTooltip, setShowTagTooltip] = useState(false)
  const [showGeoInput, setShowGeoInput] = useState(false)
  const fileInputRef = React.useRef(null)

  // Close dropdowns on click outside
  useEffect(() => {
    if (!showSaveDropdown && !showTagTooltip) return
    const handleClick = () => {
      setShowSaveDropdown(false)
      setShowTagTooltip(false)
    }
    window.addEventListener('click', handleClick)
    return () => window.removeEventListener('click', handleClick)
  }, [showSaveDropdown, showTagTooltip])

  // Helper to adjust color brightness
  const adjustColor = (hex, amount) => {
    let col = hex.replace('#', '')
    let r = parseInt(col.substring(0,2), 16)
    let g = parseInt(col.substring(2,4), 16)
    let b = parseInt(col.substring(4,6), 16)
    r = Math.max(0, Math.min(255, r + amount))
    g = Math.max(0, Math.min(255, g + amount))
    b = Math.max(0, Math.min(255, b + amount))
    return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`
  }

  useEffect(() => {
    const root = document.documentElement
    let colors = {}
    if (THEMES[activeTheme]) {
      colors = THEMES[activeTheme].colors
    } else {
      // Custom theme generation
      colors = {
        '--accent': customColor,
        '--accent2': adjustColor(customColor, 40),
        '--accent-light': adjustColor(customColor, 180),
        '--accent-text': adjustColor(customColor, -60),
        '--sidebar-bg': `linear-gradient(160deg, ${adjustColor(customColor, 40)}, ${customColor}, ${adjustColor(customColor, -60)})`,
      }
    }

    Object.entries(colors).forEach(([key, value]) => {
      root.style.setProperty(key, value)
    })
    
    if (isDark) {
      root.classList.add('dark')
    } else {
      root.classList.remove('dark')
    }
  }, [activeTheme, customColor, isDark])

  const NavItem = ({ name, icon, subItems }) => {
    const isParentActive = activeNav === name || subItems?.some(s => activeNav === s)
    const [isOpen, setIsOpen] = useState(isParentActive)

    // Force open if active nav changes to a child of this item
    useEffect(() => {
      if (isParentActive) setIsOpen(true)
    }, [activeNav, isParentActive])
    
    return (
      <div className="mb-0.5">
        <div 
          onClick={() => {
            if (subItems) setIsOpen(!isOpen)
            else setActiveNav(name)
          }}
          className={`flex items-center gap-3 px-4 py-3 cursor-pointer transition-all duration-200 relative group/item [transform-style:preserve-3d] z-10
            ${activeNav === name || isParentActive
              ? 'bg-black/40 border border-white/10 rounded-2xl shadow-[0_15px_35px_rgba(0,0,0,0.4),inset_0_1px_1px_rgba(255,255,255,0.1)] translate-z-[15px] scale-[1.03] text-white font-black' 
              : 'text-white hover:bg-white/5 hover:translate-x-1 rounded-xl'
            }`}
        >
          {/* Active 3D Indicator */}
          {(activeNav === name || isParentActive) && (
            <div className="absolute -left-1 inset-y-3 w-1 bg-white rounded-full shadow-[0_0_15px_rgba(255,255,255,0.8)]" />
          )}
          <div className={`w-7 h-7 rounded-lg flex items-center justify-center transition-colors
            ${activeNav === name || isParentActive ? 'bg-white/20 text-white shadow-inner' : 'bg-white/10 text-white'}`}>
            <Icon name={icon} className="w-3.5 h-3.5" />
          </div>
          <span className="text-[13px] flex-1 font-medium">{name}</span>
          {subItems && (
            <Icon name="chevron" className={`w-3 h-3 transition-transform ${isOpen ? 'rotate-90' : ''}`} />
          )}
        </div>
        
        {subItems && isOpen && (
          <div className="mt-1 space-y-1 ml-10 mr-1 overflow-hidden">
            {subItems.map(sub => (
              <div 
                key={sub}
                onClick={() => setActiveNav(sub)}
                className={`px-4 py-2 text-[12px] cursor-pointer rounded-xl transition-all duration-150 relative ml-4 mb-0.5 [transform-style:preserve-3d] z-10
                  ${activeNav === sub 
                    ? 'text-white bg-black/40 font-black shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/10 translate-z-[10px] scale-[1.02]' 
                    : 'text-white hover:text-white hover:bg-white/5 hover:translate-x-1'}`}
              >
                {sub}
              </div>
            ))}
          </div>
        )}
      </div>
    )
  }

  const getBreadcrumbs = () => {
    if (activeNav === 'Dashboard') return ['AuraaBooks', 'Dashboard']
    if (activeNav === 'Settings') return ['AuraaBooks', 'Settings']
    
    const sections = [
      { name: 'Masters', items: ['Customer', 'Suppliers', 'Items', 'Referrer', 'Warehouse', 'Branch', 'Franchisee', 'Project', 'Sales Rep', 'Bank / Cash', 'Rate Sheet', 'Stock Journal'] },
      { name: 'Sales', items: ['Quotes', 'Sales Order', 'Invoice', 'Delivery challan', 'Credit Note', 'Receipt'] },
      { name: 'Purchase', items: ['Purchase Quote', 'Purchase Order', 'Goods Receipt', 'Purchase Bill', 'Payment', 'Supplier Credit Note'] },
      { name: 'Expenses', items: ['Credit Expenses', 'Asset Expenses', 'Cash Expenses', 'Reclaim Expenses'] }
    ]
    
    for (const section of sections) {
      if (section.items.includes(activeNav)) return [section.name, activeNav]
      if (activeNav === section.name) return ['AuraaBooks', section.name]
    }
    return ['AuraaBooks', activeNav]
  }

  const breadcrumbs = getBreadcrumbs()

  const KPICard = ({ label, value, icon }) => (
    <div className="card group tilt-card h-full">
      <div className="absolute top-0 left-0 w-full h-[3px] bg-gradient-to-r from-accent2 to-accent opacity-0 group-hover:opacity-100 transition-opacity" />
      <div className="flex justify-between items-start mb-4 [transform:translateZ(10px)]">
        <span className="text-[11px] font-bold text-[var(--text-muted)] uppercase tracking-[0.06em]">{label}</span>
        <div className="w-[32px] h-[32px] rounded-[10px] bg-[var(--accent-light)] text-[var(--accent-text)] flex items-center justify-center shadow-inner">
          <Icon name={icon} className="w-4.5 h-4.5" />
        </div>
      </div>
      <div className="text-[34px] font-black text-[var(--accent)] tracking-tight [transform:translateZ(20px)] leading-none">{value}</div>
    </div>
  )

  const Modal = ({ isOpen, onClose, title, children, maxWidth = "max-w-[1400px]" }) => {
    if (!isOpen) return null
    return (
      <div className="fixed inset-0 z-[9999] flex items-center justify-center p-6">
        <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-md transition-opacity" />
        <div className={`bg-white dark:bg-[var(--surface)] w-full ${maxWidth} h-[92vh] rounded-[40px] 
          shadow-[0_20px_50px_rgba(0,0,0,0.3),0_10px_30px_rgba(0,0,0,0.1),inset_0_1px_1px_rgba(255,255,255,0.8)] 
          relative z-10 overflow-hidden animate-in zoom-in-95 fade-in duration-200 border border-white/40 flex flex-col isolation-auto`}>
          {/* Internal rounding fix for corners */}
          <div className="absolute inset-0 rounded-[40px] pointer-events-none border border-white/20 z-50 shadow-[inset_0_0_0_1px_rgba(255,255,255,0.1)]" />
          {title && (
            <div className="px-8 py-5 border-b border-[var(--border)] flex items-center justify-between bg-white/50 dark:bg-[var(--bg)]/50 backdrop-blur-md">
              <h3 className="text-[18px] font-bold text-[var(--text-primary)] tracking-tight">{title}</h3>
              <button onClick={onClose} className="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-red-50 text-[#EF5350] transition-colors border border-transparent hover:border-red-100">
                <Icon name="close" className="w-6 h-6" />
              </button>
            </div>
          )}
          {!title && null}
          <div className="flex-1 overflow-hidden">
            {children}
          </div>
        </div>
      </div>
    )
  }

  const CustomerScreen = ({ onAdd }) => {
    return (
      <div className="stagger-in">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">Customer Management</h1>
            <p className="text-[13px] text-[var(--text-secondary)]">Manage your customer database and credit balances.</p>
          </div>
          <button onClick={onAdd} className="px-5 py-2.5 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold flex items-center gap-2 shadow-xl hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all">
            <Icon name="plus" className="w-4 h-4" />
            Add Customer
          </button>
        </div>

        <div className="grid grid-cols-3 gap-5 mb-8">
          <KPICard label="Total Customers" value="124" icon="users" />
          <KPICard label="Active Customers" value="118" icon="userCheck" />
          <KPICard label="In-Active Customers" value="6" icon="userX" />
        </div>

        <div className="card !p-0 overflow-hidden tilt-card shadow-xl border-none">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[var(--accent)] shadow-md">
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] first:rounded-tl-2xl">Customer Name</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Email Address</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Mobile</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Balance</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] text-right last:rounded-tr-2xl">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[var(--border)]">
              {[
                { name: 'Arun', email: 'arun@example.com', mobile: '917339604466', bal: '₹12,400' },
                { name: 'Priya Nair', email: 'priya@co.in', mobile: '99001 22334', bal: '₹3,200' },
                { name: 'Ravi Kumar', email: 'ravi@biz.com', mobile: '97887 65432', bal: '₹8,750' }
              ].map((row, i) => (
                <tr key={i} className="hover:bg-[var(--bg)]/30 transition-colors group cursor-pointer">
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--accent)] group-hover:underline">{row.name}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.email}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.mobile}</td>
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--text-primary)]">{row.bal}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="px-3 py-1 bg-[var(--accent)]/10 text-[var(--accent)] rounded-lg text-[11px] font-bold hover:bg-[var(--accent)] hover:text-white transition-all">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const SupplierScreen = ({ onAdd }) => {
    return (
      <div className="stagger-in">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">Supplier Management</h1>
            <p className="text-[13px] text-[var(--text-secondary)]">Manage your vendor relationships and procurement.</p>
          </div>
          <button onClick={onAdd} className="px-5 py-2.5 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold flex items-center gap-2 shadow-xl hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all">
            <Icon name="plus" className="w-4 h-4" />
            Add Supplier
          </button>
        </div>

        <div className="grid grid-cols-3 gap-5 mb-8">
          <KPICard label="Total Suppliers" value="42" icon="factory" />
          <KPICard label="Active Suppliers" value="40" icon="userCheck" />
          <KPICard label="In-Active Suppliers" value="2" icon="userX" />
        </div>

        <div className="card !p-0 overflow-hidden tilt-card shadow-xl border-none">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[var(--accent)] shadow-md">
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] first:rounded-tl-2xl">Supplier Name</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Mobile</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Balance</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] text-right last:rounded-tr-2xl">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[var(--border)]">
              {[
                { name: 'Global Supplies Co.', mobile: '98001 11223', bal: '₹88,000' },
                { name: 'Raj Traders', mobile: '97765 43210', bal: '₹14,200' },
                { name: 'Metro Wholesale', mobile: '99834 55678', bal: '₹22,500' }
              ].map((row, i) => (
                <tr key={i} className="hover:bg-[var(--bg)]/30 transition-colors group cursor-pointer">
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--accent)] group-hover:underline">{row.name}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.mobile}</td>
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--text-primary)]">{row.bal}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="px-3 py-1 bg-[var(--accent)]/10 text-[var(--accent)] rounded-lg text-[11px] font-bold hover:bg-[var(--accent)] hover:text-white transition-all">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const ItemsScreen = ({ onAdd }) => {
    return (
      <div className="stagger-in">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">Items & Inventory</h1>
            <p className="text-[13px] text-[var(--text-secondary)]">Manage your product catalog and stock levels.</p>
          </div>
          <button onClick={onAdd} className="px-5 py-2.5 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold flex items-center gap-2 shadow-xl hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all">
            <Icon name="plus" className="w-4 h-4" />
            Add Item
          </button>
        </div>

        <div className="grid grid-cols-3 gap-5 mb-8">
          <KPICard label="Total Items" value="1,248" icon="package" />
          <KPICard label="Active Items" value="1,245" icon="userCheck" />
          <KPICard label="In-Active Items" value="3" icon="userX" />
        </div>

        <div className="card !p-0 overflow-hidden tilt-card shadow-xl border-none">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[var(--accent)] shadow-md">
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] first:rounded-tl-2xl">Item Name</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Categories</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Type</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">SKU</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">HSN</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] text-right last:rounded-tr-2xl">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[var(--border)]">
              {[
                { name: 'AERIAL CHOTTA FANCY Pcs', category: 'AERIAL CHOTTA FANCY', type: 'Goods', sku: '146', hsn: '3604' },
                { name: 'Office Chair Premium', category: 'Furniture', type: 'Goods', sku: 'FURN-001', hsn: '94013000' }
              ].map((row, i) => (
                <tr key={i} className="hover:bg-[var(--bg)]/30 transition-colors group cursor-pointer">
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--accent)] group-hover:underline">{row.name}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.category}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.type}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.sku}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.hsn}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="px-3 py-1 bg-[var(--accent)]/10 text-[var(--accent)] rounded-lg text-[11px] font-bold hover:bg-[var(--accent)] hover:text-white transition-all">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const ReferrerScreen = ({ onAdd }) => {
    return (
      <div className="stagger-in">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">Referrer Network</h1>
            <p className="text-[13px] text-[var(--text-secondary)]">Manage agents and referral commissions.</p>
          </div>
          <button onClick={onAdd} className="px-5 py-2.5 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold flex items-center gap-2 shadow-xl hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all">
            <Icon name="plus" className="w-4 h-4" />
            Add Referrer
          </button>
        </div>

        <div className="grid grid-cols-3 gap-5 mb-8">
          <KPICard label="Total Referrers" value="12" icon="link" />
          <KPICard label="Active Referrers" value="10" icon="userCheck" />
          <KPICard label="In-Active Referrers" value="2" icon="userX" />
        </div>

        <div className="card !p-0 overflow-hidden tilt-card shadow-xl border-none">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[var(--accent)] shadow-md">
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] first:rounded-tl-2xl">Name</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Mobile</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Commission %</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Balance</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] text-right last:rounded-tr-2xl">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[var(--border)]">
              {[
                { name: 'Sanjay Mehta', mobile: '98765 00001', comm: '5%', bal: '₹6,200' },
                { name: 'Asha Pillai', mobile: '99112 33445', comm: '8%', bal: '₹14,800' }
              ].map((row, i) => (
                <tr key={i} className="hover:bg-[var(--bg)]/30 transition-colors group cursor-pointer">
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--accent)] group-hover:underline">{row.name}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.mobile}</td>
                  <td className="px-6 py-4 text-[13px] font-bold text-accent icon-theme">{row.comm}</td>
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--text-primary)]">{row.bal}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="px-3 py-1 bg-[var(--accent)]/10 text-[var(--accent)] rounded-lg text-[11px] font-bold hover:bg-[var(--accent)] hover:text-white transition-all">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const WarehouseScreen = ({ onAdd }) => {
    return (
      <div className="stagger-in">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">Warehouse & Locations</h1>
            <p className="text-[13px] text-[var(--text-secondary)]">Manage inventory locations and branch stock.</p>
          </div>
          <button onClick={onAdd} className="px-5 py-2.5 bg-[var(--accent)] text-white rounded-xl text-[13px] font-bold flex items-center gap-2 shadow-xl hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all">
            <Icon name="plus" className="w-4 h-4" />
            Add Warehouse
          </button>
        </div>

        <div className="grid grid-cols-3 gap-5 mb-8">
          <KPICard label="Total Warehouses" value="5" icon="warehouse" />
          <KPICard label="Active Warehouses" value="4" icon="userCheck" />
          <KPICard label="In-Active Warehouses" value="1" icon="userX" />
        </div>

        <div className="card !p-0 overflow-hidden tilt-card shadow-xl border-none">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[var(--accent)] shadow-md">
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] first:rounded-tl-2xl">Location Name</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Contact Mobile</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Branch</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em]">Stock Value</th>
                <th className="px-6 py-4 text-[11px] font-black text-white uppercase tracking-[0.1em] text-right last:rounded-tr-2xl">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[var(--border)]">
              {[
                { name: 'Main Warehouse', mobile: '98000 11111', branch: 'HQ Branch', bal: '₹4,50,000' },
                { name: 'North Hub', mobile: '97000 22222', branch: 'North Branch', bal: '₹1,80,000' }
              ].map((row, i) => (
                <tr key={i} className="hover:bg-[var(--bg)]/30 transition-colors group cursor-pointer">
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--accent)] group-hover:underline">{row.name}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.mobile}</td>
                  <td className="px-6 py-4 text-[13px] text-[var(--text-secondary)] font-medium">{row.branch}</td>
                  <td className="px-6 py-4 text-[13px] font-bold text-[var(--text-primary)]">{row.bal}</td>
                  <td className="px-6 py-4 text-right">
                    <button className="px-3 py-1 bg-[var(--accent)]/10 text-[var(--accent)] rounded-lg text-[11px] font-bold hover:bg-[var(--accent)] hover:text-white transition-all">Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  const DashboardScreen = () => (
    <div className="stagger-in">
      <div className="mb-6">
        <h1 className="text-[22px] font-bold text-[var(--text-primary)] mb-1">System Overview</h1>
        <p className="text-[13px] text-[var(--text-secondary)]">
          Your business is performing <span className="text-[#16a34a] font-bold">12% better</span> than last quarter.
        </p>
      </div>

      <div className="grid grid-cols-4 gap-3 mb-6">
        <KPICard label="Total Revenue" value="₹24.5L" trend="12.5%" isUp={true} icon="sales" />
        <KPICard label="Pending Bills" value="₹1.42L" trend="3.2%" isUp={false} icon="purchase" />
        <KPICard label="Active Projects" value="12" trend="24%" isUp={true} icon="dashboard" />
        <KPICard label="New Leads" value="48" trend="8.4%" isUp={true} icon="masters" />
      </div>

      <div className="card !p-0 overflow-hidden tilt-card shadow-lg">
        <div className="px-5 py-4 flex justify-between items-center border-b border-[var(--border)]">
          <h2 className="text-[15px] font-semibold text-[var(--text-primary)]">Recent Transactions</h2>
          <button className="px-4 py-1.5 bg-[var(--accent)] text-white font-bold rounded-lg text-[12px] shadow-lg shadow-accent/20 hover:opacity-90 transition-all hover:-translate-y-0.5 active:scale-95">
            View All →
          </button>
        </div>
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-white/10 bg-[var(--accent)] shadow-md">
              <th className="px-5 py-3.5 text-[10px] font-black text-white uppercase tracking-widest first:rounded-tl-xl">Date</th>
              <th className="px-5 py-3.5 text-[10px] font-black text-white uppercase tracking-widest">Reference</th>
              <th className="px-5 py-3.5 text-[10px] font-black text-white uppercase tracking-widest">Customer</th>
              <th className="px-5 py-3.5 text-[10px] font-black text-white uppercase tracking-widest">Status</th>
              <th className="px-5 py-3.5 text-[10px] font-black text-white uppercase tracking-widest text-right last:rounded-tr-xl">Amount</th>
            </tr>
          </thead>
          <tbody>
            {[
              { date: '2026-04-18', ref: 'INV-001', cust: 'Arun Kumar', status: 'PAID', amt: '₹12,400', color: 'bg-green-100 text-green-700' },
              { date: '2026-04-17', ref: 'INV-002', cust: 'Priya Nair', status: 'PENDING', amt: '₹8,750', color: 'bg-yellow-100 text-yellow-700' },
              { date: '2026-04-17', ref: 'INV-003', cust: 'Ravi Singh', status: 'OVERDUE', amt: '₹14,200', color: 'bg-red-100 text-red-700' },
            ].map((row, i) => (
              <tr key={i} className="border-b border-[var(--border)] hover:bg-[var(--bg)] transition-colors">
                <td className="px-5 py-4 text-[13px] text-[var(--text-secondary)]">{row.date}</td>
                <td className="px-5 py-4 text-[13px] font-bold text-[var(--text-primary)]">{row.ref}</td>
                <td className="px-5 py-4 text-[13px] text-[var(--text-secondary)]">{row.cust}</td>
                <td className="px-5 py-4 text-[13px]">
                  <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${row.color}`}>{row.status}</span>
                </td>
                <td className="px-5 py-4 text-[13px] font-bold text-[var(--text-primary)] text-right">{row.amt}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )

  return (
    <div className="flex h-screen overflow-hidden rounded-[16px] perspective-2000 relative">
      <div className="mesh-bg" />
      
      {/* SIDEBAR */}
      <aside 
        className="w-[230px] h-full flex-shrink-0 flex flex-col relative z-20 group/sidebar transition-all duration-700 ease-out [transform-style:preserve-3d] [perspective:1000px]" 
        style={{ 
          background: 'var(--sidebar-bg)',
          boxShadow: '20px 0 50px -10px rgba(0,0,0,0.3)'
        }}
      >
        {/* 3D Decorative Elements (Background Layers) */}
        <div className="absolute inset-0 bg-white/5 backdrop-blur-[2px] pointer-events-none z-0" />
        <div className="absolute inset-y-0 right-0 w-[2px] bg-white/20 blur-[1px] z-0" />
        <div className="h-[52px] flex items-center px-4 mb-4 relative z-10">
          <div className="w-9 h-9 rounded-full bg-white/30 backdrop-blur-md border border-white/40 flex items-center justify-center text-white font-black text-[18px] shadow-[0_4px_12px_rgba(255,255,255,0.15)] transition-transform hover:scale-110">A</div>
          <span className="ml-2.5 text-[15px] font-black text-white drop-shadow-md">AuraaBooks</span>
        </div>

        <div className="flex-1 px-3 space-y-0.5 overflow-y-auto no-scrollbar">
          <NavItem name="Dashboard" icon="dashboard" />
          
          <div className="h-1" /> {/* Smaller Spacer */}
          
          <NavItem 
            name="Masters" 
            icon="masters" 
            subItems={[
              'Customer', 'Suppliers', 'Items', 'Referrer', 'Warehouse', 
              'Branch', 'Franchisee', 'Project', 'Sales Rep', 
              'Bank / Cash', 'Rate Sheet', 'Stock Journal'
            ]} 
          />
          
          <div className="h-1" /> {/* Smaller Spacer */}
          
          <NavItem 
            name="Sales" 
            icon="sales" 
            subItems={['Quotes', 'Sales Order', 'Invoice', 'Delivery challan', 'Credit Note', 'Receipt']} 
          />
          <NavItem 
            name="Purchase" 
            icon="purchase" 
            subItems={['Purchase Quote', 'Purchase Order', 'Goods Receipt', 'Purchase Bill', 'Payment', 'Supplier Credit Note']} 
          />
          <NavItem 
            name="Expenses" 
            icon="expenses" 
            subItems={['Credit Expenses', 'Asset Expenses', 'Cash Expenses', 'Reclaim Expenses']} 
          />
          
          <div className="h-1" /> {/* Smaller Spacer */}
          
          <NavItem name="Settings" icon="settings" />
        </div>

        <div className="p-4 flex items-center gap-3 border-t border-white/15 relative z-10 bg-black/10">
          <div className="w-8 h-8 rounded-full bg-white/25 border border-white/35 flex items-center justify-center text-white text-[12px] font-bold shadow-lg">G</div>
          <div>
            <div className="text-white text-[13px] font-black leading-tight">Guest</div>
            <div className="text-white text-[11px] leading-tight font-bold opacity-90">User</div>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <div className="flex-1 flex flex-col overflow-hidden bg-[var(--bg)]">
        {/* HEADER */}
        <header className="h-[52px] flex-shrink-0 bg-white border-b border-[#d6e6fb] dark:bg-[var(--surface)] dark:border-[var(--border)] flex items-center justify-between px-6 sticky top-0 z-20 transition-all">
          <div className="text-[13px] flex items-center gap-1.5 text-[var(--text-muted)]">
            <span className="hover:text-accent icon-theme cursor-pointer">{breadcrumbs[0]}</span>
            <span className="opacity-50">/</span>
            <span className="text-[var(--text-secondary)] font-medium">{breadcrumbs[1]}</span>
          </div>

          <div className="flex-1 max-w-[400px] mx-10 relative">
            <Icon name="search" className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[var(--text-muted)]" />
            <input 
              type="text" 
              placeholder="Search or press ⌘K"
              className="w-full h-9 bg-[#f0f6ff] border border-[#d6e6fb] rounded-lg pl-9 pr-4 text-[13px] outline-none focus:border-accent dark:bg-[var(--bg)] dark:border-[var(--border)]"
            />
          </div>

          <div className="flex items-center gap-2">
            <button onClick={() => setIsDark(!isDark)} className="btn-icon">
              <Icon name={isDark ? 'sun' : 'moon'} />
            </button>
            <div className="relative">
              <button onClick={() => setShowThemePanel(!showThemePanel)} className="btn-icon">
                <Icon name="palette" />
              </button>
              {showThemePanel && (
                <div className="absolute right-0 top-10 w-[180px] bg-white dark:bg-[var(--surface)] border border-[var(--border)] rounded-lg shadow-xl p-3 z-50">
                  <div className="text-[10px] font-bold text-[var(--text-muted)] uppercase mb-3">Color Theme</div>
                  <div className="space-y-1">
                    {Object.entries(THEMES).map(([key, theme]) => (
                      <div 
                        key={key}
                        onClick={() => { setActiveTheme(key); setShowThemePanel(false); }}
                        className={`flex items-center gap-2.5 p-1.5 rounded-md cursor-pointer transition-colors
                          ${activeTheme === key ? 'bg-[var(--accent-light)] border border-[var(--border)]' : 'hover:bg-[var(--bg)]'}`}
                      >
                        <div className="w-5 h-5 rounded-full" style={{ background: theme.colors['--sidebar-bg'] }} />
                        <span className="text-[11px] font-medium text-[var(--text-secondary)]">{theme.name}</span>
                      </div>
                    ))}
                    <div className="pt-2 mt-2 border-t border-[var(--border)]">
                      <div className="text-[9px] font-bold text-[var(--text-muted)] uppercase mb-2">Custom Color</div>
                      <div className="flex items-center gap-2">
                        <input 
                          type="color" 
                          value={customColor}
                          onChange={(e) => { setCustomColor(e.target.value); setActiveTheme('custom'); }}
                          className="w-full h-8 cursor-pointer rounded bg-transparent border-none"
                        />
                        <div className="text-[10px] font-mono opacity-50">{customColor.toUpperCase()}</div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
            <button className="btn-icon relative">
              <Icon name="bell" />
              <div className="absolute top-1.5 right-1.5 w-1.5 h-1.5 bg-[#EB5757] rounded-full border border-white" />
            </button>
            <div className="w-8 h-8 rounded-full bg-accent border-2 border-accent-light flex items-center justify-center text-white text-[12px] font-bold">G</div>
          </div>
        </header>

        {/* CONTENT */}
        <main className="flex-1 overflow-y-auto p-6 no-scrollbar stagger-in">
          {activeNav === 'Dashboard' ? <DashboardScreen /> : 
           activeNav === 'Customer' ? <CustomerScreen onAdd={() => { setModalTab('Billing Address'); setIsModalOpen(true); }} /> : 
           activeNav === 'Suppliers' ? <SupplierScreen onAdd={() => { setModalTab('Billing Address'); setIsModalOpen(true); }} /> : 
           activeNav === 'Items' ? <ItemsScreen onAdd={() => { setModalTab('Details'); setIsModalOpen(true); }} /> : 
           activeNav === 'Referrer' ? <ReferrerScreen onAdd={() => { setModalTab('Basic Details'); setIsModalOpen(true); }} /> : 
           activeNav === 'Warehouse' ? <WarehouseScreen onAdd={() => { setModalTab('Warehouse Details'); setIsModalOpen(true); }} /> : 
           <div className="flex items-center justify-center h-full text-[var(--text-muted)] animate-pulse">
             <div className="text-center">
                <Icon name="masters" className="w-12 h-12 mx-auto mb-4 opacity-20" />
                <div className="text-[15px] font-bold uppercase tracking-widest opacity-30">Screen "{activeNav}"</div>
                <div className="text-[12px] opacity-20 mt-1">This module is currently under development</div>
             </div>
           </div>
          }
        </main>
      </div>

      {/* MODAL PORTAL (ROOT LEVEL) */}
      <Modal 
        isOpen={isModalOpen} 
        onClose={() => setIsModalOpen(false)} 
        title={null}
        maxWidth={activeNav === 'Items' ? 'max-w-5xl' : 
                  (activeNav === 'Warehouse' || activeNav === 'Referrer') ? 'max-w-2xl' : 'max-w-[1400px]'}
      >
        <div className="flex flex-col h-full">
          {/* Header Actions / 3D Tabs */}
          <div className="px-8 py-3.5 border-b border-slate-100 flex items-center justify-between bg-white/80 backdrop-blur-md sticky top-0 z-30 shadow-[0_4px_20px_-5px_rgba(0,0,0,0.05)] rounded-t-[40px]">
            <div className="flex items-center gap-8">
              <div className="flex items-center gap-2">
                <span className="text-[20px] font-black text-[var(--accent)] tracking-tight">
                  {activeNav === 'Supplier' ? 'Add Supplier' : 
                   activeNav === 'Items' ? 'Add Item' : 
                   activeNav === 'Referrer' ? 'Add Referrer' : 
                   activeNav === 'Warehouse' ? 'Add Warehouse' : 'Add Customer'}
                </span>
              </div>
              
              {activeNav === 'Items' && (
                <div className="flex bg-[var(--accent)] p-1 rounded-2xl border border-white/20 shadow-lg shadow-black/10">
                  {['Details', 'Attributes', 'Rate Sheet'].map(tab => (
                    <button
                      key={tab}
                      onClick={() => setModalTab(tab)}
                      className={`px-6 py-1.5 rounded-xl text-[11px] font-black uppercase tracking-widest transition-all duration-150
                        ${modalTab === tab 
                          ? 'bg-white text-[var(--accent)] shadow-[0_4px_12px_rgba(0,0,0,0.15)] scale-[1.02]' 
                          : 'text-white/70 hover:text-white hover:bg-white/10'}`}
                    >
                      {tab}
                    </button>
                  ))}
                </div>
              )}
            </div>
            <div className="flex items-center gap-3">
              <button onClick={() => setIsModalOpen(false)} className="px-6 py-2 bg-[#64748B] text-white rounded-xl text-[13px] font-bold hover:bg-[#475569] transition-all shadow-lg hover:shadow-xl active:scale-95">Cancel</button>
              <div className="flex relative">
                <button 
                  onClick={() => setIsModalOpen(false)} 
                  className="px-6 py-2 bg-[var(--accent)] text-white rounded-l-lg text-[13px] font-bold shadow-md hover:brightness-110 transition-all border-r border-white/20"
                >
                  Save
                </button>
                <button 
                  onClick={(e) => {
                    e.stopPropagation();
                    setShowSaveDropdown(!showSaveDropdown);
                  }}
                  className="px-2 bg-[var(--accent)] text-white rounded-r-lg hover:brightness-110 border-l border-white/10 transition-all"
                >
                  <Icon name="chevron" className={`w-3 h-3 transition-transform duration-200 ${showSaveDropdown ? 'rotate-[-90deg]' : 'rotate-90'}`} />
                </button>

                {showSaveDropdown && (
                  <div className="absolute top-full right-0 mt-3 w-56 bg-white/95 backdrop-blur-xl rounded-[24px] shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] border border-[var(--accent)]/30 py-3 z-[10001] animate-in fade-in zoom-in-95 slide-in-from-top-4 duration-150 ring-1 ring-black/5">
                    <div className="px-2 space-y-1">
                      <button 
                        onClick={() => { setIsModalOpen(false); setShowSaveDropdown(false); }}
                        className="w-full text-left px-5 py-3.5 text-[14px] text-[#334155] hover:bg-[var(--accent)] hover:text-white rounded-2xl transition-all font-bold flex items-center justify-between group"
                      >
                        Save & New
                        <Icon name="plus" className="w-3.5 h-3.5 opacity-0 group-hover:opacity-100 transition-opacity" />
                      </button>
                      <button 
                        onClick={() => { setIsModalOpen(false); setShowSaveDropdown(false); }}
                        className="w-full text-left px-5 py-3.5 text-[14px] text-[#334155] hover:bg-[var(--accent)] hover:text-white rounded-2xl transition-all font-bold flex items-center justify-between group"
                      >
                        Save
                        <Icon name="chevron" className="w-3.5 h-3.5 opacity-0 group-hover:opacity-100 transition-opacity" />
                      </button>
                    </div>
                  </div>
                )}
              </div>
              <button onClick={() => setIsModalOpen(false)} className="w-9 h-9 flex items-center justify-center rounded-lg hover:bg-red-50 text-[#EF5350] transition-colors ml-2 border border-red-100/50">
                <Icon name="close" className="w-5 h-5" />
              </button>
            </div>
          </div>

          <div className="flex flex-1 overflow-hidden h-full">
            {activeNav === 'Items' ? (
              <div className="w-full flex flex-col h-full bg-white">
                <div className="flex-1 overflow-y-auto p-5 space-y-2 no-scrollbar">
                  {modalTab === 'Details' ? (
                    <div className="animate-in fade-in duration-200 space-y-2.5">
                      {/* Row 1: Identity */}
                      <div className="flex gap-4 items-start">
                        <div className="flex-1 grid grid-cols-3 gap-3">
                          <div className="col-span-2 space-y-1">
                            <label className="text-[9px] font-black text-red-500 uppercase tracking-widest">Item Name *</label>
                            <input type="text" className="w-full h-8 bg-slate-50 border border-slate-200 rounded-lg px-3 text-[12px] outline-none" />
                          </div>
                          <div className="space-y-1">
                            <label className="text-[9px] font-black text-black uppercase tracking-widest">Type</label>
                            <div className="relative">
                              <select className="w-full h-8 bg-slate-50 border border-slate-200 rounded-lg px-3 text-[12px] outline-none appearance-none">
                                <option>Goods</option>
                                <option>Service</option>
                              </select>
                              <Icon name="chevron" className="absolute right-3 top-1/2 -translate-y-1/2 w-3 h-3 text-slate-400 rotate-90" />
                            </div>
                          </div>
                        </div>
                        <div className="w-16 h-16 rounded-xl bg-[var(--accent-light)] border border-accent/20 flex flex-col items-center justify-center text-accent icon-theme group cursor-pointer shrink-0 transition-all hover:bg-accent hover:text-white mt-5">
                          <Icon name="package" className="w-5 h-5 opacity-80" />
                          <span className="text-[7px] font-black mt-0.5">IMAGE</span>
                        </div>
                      </div>

                      {/* Row 2: Metadata */}
                      <div className="grid grid-cols-3 gap-3">
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Print Name</label>
                          <input type="text" className="w-full h-8 bg-slate-50 border border-slate-200 rounded-lg px-3 outline-none text-[11px]" />
                        </div>
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Unit</label>
                          <select className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] appearance-none outline-none">
                            <option>NOS</option>
                          </select>
                        </div>
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">SKU / Barcode</label>
                          <input type="text" className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] outline-none" />
                        </div>
                      </div>

                      {/* Row 3: HSN & Classification */}
                      <div className="grid grid-cols-3 gap-3">
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">HSN Code</label>
                          <input type="text" className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] outline-none" />
                        </div>
                        <div className="col-span-2 space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">HSN Description</label>
                          <input type="text" placeholder="Description" className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] outline-none" />
                        </div>
                      </div>

                      <div className="grid grid-cols-3 gap-3">
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Category</label>
                          <select className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] appearance-none outline-none">
                            <option>Categories...</option>
                          </select>
                        </div>
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Brand</label>
                          <select className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] appearance-none outline-none">
                            <option>Brand...</option>
                          </select>
                        </div>
                        <div className="space-y-1">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Tax</label>
                          <select className="w-full h-8 px-3 rounded-lg border border-slate-200 bg-slate-50 text-[11px] appearance-none outline-none">
                            <option>GST 18%</option>
                          </select>
                        </div>
                      </div>

                      {/* Row 4: Logistics */}
                      <div className="grid grid-cols-4 gap-3 items-end bg-slate-50/50 p-2 rounded-xl border border-slate-100">
                        <div className="flex flex-col gap-1.5 pb-0.5">
                          <div className="flex items-center gap-1.5">
                            <input type="checkbox" defaultChecked className="w-3.5 h-3.5 rounded border-slate-200 accent-accent text-accent icon-theme" />
                            <span className="text-[9px] font-black text-slate-500 uppercase">Inventory</span>
                          </div>
                          <div className="flex items-center gap-1.5">
                            <input type="checkbox" defaultChecked className="w-3.5 h-3.5 rounded border-slate-200 accent-accent text-accent icon-theme" />
                            <span className="text-[9px] font-black text-slate-500 uppercase">Active</span>
                          </div>
                        </div>
                        <div className="space-y-0.5">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Reorder</label>
                          <input type="text" className="w-full h-7 bg-white border border-slate-200 rounded-lg px-2 outline-none text-[11px]" />
                        </div>
                        <div className="space-y-0.5">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Min Qty</label>
                          <input type="text" className="w-full h-7 bg-white border border-slate-200 rounded-lg px-2 outline-none text-[11px]" />
                        </div>
                        <div className="space-y-0.5">
                          <label className="text-[8px] font-black text-black uppercase tracking-widest">Pieces</label>
                          <input type="text" className="w-full h-7 bg-white border border-slate-200 rounded-lg px-2 outline-none text-[11px]" />
                        </div>
                      </div>

                      {/* Financial Cards (Side by side) */}
                      <div className="grid grid-cols-2 gap-4">
                        <div className="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-3 shadow-sm relative overflow-hidden">
                          <div className="flex items-center gap-2">
                            <input type="checkbox" defaultChecked className="w-4 h-4 rounded border-slate-200 accent-accent text-accent icon-theme shadow-sm" />
                            <span className="text-[11px] font-black uppercase tracking-widest text-black">In Sales</span>
                          </div>
                          <div className="grid grid-cols-2 gap-3">
                            <div className="space-y-1">
                              <label className="text-[9px] font-black text-black uppercase tracking-widest">Sale Rate</label>
                              <input type="text" className="w-full h-8 px-3 rounded-lg border border-white bg-white outline-none text-[12px] shadow-sm font-bold" />
                            </div>
                            <div className="space-y-1">
                              <label className="text-[9px] font-black text-black uppercase tracking-widest">Discount %</label>
                              <input type="text" className="w-full h-8 px-3 rounded-lg border border-white bg-white outline-none text-[12px] shadow-sm" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-3">
                            <textarea placeholder="Sales description" className="w-full h-12 px-3 py-2 rounded-lg border border-white bg-white outline-none text-[11px] shadow-sm resize-none"></textarea>
                            <div className="space-y-1">
                              <label className="text-[9px] font-black text-black uppercase tracking-widest">Account</label>
                              <select className="w-full h-8 px-3 rounded-lg border border-white bg-white outline-none text-[11px] shadow-sm appearance-none">
                                <option>Sales</option>
                              </select>
                            </div>
                          </div>
                        </div>

                        <div className="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-3 shadow-sm relative overflow-hidden">
                          <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2">
                              <input type="checkbox" defaultChecked className="w-4 h-4 rounded border-slate-200 accent-accent text-accent icon-theme shadow-sm" />
                              <span className="text-[11px] font-black uppercase tracking-widest text-black">In Purchase</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <input type="checkbox" defaultChecked className="w-3.5 h-3.5 rounded border-slate-200 accent-accent text-accent icon-theme" />
                              <span className="text-[9px] font-black text-black uppercase tracking-widest">ITC</span>
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-3">
                            <div className="space-y-1">
                              <label className="text-[9px] font-black text-black uppercase tracking-widest flex items-center justify-between">
                                Purchase Rate 
                                <span className="text-accent icon-theme cursor-pointer flex items-center gap-1 relative group/menu">
                                  Recent <Icon name="chevron" className="w-2.5 h-2.5 rotate-90" />
                                  <div className="absolute top-full right-0 mt-1 w-24 bg-white rounded-lg shadow-xl border border-slate-100 py-1 hidden group-hover/menu:block z-50">
                                    <button className="w-full text-left px-3 py-1.5 text-[10px] font-bold text-black hover:bg-slate-50">Default</button>
                                    <button className="w-full text-left px-3 py-1.5 text-[10px] font-bold text-accent icon-theme hover:bg-slate-50">Recent</button>
                                  </div>
                                </span>
                              </label>
                              <div className="text-lg font-black text-slate-800 h-8 flex items-center">0.00</div>
                            </div>
                            <div className="space-y-1">
                              <label className="text-[9px] font-black text-black uppercase tracking-widest">Account</label>
                              <select className="w-full h-8 px-3 rounded-lg border border-white bg-white outline-none text-[11px] shadow-sm appearance-none">
                                <option>Purchase</option>
                              </select>
                            </div>
                          </div>
                          <textarea placeholder="Purchase notes" className="w-full h-12 px-3 py-2 rounded-lg border border-white bg-white outline-none text-[11px] shadow-sm resize-none"></textarea>
                        </div>
                      </div>
                    </div>
                  ) : modalTab === 'Attributes' ? (
                    <div className="animate-in fade-in duration-200 space-y-4">
                      <div className="grid grid-cols-4 gap-3 items-end">
                        <div className="space-y-0.5">
                          <label className="text-[9px] font-black text-black uppercase tracking-widest">Sale Rate</label>
                          <input type="text" placeholder="Sale Rate" className="w-full h-8 bg-slate-50 border border-slate-200 rounded px-2.5 outline-none text-[11px]" />
                        </div>
                        <div className="space-y-0.5">
                          <label className="text-[9px] font-black text-black uppercase tracking-widest">MRP</label>
                          <input type="text" placeholder="MRP" className="w-full h-8 bg-slate-50 border border-slate-200 rounded px-2.5 outline-none text-[11px]" />
                        </div>
                        <div className="space-y-0.5">
                          <label className="text-[9px] font-black text-black uppercase tracking-widest">SKU</label>
                          <input type="text" placeholder="SKU" className="w-full h-8 bg-slate-50 border border-slate-200 rounded px-2.5 outline-none text-[11px]" />
                        </div>
                        <div className="flex gap-1.5">
                          <button className="flex-1 h-8 bg-[#22c55e] text-white rounded font-bold text-[11px]">Add</button>
                          <button className="w-8 h-8 bg-[#ef4444] text-white rounded flex items-center justify-center font-bold">×</button>
                        </div>
                      </div>
                      <div className="border border-slate-100 rounded-lg overflow-hidden shadow-sm">
                        <table className="w-full text-left">
                          <thead className="bg-slate-50/50">
                            <tr>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest">Sale Rate</th>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest text-center">MRP</th>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest text-right">SKU</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td colSpan="3" className="px-3 py-8 text-center text-slate-300 font-bold text-[12px]">No records found</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  ) : (
                    <div className="animate-in fade-in duration-200">
                      <div className="border border-slate-100 rounded-lg overflow-hidden shadow-sm">
                        <table className="w-full text-left">
                          <thead className="bg-slate-50/50">
                            <tr>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest">Rate Sheet Name</th>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest">Base Sales Rate (₹)</th>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest">Rate Sheet Rate (%)</th>
                              <th className="px-3 py-2 text-[9px] font-black text-black uppercase tracking-widest">Rate Sheet Rate (₹)</th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-50">
                            {[
                              { name: 'Retail' },
                              { name: 'Wholesale Retail' }
                            ].map((row, i) => (
                              <tr key={i}>
                                <td className="px-3 py-3 text-[12px] font-bold text-slate-600">{row.name}</td>
                                <td className="px-3 py-3"></td>
                                <td className="px-3 py-3">
                                  <input type="text" className="w-full h-8 bg-slate-50 border border-slate-200 rounded px-2.5 outline-none text-[11px]" />
                                </td>
                                <td className="px-3 py-3">
                                  <input type="text" className="w-full h-8 bg-slate-50 border border-slate-200 rounded px-2.5 outline-none text-[11px]" />
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <>
                {/* Left Column: Basic Info */}
                <div className="w-[55%] p-10 overflow-y-auto no-scrollbar border-r border-[var(--border)] space-y-8 bg-white">
                  <div className="grid grid-cols-2 gap-6">
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">Company Name</label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" />
                    </div>
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">
                        {activeNav === 'Warehouse' ? 'Contact Person' : 
                         activeNav === 'Referrer' ? 'Contact Person' : 'Contact Name'}
                      </label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" />
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-6">
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">Ledger Name <span className="text-red-500">*</span></label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" />
                    </div>
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-slate-400 mb-2 block flex items-center gap-1 uppercase tracking-widest">
                        GSTIN <Icon name="info" className="w-3.5 h-3.5 text-accent icon-theme" />
                      </label>
                      <div className="relative group">
                        <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 pl-11 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" />
                        <Icon name="search" className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-accent icon-theme group-focus-within:scale-110 transition-transform" />
                      </div>
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-6">
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-slate-400 mb-2 block flex items-center gap-1 uppercase tracking-widest">
                        PAN <Icon name="info" className="w-3.5 h-3.5 text-accent icon-theme" />
                      </label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" />
                    </div>
                    <div className="col-span-1 flex items-center gap-2">
                      <div className="flex items-center gap-2.5 mt-6">
                        <input type="checkbox" className="w-5 h-5 rounded border-slate-200 accent-accent text-accent icon-theme focus:ring-accent cursor-pointer" />
                        <label className="text-[11px] font-bold text-slate-600 uppercase tracking-wider flex items-center gap-1">
                          Composition scheme <Icon name="info" className="w-3 h-3 text-accent icon-theme" />
                        </label>
                      </div>
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-6">
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">Contact Mobile</label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" placeholder="+91 00000 00000" />
                    </div>
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">Work Phone</label>
                      <input type="text" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all" placeholder="044-000000" />
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-6">
                    <div className="col-span-1">
                      <div className="flex justify-between items-center mb-2">
                        <label className="text-[11px] font-black text-slate-400 block uppercase tracking-widest">TAG</label>
                        <button className="text-[10px] text-accent icon-theme font-black hover:underline uppercase tracking-tighter">Manage Tags</button>
                      </div>
                      <div className="relative group">
                        <select className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all appearance-none">
                          <option>All</option>
                        </select>
                        <Icon name="chevron" className="absolute right-4 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-slate-400 rotate-90" />
                      </div>
                    </div>
                    <div className="col-span-1">
                      <label className="text-[11px] font-black text-black font-black mb-2 block uppercase tracking-widest">DOB</label>
                      <div className="relative group">
                        <input type="date" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[14px] outline-none focus:border-accent focus:bg-white focus:shadow-md transition-all appearance-none" />
                        <Icon name="calendar" className="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-accent icon-theme pointer-events-none" />
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center justify-between pt-3 border-t border-slate-100">
                    <div className="flex items-center gap-6">
                      <div className="flex items-center gap-3 group cursor-pointer">
                        <input type="checkbox" defaultChecked className="w-5 h-5 rounded border-slate-200 accent-accent text-accent icon-theme focus:ring-accent cursor-pointer" />
                        <span className="text-[14px] font-bold text-slate-600">Active</span>
                        <Icon name="info" className="w-3 h-3 text-slate-400" />
                      </div>
                      <button 
                        onClick={() => fileInputRef.current?.click()}
                        className="p-2 rounded-xl bg-slate-50 text-slate-500 hover:bg-slate-100 transition-all border border-slate-200"
                      >
                        <Icon name="attach" className="w-4.5 h-4.5 text-accent icon-theme" />
                      </button>
                      <input type="file" ref={fileInputRef} className="hidden" />
                    </div>
                  </div>
                </div>

                {/* Right Column: Tabbed Sections */}
                <div className="w-[45%] p-6 bg-slate-50/50">
                  <div className="bg-white rounded-[32px] shadow-2xl border border-slate-100 h-full overflow-hidden flex flex-col">
                    <div className="flex bg-[var(--accent)] p-1 rounded-2xl border border-white/10 shadow-lg shadow-black/5 sticky top-0 z-20 m-4 mb-0">
                      {(activeNav === 'Warehouse' ? ['Basic Details', 'Address', 'Bank Details'] : 
                        activeNav === 'Referrer' ? ['Basic Details', 'Billing Address', 'Bank Details'] :
                        ['Billing Address', 'Shipping Address', 'Bank Details', 'Default']).map(tab => (
                        <button 
                          key={tab}
                          onClick={() => setModalTab(tab)}
                          className={`flex-1 py-2 rounded-xl text-[9px] font-black transition-all uppercase tracking-widest
                            ${modalTab === tab 
                              ? 'bg-white text-[var(--accent)] shadow-md scale-[1.02]' 
                              : 'text-white/60 hover:text-white hover:bg-white/10'}`}
                        >
                          {tab}
                        </button>
                      ))}
                    </div>

                    <div className="p-8 flex-1 overflow-y-auto no-scrollbar">
                      {modalTab === 'Billing Address' && (
                        <div className="space-y-6 animate-in slide-in-from-right-4 duration-200">
                          <div className="grid grid-cols-2 gap-6">
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Address Line 1</label>
                              <input type="text" placeholder="Address1" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none" />
                            </div>
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Address Line 2</label>
                              <input type="text" placeholder="Address2" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-6">
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">City / Town</label>
                              <input type="text" placeholder="City / Town" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none" />
                            </div>
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Postal / Zip Code</label>
                              <input type="text" placeholder="Postal / Zip code" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-6">
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Country</label>
                              <div className="relative group">
                                <select className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none appearance-none">
                                  <option>India</option>
                                </select>
                                <Icon name="chevron" className="absolute right-4 top-1/2 -translate-y-1/2 w-3 h-3 text-slate-400 rotate-90" />
                              </div>
                            </div>
                            <div className="space-y-2">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">State</label>
                              <div className="relative group">
                                <input type="text" defaultValue="Tamil Nadu" className="w-full h-11 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px] outline-none" />
                                <Icon name="close" className="absolute right-4 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-accent icon-theme cursor-pointer" />
                              </div>
                            </div>
                          </div>
                          <div className="pt-4">
                            <Icon name="pin" className="w-5 h-5 text-accent icon-theme" />
                          </div>
                        </div>
                      )}

                      {modalTab === 'Shipping Address' && (
                        <div className="space-y-6 animate-in slide-in-from-right-4 duration-200">
                          <div className="flex items-center justify-end">
                            <div className="flex items-center gap-2 group cursor-pointer">
                              <input type="checkbox" defaultChecked className="w-5 h-5 rounded border-slate-200 accent-accent text-accent icon-theme shadow-sm cursor-pointer" />
                              <span className="text-[12px] font-bold text-slate-500">Same as Billing Address</span>
                            </div>
                          </div>
                          <div className="h-[200px] border-2 border-dashed border-slate-100 rounded-[32px] flex items-center justify-center">
                            <span className="text-[14px] text-slate-300 font-medium">Shipping info matches billing address</span>
                          </div>
                        </div>
                      )}

                      {modalTab === 'Bank Details' && (
                        <div className="space-y-3 animate-in slide-in-from-right-4 duration-200">
                          <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Account Name</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Account Number</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Account Type (Savings / Current)</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Bank Name</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">Bank Branch</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest">IFSC Code</label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-4">
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest flex items-center gap-1.5">Swift Code <Icon name="info" className="w-3.5 h-3.5 text-accent icon-theme" /></label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                            <div className="space-y-1">
                              <label className="text-[10px] font-black text-black uppercase tracking-widest flex items-center gap-1.5">Dealer Code <Icon name="info" className="w-3.5 h-3.5 text-accent icon-theme" /></label>
                              <input type="text" className="w-full h-10 bg-slate-50 border border-slate-200 rounded-xl px-4 text-[13px]" />
                            </div>
                          </div>
                          <div className="space-y-1">
                            <label className="text-[10px] font-black text-black uppercase tracking-widest">Correspondent Bank</label>
                            <textarea className="w-full h-16 bg-slate-50 border border-slate-200 rounded-2xl px-4 py-2 text-[13px] resize-none" />
                          </div>
                        </div>
                      )}

                      {modalTab === 'Default' && (
                        <div className="space-y-6 animate-in slide-in-from-right-4 duration-200">
                          <div className="space-y-2">
                            <label className="text-[10px] font-black text-black uppercase tracking-widest">Notes</label>
                            <textarea placeholder="Notes" className="w-full h-32 bg-slate-50 border border-slate-200 rounded-3xl px-6 py-4 text-[14px] resize-none outline-none focus:bg-white focus:border-accent focus:shadow-md transition-all" />
                          </div>
                          <div className="space-y-2">
                            <label className="text-[10px] font-black text-black uppercase tracking-widest">Terms and Conditions</label>
                            <textarea placeholder="Terms and Conditons" className="w-full h-32 bg-slate-50 border border-slate-200 rounded-3xl px-6 py-4 text-[14px] resize-none outline-none focus:bg-white focus:border-accent focus:shadow-md transition-all" />
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      </Modal>
    </div>
  )
}

export default App
