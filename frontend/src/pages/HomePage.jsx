import ApiStatus from '../components/ApiStatus'

function HomePage() {
  return (
    <main className="home">
      <h1>AprovaEnem</h1>
      <p>Dados públicos do Enem organizados para quem vai fazer a prova.</p>
      <ApiStatus />
    </main>
  )
}

export default HomePage
