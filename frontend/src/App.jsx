import Hero from './components/Hero'
import Docs from './components/Docs'
import Social from './components/Social'
import './App.css'

function App() {
  return (
    <>
      <Hero />
      <div className="ticks"></div>
      <section id="next-steps">
        <Docs />
        <Social />
      </section>
      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
