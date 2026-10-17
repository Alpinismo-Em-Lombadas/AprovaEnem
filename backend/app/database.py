from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

# pool_pre_ping testa a conexão antes de usar, evitando erro se o banco reiniciou.
engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """Classe base de todos os models. O Alembic usa ela para achar as tabelas."""


def get_db() -> Generator[Session]:
    """Abre uma sessão por requisição e garante que ela seja fechada no final.

    Use nos endpoints com: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
