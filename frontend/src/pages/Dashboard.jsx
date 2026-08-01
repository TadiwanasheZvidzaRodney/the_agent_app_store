import { useState, useEffect } from 'react'
import Header from '../components/Header'
import AgentForm from '../components/AgentForm'
import AgentGrid from '../components/AgentGrid'
import '../App.css'

const API_URL = 'http://localhost:8000/api/agents'

export default function Dashboard() {
  const [agents, setAgents] = useState([])
  const [loading, setLoading] = useState(true)

  const fetchAgents = async () => {
    try {
      const res = await fetch(API_URL)
      const data = await res.json()
      setAgents(data)
    } catch (err) {
      console.error("Failed to fetch agents:", err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchAgents()
  }, [])

  const systemAgents = agents.filter(a => a.is_system)
  const customAgents = agents.filter(a => !a.is_system)

  return (
    <div className="dashboard">
      <Header />
      
      {systemAgents.length > 0 && (
        <section className="system-agents-tabs" style={{ marginBottom: '32px' }}>
          <h2 style={{ marginBottom: '16px' }}>Core System Agents</h2>
          <div className="tabs-container" style={{ display: 'flex', gap: '16px', overflowX: 'auto', paddingBottom: '8px' }}>
            {systemAgents.map(agent => (
              <div key={agent.id} className="agent-tab" style={{ background: 'var(--accent-bg)', padding: '20px', borderRadius: '12px', border: '1px solid var(--accent-border)', minWidth: '300px', transition: 'transform 0.2s' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px', alignItems: 'center' }}>
                  <h3 style={{ margin: 0, fontSize: '18px', color: 'var(--text-h)' }}>{agent.name}</h3>
                  <span className="badge" style={{ background: 'var(--accent)', color: 'white', fontWeight: 'bold' }}>SYSTEM</span>
                </div>
                <p style={{ fontSize: '14px', color: 'var(--text)', margin: '0 0 16px 0', lineHeight: '1.4' }}>{agent.description}</p>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span className="voice-tag">🎤 {agent.voice_type}</span>
                  <span className="badge">{agent.llm_model}</span>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      <main className="dashboard-layout">
        <AgentForm onAgentCreated={fetchAgents} />
        <AgentGrid agents={customAgents} loading={loading} />
      </main>
    </div>
  )
}
