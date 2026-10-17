// Único lugar do frontend que sabe o endereço da API.
// Componentes e páginas devem importar as funções daqui, nunca usar fetch direto.
const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

async function get(path) {
  const response = await fetch(`${API_URL}${path}`)
  if (!response.ok) {
    throw new Error(`Erro ${response.status} ao chamar ${path}`)
  }
  return response.json()
}

export function getHealth() {
  return get('/health')
}
