FROM python:3.12-slim

WORKDIR /app

# Copiamos só o requirements.txt primeiro para o Docker reaproveitar o cache
# das dependências quando apenas o código mudar.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Aplica as migrations e sobe a API com recarregamento automático.
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
