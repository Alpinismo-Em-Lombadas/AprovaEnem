# Como contribuir

Este guia é o fluxo do time, passo a passo. Se ainda não rodou o projeto, comece pelo [README](README.md).

Regra de ouro: **ninguém faz commit direto na `main`**. Toda mudança entra por Pull Request (PR) revisado.

## 1. Pegue uma issue

1. Vá na aba **Issues** do repositório. As marcadas com `good first issue` são boas para começar.
2. Escolha uma que ninguém esteja fazendo (campo **Assignees** vazio).
3. Atribua a issue a você em **Assignees > assign yourself** e comente que vai pegar.
4. Ficou com dúvida sobre a tarefa? Pergunte nos comentários da issue antes de começar.

## 2. Atualize a `main` e crie sua branch

Sempre crie a branch a partir da `main` atualizada:

```bash
git checkout main
git pull origin main
git checkout -b feat/nome-curto
```

Nome da branch:

- `feat/nome-curto` para funcionalidade nova (ex.: `feat/endpoint-medias-estado`)
- `fix/nome-curto` para correção de bug (ex.: `fix/cors-frontend`)
- `docs/nome-curto` para documentação
- `chore/nome-curto` para configuração e manutenção

Use letras minúsculas, sem acento e com hífen no lugar de espaço.

## 3. Faça commits pequenos e no padrão

Seguimos o [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `tipo: descrição curta no presente`.

| Tipo | Quando usar | Exemplo |
| --- | --- | --- |
| `feat` | funcionalidade nova | `feat: adiciona endpoint de médias por estado` |
| `fix` | correção de bug | `fix: corrige cálculo da média de matemática` |
| `docs` | só documentação | `docs: explica como importar os microdados` |
| `test` | testes | `test: adiciona teste do endpoint de notas` |
| `refactor` | melhora o código sem mudar o comportamento | `refactor: move consulta para services` |
| `chore` | configuração, dependências, CI | `chore: atualiza versão do pandas` |

```bash
git status                  # veja o que mudou
git add caminho/do/arquivo  # adicione só o que faz parte da tarefa
git commit -m "feat: adiciona endpoint de médias por estado"
```

Prefira vários commits pequenos a um commit gigante. Cada commit deve fazer uma coisa só.

## 4. Confira antes de enviar

O CI vai rodar essas verificações no seu PR. Rode antes na sua máquina para não ter surpresa:

```bash
# backend (dentro de backend/, com o venv ativado)
ruff check .
ruff format .
pytest

# frontend (dentro de frontend/)
npm run lint
npm run build
```

## 5. Envie a branch e abra o PR

```bash
git push -u origin feat/nome-curto
```

1. O GitHub mostra um botão **Compare & pull request**. Clique nele (ou vá em **Pull requests > New pull request**).
2. Base: `main`. Compare: a sua branch.
3. Preencha o template: o que foi feito, como testar, e escreva `Closes #numero-da-issue` para a issue fechar sozinha no merge.
4. Marque o checklist.

## 6. Peça review

1. No PR, em **Reviewers**, escolha pelo menos uma pessoa do time.
2. Avise no grupo que tem PR esperando revisão.
3. Se pedirem mudanças, corrija **na mesma branch** e envie de novo. O PR atualiza sozinho:

```bash
git add .
git commit -m "fix: ajusta nomes conforme review"
git push
```

Revisando o PR de alguém? Seja gentil e específico: diga o que mudar e por quê. Elogiar o que ficou bom também conta.

## 7. Merge só depois de aprovado

- O merge só acontece com **pelo menos uma aprovação** e o **CI verde**.
- Use **Squash and merge**.
- Depois do merge, apague a branch no GitHub (botão **Delete branch**) e atualize sua máquina:

```bash
git checkout main
git pull origin main
git branch -d feat/nome-curto
```

### A `main` andou enquanto eu trabalhava

Se o GitHub disser que sua branch está desatualizada ou tem conflitos:

```bash
git checkout main
git pull origin main
git checkout feat/nome-curto
git merge main
# resolva os conflitos nos arquivos marcados, depois:
git add .
git commit
git push
```

Travou num conflito? Peça ajuda no grupo, é normal.

## Deu erro? Comece por aqui

### `port is already allocated` / `address already in use`

Outro programa (ou outro projeto) já está usando a porta.

- Veja quem está usando: `lsof -i :8000` (macOS/Linux) ou `netstat -ano | findstr :8000` (Windows).
- Se for um container antigo deste projeto: `docker compose down`.
- Se for outro projeto que você precisa manter rodando, mude a porta no seu `.env` (`DB_PORT`, `API_PORT` ou `WEB_PORT`) e ajuste também `CORS_ORIGINS` e o `VITE_API_URL` do `frontend/.env`, como explicam os comentários do `.env.example`.
- Lembre: não rode o modo Docker e o modo desenvolvimento ao mesmo tempo.

### `Cannot connect to the Docker daemon` / `docker: command not found`

O Docker Desktop está fechado. Abra o Docker Desktop, espere o ícone ficar verde ("Engine running") e rode o comando de novo.

### Mudei o `requirements.txt` ou o `package.json` e nada mudou

Faltou o `--build`. As dependências são instaladas na hora de construir a imagem:

```bash
docker compose up --build
```

Se mesmo assim o frontend não enxergar um pacote novo, recrie o volume do `node_modules`:

```bash
docker compose down
docker compose up --build --renew-anon-volumes
```

### `env file .env not found`

Você esqueceu de criar o `.env`: `cp .env.example .env` na raiz do projeto.

### Erro de CORS no console do navegador

Mensagem parecida com `blocked by CORS policy`. A API só aceita chamadas dos endereços listados em `CORS_ORIGINS` no `.env`.

- Confira se o endereço que aparece no navegador (ex.: `http://localhost:5173`) está em `CORS_ORIGINS`, exatamente igual (sem barra no final).
- Depois de mudar o `.env`, reinicie a API (`docker compose up` de novo, ou pare e rode o `uvicorn` de novo).
- Às vezes o "erro de CORS" esconde outro problema: se a API caiu com erro, o navegador também reclama de CORS. Olhe o log da API (`docker compose logs api`).

### A tela mostra "API: fora do ar"

1. A API está rodando? Abra <http://localhost:8000/health>.
2. Se `/health` responde `503`, a API não consegue falar com o banco: veja se o `db` está de pé (`docker compose ps`).
3. No modo desenvolvimento, confira se o `frontend/.env` existe e aponta para `http://localhost:8000`.

### `ModuleNotFoundError` no Python

O venv não está ativado ou faltou instalar as dependências. Dentro de `backend/`:

```bash
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Rode os comandos (`uvicorn`, `pytest`, `alembic`) sempre de dentro da pasta `backend/`.

### `password authentication failed` no banco

O banco foi criado da primeira vez com outra senha e guardou ela no volume. Se não tem nada importante no banco, recrie:

```bash
docker compose down -v
docker compose up --build
```

### Nada disso resolveu

Abra uma issue usando o template **Bug**, com o erro completo e o passo a passo para reproduzir, ou pergunte no grupo.
