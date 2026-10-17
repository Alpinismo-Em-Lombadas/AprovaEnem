# Backlog inicial

Tarefas sugeridas para virar issues, em ordem lógica: as de cima destravam as de baixo. As marcadas com `good first issue` são boas para quem está começando.

Ao criar a issue, use o template **Tarefa**, copie a descrição e detalhe os critérios de pronto.

---

### 1. Explorar os microdados e documentar as colunas que vamos usar
`good first issue` `dados`

Baixar os microdados de um ano (veja `backend/etl/README.md`), abrir uma amostra com o pandas e escrever em `docs/dados.md` quais colunas vamos usar (ano, UF, notas por área, redação etc.) e o que cada uma significa segundo o dicionário de dados do INEP.

### 2. Modelar as tabelas do banco
`dados` `backend`

Com base na tarefa 1, criar os models do SQLAlchemy em `app/models/` (por exemplo, uma tabela de participantes/notas) e gerar a migration com `alembic revision --autogenerate`. Discutir a modelagem na issue antes de implementar.

### 3. Script para importar os microdados de um ano
`dados` `backend`

Criar `backend/etl/importar_ano.py`, que recebe o ano, lê o CSV de `etl/data/<ano>/` em pedaços (`chunksize`), fica só com as colunas da tarefa 1 e grava no banco. Mostrar no terminal quantas linhas foram importadas.

### 4. Gerar uma amostra pequena dos dados para desenvolvimento
`good first issue` `dados`

Script que gera um CSV com poucas milhares de linhas a partir do arquivo completo, para quem não quiser baixar vários GB. Documentar como usar no `etl/README.md`.

### 5. Endpoint de anos disponíveis
`good first issue` `backend`

`GET /anos` retornando a lista de anos que já foram importados no banco. Criar o schema em `app/schemas/`, a consulta em `app/services/` e um teste em `tests/`.

### 6. Endpoint de médias por estado
`backend`

`GET /medias/estados?ano=2023` retornando a média de cada área do conhecimento por UF. A consulta deve ser feita no banco (com `GROUP BY`), não em Python.

### 7. Endpoint de notas por área
`backend`

`GET /notas/areas?ano=2023` retornando, para cada área (Linguagens, Humanas, Natureza, Matemática e Redação), a média, a nota mínima e a nota máxima.

### 8. Página de médias por estado com gráfico
`frontend`

Nova página em `src/pages/` que chama o endpoint da tarefa 6 via `services/api.js` e mostra um gráfico de barras com o Recharts.

### 9. Filtro por ano
`frontend`

Componente de seleção de ano (usando o endpoint da tarefa 5) que atualiza o gráfico da tarefa 8.

### 10. Tabela de notas por área
`good first issue` `frontend`

Componente que mostra os dados do endpoint da tarefa 7 numa tabela simples, com as notas formatadas no padrão brasileiro (vírgula decimal).

### 11. Navegação entre páginas
`frontend`

Adicionar um menu e rotas (por exemplo, com React Router) para navegar entre a página inicial e as páginas de gráficos.

### 12. Estados de carregando e de erro nas telas
`good first issue` `frontend`

Criar componentes reutilizáveis de "Carregando..." e de mensagem de erro, e usar nas páginas que chamam a API.

### 13. Exportar dados para planilha (CSV)
`backend`

`GET /medias/estados.csv?ano=2023` devolvendo os mesmos dados da tarefa 6 em CSV, e um botão "Baixar planilha" na página da tarefa 8.

### 14. Testes dos endpoints com banco de verdade
`backend` `testes`

Configurar os testes para rodar com um Postgres de teste (no CI, como `service` do GitHub Actions), para testar as consultas dos endpoints com dados reais de exemplo.

### 15. Melhorar a página inicial
`good first issue` `frontend`

Explicar o que é o projeto, de onde vêm os dados (INEP) e colocar links para as páginas de gráficos.
