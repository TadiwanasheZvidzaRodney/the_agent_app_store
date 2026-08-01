import logo from '../assets/logo.svg'

export default function Hero() {
  return (
    <section id="center" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2rem', padding: '4rem 1rem' }}>
      <div className="hero" style={{ position: 'relative' }}>
        {/* Glow effect behind the logo */}
        <div style={{ position: 'absolute', inset: 0, background: '#aa3bff', filter: 'blur(60px)', opacity: 0.3, borderRadius: '50%' }}></div>
        <img src={logo} alt="Agent App Store Logo" style={{ width: '180px', height: '180px', position: 'relative', zIndex: 1, filter: 'drop-shadow(0 0 20px rgba(170, 59, 255, 0.4))' }} />
      </div>
      <div style={{ textAlign: 'center' }}>
        <h1 style={{ fontSize: '4rem', fontWeight: '800', letterSpacing: '-1.5px', margin: '0 0 1rem 0', background: 'linear-gradient(135deg, #ffffff 0%, #aa3bff 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          The Agent App Store
        </h1>
        <p style={{ fontSize: '1.25rem', color: '#a0a0a0', maxWidth: '600px', margin: '0 auto', lineHeight: '1.6' }}>
          Browse, interact, and deploy next-generation AI personas seamlessly.
        </p>
      </div>
      <button
        type="button"
        style={{
          background: 'linear-gradient(135deg, #aa3bff 0%, #7a1fd6 100%)',
          color: 'white',
          border: 'none',
          padding: '1rem 2.5rem',
          borderRadius: '50px',
          fontSize: '1.1rem',
          fontWeight: '600',
          cursor: 'pointer',
          boxShadow: '0 10px 30px -10px rgba(170, 59, 255, 0.6)',
          transition: 'all 0.3s ease'
        }}
        onMouseOver={(e) => {
          e.currentTarget.style.transform = 'translateY(-2px)'
          e.currentTarget.style.boxShadow = '0 15px 40px -10px rgba(170, 59, 255, 0.8)'
        }}
        onMouseOut={(e) => {
          e.currentTarget.style.transform = 'translateY(0)'
          e.currentTarget.style.boxShadow = '0 10px 30px -10px rgba(170, 59, 255, 0.6)'
        }}
      >
        Explore Agents
      </button>
    </section>
  )
}
