export default function AgentGrid({ agents, loading }) {
  return (
    <section className="grid-section">
      <h2>Active Agents</h2>
      {loading ? (
        <p className="loading">Fetching agents...</p>
      ) : agents.length === 0 ? (
        <p className="empty-state">No agents deployed yet. Create your first one!</p>
      ) : (
        <div className="agents-grid">
          {agents.map((agent) => (
            <div key={agent.id} className={`agent-card ${agent.isActive ? 'active' : 'inactive'}`}>
              <div className="card-header">
                <h3>{agent.name}</h3>
                <span className="badge">{agent.llm_model}</span>
              </div>
              <p className="card-desc">{agent.description || 'No description provided.'}</p>
              <div className="card-footer">
                <span className="voice-tag">🎤 {agent.voice_type}</span>
                <span className={`status-dot ${agent.isActive ? 'live' : 'offline'}`}></span>
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  )
}
