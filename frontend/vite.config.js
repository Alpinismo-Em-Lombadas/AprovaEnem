import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react()],
  server: {
    // host: true (o mesmo que --host) deixa o Vite acessível de fora do container
    host: true,
    port: 5173,
  },
})
