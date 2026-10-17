import os

# Valores falsos só para os testes conseguirem carregar as configurações
# mesmo sem um arquivo .env (como acontece no CI).
os.environ.setdefault("POSTGRES_USER", "test")
os.environ.setdefault("POSTGRES_PASSWORD", "test")
os.environ.setdefault("POSTGRES_DB", "test")
