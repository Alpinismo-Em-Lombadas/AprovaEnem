from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import health

app = FastAPI(
    title="AprovaEnem API",
    description="Dados públicos do Enem organizados para quem vai fazer a prova.",
    version="0.1.0",
)

# Sem isso o navegador bloqueia as chamadas do frontend (outra porta = outra origem).
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
