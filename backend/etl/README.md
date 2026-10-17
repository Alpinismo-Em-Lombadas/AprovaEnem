# ETL dos microdados do Enem

**ETL** = *Extract, Transform, Load* (extrair, transformar, carregar). É o caminho que os dados fazem do arquivo do INEP até o nosso banco:

1. **Extrair**: ler o CSV dos microdados com o pandas.
2. **Transformar**: ficar só com as colunas que usamos, renomear, tratar valores vazios, corrigir tipos.
3. **Carregar**: gravar o resultado nas tabelas do PostgreSQL (definidas em `app/models/`).

Os scripts desta pasta ainda não existem: criar o primeiro é uma das tarefas do [backlog](../../docs/backlog.md).

## 1. Baixar os microdados

1. Acesse o portal do INEP: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem>
2. Baixe o `.zip` do ano que você vai trabalhar (ex.: `microdados_enem_2023.zip`).
3. Descompacte. Dentro da pasta `DADOS/` fica o CSV com os dados dos participantes. Ao lado vêm o **dicionário de dados** (planilha que explica cada coluna) e outros documentos: leia o dicionário antes de escrever código.

> O arquivo é grande (alguns GB descompactado). Comece testando com poucas linhas, por exemplo `pd.read_csv(..., nrows=1000)`.

## 2. Onde colocar os arquivos

Coloque os CSVs em `backend/etl/data/`, separados por ano:

```
backend/etl/data/
└── 2023/
    └── MICRODADOS_ENEM_2023.csv
```

Essa pasta está no `.gitignore`: **os microdados nunca vão para o GitHub**. Cada pessoa baixa na própria máquina.

## 3. Dicas para ler o CSV

Os arquivos do INEP costumam usar `;` como separador e codificação `latin-1`. Um ponto de partida:

```python
import pandas as pd

df = pd.read_csv(
    "etl/data/2023/MICRODADOS_ENEM_2023.csv",
    sep=";",
    encoding="latin-1",
    usecols=["NU_ANO", "SG_UF_PROVA", "NU_NOTA_MT"],  # só o que você precisa
    nrows=1000,
)
```

Os nomes de colunas e o formato podem mudar de um ano para outro: confira sempre o dicionário de dados do ano que você baixou.

## 4. Como rodar um script

Com o banco no ar (`docker compose up db`) e o venv ativado, a partir da pasta `backend/`:

```bash
python -m etl.nome_do_script
```

Rodar com `-m` a partir de `backend/` faz o Python encontrar o pacote `app` (para reaproveitar `app.database` e os models).
