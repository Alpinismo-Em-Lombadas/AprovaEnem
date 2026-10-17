# AprovaEnem

O AprovaEnem pega os dados públicos do Enem (microdados do INEP), organiza num banco de dados e mostra tudo em gráficos e planilhas para ajudar quem vai fazer a prova.
É um projeto colaborativo feito por devs iniciantes que estão aprendendo enquanto constroem juntos.

## Stack

| Parte | Tecnologias |
| --- | --- |
| Backend | Python 3.12, FastAPI, Uvicorn, SQLAlchemy 2, Alembic, Pydantic Settings |
| Dados | pandas (scripts de importação dos microdados) |
| Frontend | React + Vite (JavaScript), Recharts para gráficos |
| Banco | PostgreSQL 16 |
| Infra | Docker e Docker Compose |
| Qualidade | Ruff e pytest (backend), ESLint (frontend), GitHub Actions (CI) |

## Pré-requisitos

- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (já vem com o Docker Compose)
- [Python 3.12](https://www.python.org/downloads/) (só para o modo desenvolvimento)
- [Node.js](https://nodejs.org/) versão 22 ou mais nova, que já vem com o npm (só para o modo desenvolvimento)

## Primeiro passo: clonar e criar o `.env`

```bash
git clone git@github.com:Projetos-Any/AprovaEnem.git
cd AprovaEnem
cp .env.example .env
```

O `.env` guarda as senhas e configurações da sua máquina. Ele **não vai para o Git**. No Windows (PowerShell), use `copy .env.example .env`.

## Jeito 1: rodar tudo com Docker (mais fácil)

```bash
docker compose up --build
```

Isso sobe três serviços:

| Serviço | O que é | Endereço |
| --- | --- | --- |
| `db` | PostgreSQL | `localhost:5432` |
| `api` | Backend FastAPI | <http://localhost:8000> (documentação em <http://localhost:8000/docs>) |
| `web` | Frontend React | <http://localhost:5173> |

Abra <http://localhost:5173>. Se aparecer **"API: ok"**, está tudo funcionando.

- Para parar: `Ctrl + C` no terminal, ou `docker compose down`.
- Alterações no código recarregam sozinhas. Só rode `--build` de novo quando mudar dependências (`requirements.txt` ou `package.json`).
- Para apagar também os dados do banco: `docker compose down -v`.

## Jeito 2: modo desenvolvimento (banco no Docker, código na sua máquina)

Útil para usar o debugger do editor e ver os erros mais de perto. Use **três terminais**.

**Terminal 1: só o banco**

```bash
docker compose up db
```

**Terminal 2: API**

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head             # aplica as migrations no banco
uvicorn app.main:app --reload
```

Nas próximas vezes, basta `source .venv/bin/activate` e `uvicorn app.main:app --reload`.

**Terminal 3: frontend**

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

> Não rode o Jeito 1 e o Jeito 2 ao mesmo tempo: os dois usam as mesmas portas.

## Comandos úteis

| O que | Onde | Comando |
| --- | --- | --- |
| Lint do backend | `backend/` | `ruff check .` |
| Formatar o backend | `backend/` | `ruff format .` |
| Testes do backend | `backend/` | `pytest` |
| Nova migration | `backend/` | `alembic revision --autogenerate -m "descricao"` |
| Lint do frontend | `frontend/` | `npm run lint` |
| Build do frontend | `frontend/` | `npm run build` |

Com Docker, rode os comandos do backend dentro do container: `docker compose exec api pytest`.

## Estrutura de pastas

```
AprovaEnem/
├── docker-compose.yml      # sobe banco, API e frontend juntos
├── .env.example            # modelo das variáveis de ambiente (copie para .env)
├── CONTRIBUTING.md         # como contribuir: issues, branches, commits e PRs
├── .github/                # templates de issue e PR, e o CI (workflows/ci.yml)
├── docs/backlog.md         # tarefas iniciais sugeridas para virar issues
├── backend/
│   ├── requirements.txt    # dependências Python
│   ├── alembic/            # migrations do banco (histórico de mudanças nas tabelas)
│   ├── app/
│   │   ├── main.py         # cria a aplicação FastAPI e registra as rotas
│   │   ├── config.py       # lê as configurações do .env
│   │   ├── database.py     # conexão com o banco (engine e sessão)
│   │   ├── routers/        # endpoints da API, um arquivo por assunto
│   │   ├── models/         # tabelas do banco (SQLAlchemy)
│   │   ├── schemas/        # formato dos dados que entram e saem da API (Pydantic)
│   │   └── services/       # regras de negócio e consultas
│   ├── etl/                # scripts para importar os microdados (veja etl/README.md)
│   └── tests/              # testes automatizados (pytest)
└── frontend/
    ├── .env.example        # endereço da API usado pelo frontend
    └── src/
        ├── App.jsx         # componente raiz
        ├── services/api.js # único lugar que conversa com a API
        ├── pages/          # páginas inteiras (ex.: HomePage)
        └── components/     # pedaços reutilizáveis de tela
```

## Quer contribuir?

Leia o [CONTRIBUTING.md](CONTRIBUTING.md): lá está o passo a passo para pegar uma tarefa e abrir seu primeiro Pull Request, e também o que fazer quando algo dá errado.
