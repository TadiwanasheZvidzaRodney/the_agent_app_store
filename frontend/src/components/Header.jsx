import { Link } from 'react-router-dom'
import logo from '../assets/logo.svg'

export default function Header() {
  return (
    <header className="dashboard-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <img src={logo} alt="Agent App Store Logo" width="40" height="40" />
        <h1 style={{ margin: 0 }}>Agent Control Center</h1>
      </div>
      <Link to="/" style={{ color: 'var(--text-h)', display: 'flex', alignItems: 'center', gap: '8px', textDecoration: 'none', fontWeight: '500', padding: '8px 16px', borderRadius: '8px', background: 'var(--code-bg)', border: '1px solid var(--border)', transition: 'border-color 0.2s' }} onMouseOver={(e) => e.currentTarget.style.borderColor = 'var(--accent)'} onMouseOut={(e) => e.currentTarget.style.borderColor = 'var(--border)'}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
          <polyline points="9 22 9 12 15 12 15 22"></polyline>
        </svg>
        Home
      </Link>
    </header>
  )
}
