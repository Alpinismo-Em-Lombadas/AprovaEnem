"""Models do SQLAlchemy: cada classe aqui vira uma tabela no banco.

Importe cada model novo neste arquivo para o Alembic enxergá-lo
na hora de gerar migrations (alembic revision --autogenerate).
"""

from app.database import Base

__all__ = ["Base"]
