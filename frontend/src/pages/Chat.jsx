import { useState, useEffect, useRef } from 'react'
import { useParams, Link } from 'react-router-dom'
import Header from '../components/Header'
import '../App.css'

export default function Chat() {
  const { agentId } = useParams()
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [sessionId, setSessionId] = useState(null)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async (e) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage = { role: 'user', content: input }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      const res = await fetch(`${baseUrl}/api/agents/${agentId}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: userMessage.content,
          session_id: sessionId
        })
      })
      const data = await res.json()

      if (data.session_id) {
        setSessionId(data.session_id)
      }

      setMessages(prev => [...prev, { role: 'assistant', content: data.reply }])
    } catch (err) {
      console.error(err)
      setMessages(prev => [...prev, { role: 'assistant', content: 'Error communicating with agent.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="dashboard" style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Header />
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', maxWidth: '800px', margin: '0 auto', width: '100%', padding: '24px' }}>
        <div style={{ marginBottom: '16px' }}>
          <Link to="/dashboard" style={{ color: 'var(--text)', textDecoration: 'none' }}>← Back to Dashboard</Link>
        </div>

        <div style={{ flex: 1, overflowY: 'auto', background: 'var(--code-bg)', borderRadius: '12px', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px', border: '1px solid var(--border)' }}>
          {messages.length === 0 ? (
            <div style={{ margin: 'auto', color: 'var(--text)', textAlign: 'center' }}>
              <h3>Start a conversation</h3>
              <p>Send a message to begin chatting with this agent.</p>
            </div>
          ) : (
            messages.map((msg, i) => (
              <div key={i} style={{ alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start', maxWidth: '80%', background: msg.role === 'user' ? 'var(--accent)' : 'var(--bg)', color: msg.role === 'user' ? 'white' : 'var(--text-h)', padding: '12px 16px', borderRadius: '12px', border: msg.role === 'user' ? 'none' : '1px solid var(--border)' }}>
                {msg.content}
              </div>
            ))
          )}
          {loading && <div style={{ alignSelf: 'flex-start', padding: '12px 16px', color: 'var(--text)' }}>Let me think...</div>}
          <div ref={messagesEndRef} />
        </div>

        <form onSubmit={sendMessage} style={{ marginTop: '16px', display: 'flex', gap: '8px' }}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            style={{ flex: 1, padding: '16px', borderRadius: '8px', border: '1px solid var(--border)', background: 'var(--code-bg)', color: 'var(--text-h)' }}
          />
          <button type="submit" disabled={loading} style={{ background: 'var(--accent)', color: 'white', border: 'none', borderRadius: '8px', padding: '0 24px', fontWeight: 'bold', cursor: 'pointer' }}>
            Send
          </button>
        </form>
      </main>
    </div>
  )
}
