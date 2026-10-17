import { useEffect, useState } from 'react'
import { getHealth } from '../services/api'

function ApiStatus() {
  const [status, setStatus] = useState('carregando...')

  useEffect(() => {
    getHealth()
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('fora do ar'))
  }, [])

  return <p className="api-status">API: {status}</p>
}

export default ApiStatus
