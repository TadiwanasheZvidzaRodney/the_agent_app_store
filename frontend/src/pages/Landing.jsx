import { Link } from 'react-router-dom'
import logo from '../assets/logo.svg'
import './Landing.css'

export default function Landing() {
  return (
    <div className="landing-container">
      {/* Navigation */}
      <nav className="startup-nav">
        <div className="nav-brand">
          <img src={logo} alt="The Hub Logo" width="32" height="32" />
          <span>The Hub</span>
        </div>
        <div className="nav-links">
          <a href="#features">Features</a>
          <a href="#about">About</a>
          <Link to="/dashboard" className="nav-cta">Go to Dashboard</Link>
        </div>
      </nav>
      
      {/* Hero Section */}
      <section className="startup-hero">
        <div className="hero-glow"></div>
        <div className="hero-content">
          <div className="hero-badge">✨ Version 1.0 is live</div>
          <h1 className="hero-title">
            The Ultimate <span className="text-gradient">AI Agent</span> Ecosystem
          </h1>
          <p className="hero-subtitle">
            Deploy, manage, and scale intelligent personas directly to Telegram. Bring your custom AI agents to life in seconds.
          </p>
          <div className="hero-actions">
            <Link to="/dashboard" className="primary-btn">
              Get Started Free
            </Link>
            <a href="#features" className="secondary-btn">
              Learn More
            </a>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="startup-features">
        <div className="section-header">
          <h2>Everything you need to scale AI</h2>
          <p>Powerful tools designed for creators and developers.</p>
        </div>
        
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🚀</div>
            <h3>One-Click Deploy</h3>
            <p>Push your custom agents instantly to Telegram without touching any infrastructure code.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🧠</div>
            <h3>Multi-Model Support</h3>
            <p>Seamlessly switch between Llama 3, Gemini, and other cutting-edge LLMs on the fly.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">💬</div>
            <h3>Persistent Memory</h3>
            <p>Agents remember past interactions, providing a highly contextual and personalized experience.</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="startup-footer">
        <div className="footer-content">
          <div className="footer-brand">
            <img src={logo} alt="The Hub Logo" width="24" height="24" />
            <span>The Hub © 2026</span>
          </div>
          <div className="footer-links">
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
          </div>
        </div>
      </footer>
    </div>
  )
}
