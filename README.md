<img width="1259" height="323" alt="image" src="https://github.com/user-attachments/assets/812e3dec-05cb-43b3-9e83-945c8c9126df" />

# Tech Challenge FASE 03 - API: Vitivinicultura da Embrapa 

# 📂 Problema de negócio

Você foi contratado para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa. A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:
  - Produção;
  - Processamento;
  - Comercialização;
  - Importação;
  - Exportação.
    
Objetivos do projeto

  -  Criar uma Rest API em Python que faça a consulta no site da Embrapa.
  -  Sua API deve estar documentada.
  - É recomendável (não obrigatório) a escolha de um método deautenticação (JWT, por exemplo).
  - Criar um plano para fazer o deploy da API, desenhando a arquiteturado projeto desde a ingestão até a alimentação do modelo.
  -  Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.
 
# 📡 API de Dados da Vitivinicultura Embrapa

Este projeto tem como objetivo criar uma API pública RESTful, com autenticação via JWT, que extrai, trata e disponibiliza dados da vitivinicultura brasileira diretamente do site da Embrapa (Vitibrasil). A API alimenta um modelo de Machine Learning que estima a produção futura de vinhos no Brasil para os próximos 5 anos.

---

## 🧱 Arquitetura do Projeto

A seguir, apresentamos a arquitetura completa do sistema desenvolvido:

Arquitetura do Projeto 
<img width="1223" alt="image" src="https://github.com/user-attachments/assets/8a22867c-a3e3-4388-b013-af7bee1a8a31" />


### 🔄 Etapas da Arquitetura:

1. **Extração de Dados – Web Scraping**  
   - Utiliza **Selenium** e **BeautifulSoup** para extrair dados de páginas HTML com conteúdo dinâmico.
   - Devido à instabilidade do site da Vitivinicultura, o script em Python foi desenvolvido para acessar diretamente as abas de Produção, Processamento, Comercialização, Importação e Exportação, realizando o download dos arquivos CSV. Esses arquivos são então tratados e limpos antes de serem persistidos no banco de dados, garantindo a integridade e a padronização dos dados. 

2. **Limpeza e Processamento – Pandas**  
   - Os dados brutos são transformados com `pandas`, eliminando ruídos como rodapés, cabeçalhos duplicados, e valores nulos.
   - Os dados são convertidos para formatos numéricos e padronizados para persistência.

3. **Persistência – PostgreSQL**  
   - Os dados tratados são salvos em tabelas normalizadas em um banco relacional PostgreSQL.
   - A modelagem segue boas práticas de integridade referencial, pronta para uso por sistemas externos ou pipelines de ML.

4. **Lógica de Negócio – FastAPI + JWT**  
   - API construída com **FastAPI**, oferece endpoints segmentados e protegidos por **autenticação JWT**.
   - Estrutura modular, fácil de escalar e manter.

5. **Versionamento – GitHub**  
   - Todo o código está versionado em repositório Git, com organização por módulos (scraping, modelos, rotas, schemas, etc).

6. **Deploy – Render + Streamlit**  
   - O backend (API) é hospedado na **Render**.
   - O frontend é construído com **Streamlit**, fornecendo visualização interativa dos dados (gráficos, filtros, login, etc).


## 📁 Estrutura do Projeto

A estrutura do projeto foi organizada para garantir **modularidade**, **clareza** e **escalabilidade**:

```
TechChallengeAPI/
│
├── api/
│   └── v1/
│       ├── endpoints/
│       │   ├── comercializacao.py
│       │   ├── exportacao.py
│       │   ├── importacao.py
│       │   ├── processamento.py
│       │   ├── producao.py
│       │   ├── sintese.py                
│       │   └── user.py
│       └── api.py
│
├── core/
│   ├── auth.py
│   ├── database.py
│   ├── deps.py
│   ├── security.py
│   └── settings.py
│
├── models/
│   ├── __all_models__.py
│   ├── comercializacao_model.py
│   ├── exportacao_model.py
│   ├── importacao_model.py
│   ├── processamento_model.py
│   ├── producao_model.py
│   └── user_model.py
│
├── data_process/
│   ├── comercializacao_clear.py
│   ├── exportacao_clear.py
│   ├── importacao_clear.py
│   ├── processamento_clear.py
│   ├── producao_clear.py
│   ├── web_scraping.py
│   ├── load_all.py
│   └── data_scraping/
│
├── schemas/
│   ├── comercializacao_schema.py
│   ├── exportacao_schema.py
│   ├── importacao_schema.py
│   ├── processamento_schema.py
│   ├── producao_schema.py
│   └── user_schema.py
│
├── create_tables.py
├── create_views_previsoes.py      
├── streamlit.py                   
├── main.py
├── requirements.txt
└── README.md



```

### 🔍 Organização por responsabilidades

- **api/**: Define os endpoints REST e o roteamento geral da API.
- **core/**: Contém configurações centrais, autenticação, dependências e segurança.
- **models/**: Define os modelos ORM (SQLAlchemy) correspondentes às tabelas no banco de dados.
- **schemas/**: Schemas Pydantic usados para validação e serialização de dados.
- **data_process/**: Scripts responsáveis por limpar, transformar e carregar os dados.
- **data_scraping/**: Pasta que armazenda os dados que foram extraídos via selenium e beatifulsoap .
- **main.py**: Ponto de entrada da aplicação FastAPI.
- **create_table.py**: Script resposável pela criação e persistência das tabelas no banco de dados.
- **requirements.txt**: Lista de dependências do projeto.
- **create_views_previsoes.py**: Script responsável por criar e atualizar a view SQL vw_previsoes, que consolida os dados históricos de produção, processamento, comercialização, importação e exportação da vitivinicultura brasileira. 
---

## 🤖 Preparação para Machine Learning

A estrutura foi pensada para garantir:

- Consistência e padronização nos dados;
- Disponibilidade via API RESTful;
- Segurança com autenticação JWT;
- Facilidade de ingestão para pipelines de ML.

---


## 📊 Interface de Visualização

O projeto conta com um **frontend desenvolvido em Streamlit**, que permite:

- Login autenticado com token JWT
- Escolha da categoria (Produção, Importação, etc.)
- Filtros por ano, produto ou país
- Aba de previsões
- Visualização por:
  - Tabela interativa
  - Gráficos de barras, linhas, top 5, pareto e comparações
- Exportação dos dados filtrados em CSV, Excel ou JSON

### Exemplo da interface:
<img width="965" height="312" alt="image" src="https://github.com/user-attachments/assets/8edf580a-901b-4ce8-9f18-7a243f5eb14a" />

---

<img width="1237" height="253" alt="image" src="https://github.com/user-attachments/assets/171f270f-836a-467d-880c-350aa45a5fdf" />



## 📈 Análise Exploratória dos Dados (EDA)

Antes de alimentar os dashboards e modelos de machine learning, foi realizada uma **Análise Exploratória de Dados (EDA)**, utilizando bibliotecas como `pandas`, `matplotlib` e `plotly`.

A EDA em sua essência tem como objetivos principais:

- Verificar **distribuições temporais** (ex: volume de importação por ano)
- Identificar **outliers** e possíveis inconsistências
- Analisar **tendências por tipo de produto e país**
- Medir **ausência de dados** (valores nulos) e corrigir colunas incompletas
- Preparar os dados com agregações e filtros otimizados para os dashboards

No caso do nosso projeto, os insights gerados orientaram:
- A escolha de filtros por **ano**, **produto** e **país**;
- A separação das abas no dashboard;
- A modelagem dos dados para futura análise preditiva e agrupamentos.

### Exemplo de visualização da EDA:


<img width="931" height="270" alt="image" src="https://github.com/user-attachments/assets/c800d2cc-cea3-496c-a8c0-425cbbb988d6" />


---

<img width="989" height="242" alt="image" src="https://github.com/user-attachments/assets/832a81c4-eb11-4668-b92b-75f8a9895726" />



---

## 🧭 Endpoints Disponíveis

A API oferece múltiplos endpoints organizados por módulos, todos protegidos por autenticação JWT:

### 🔐 Autenticação & Usuários (`/api/v1/users`)
| Método | Rota             | Descrição                    |
|--------|------------------|-------------------------------|
| POST   | `/login`         | Login do usuário              |
| POST   | `/signup`        | Criação de novo usuário       |
| GET    | `/`              | Lista todos os usuários       |
| GET    | `/by-id/{user_id}` | Busca usuário por ID        |
| GET    | `/logado`        | Retorna usuário logado        |
| PUT    | `/{user_id}`     | Atualiza dados do usuário     |
| DELETE | `/{user_id}`     | Deleta usuário                |

### 🍇 Produção (`/api/v1/producoes`)
| Método | Rota                        | Descrição                   |
|--------|-----------------------------|------------------------------|
| GET    | `/`                         | Retorna todos os dados       |
| GET    | `/get_prod_ano_min_max`     | Retorna o menor e maior ano  |
| GET    | `/get_producao_by_ano`      | Produção agrupada por ano    |

### 🏭 Processamento (`/api/v1/processamentos`)
| Método | Rota                                | Descrição                   |
|--------|-------------------------------------|------------------------------|
| GET    | `/`                                 | Retorna todos os dados       |
| GET    | `/get_processamento_ano_min_max`    | Retorna o menor e maior ano  |
| GET    | `/get_processamento_by_ano`          | Processamento agrupada por ano|

ℹ️ **Rotas de importação, exportação e comercialização seguem estrutura semelhante.**

### 🔑 Segurança
- Todas as rotas (exceto login e signup) exigem **autenticação via JWT Bearer Token**.
- Use o botão `"Authorize"` na documentação Swagger para testar os endpoints autenticados.

---

### 📦 Importação (`/api/v1/importacoes`)
| Método | Rota                        | Descrição                       |
|--------|-----------------------------|----------------------------------|
| GET    | `/`                         | Lista todos os dados de importação |
| GET    | `/get_importacao_ano_min_max` | Ano mínimo e máximo disponível   |
| GET    | `/get_importacao_by_ano`     | Importação agrupada por ano      |

### 🚢 Exportação (`/api/v1/exportacoes`)
| Método | Rota                        | Descrição                       |
|--------|-----------------------------|----------------------------------|
| GET    | `/`                         | Lista todos os dados de exportação |
| GET    | `/get_exportacao_ano_min_max` | Ano mínimo e máximo disponível   |
| GET    | `/get_exportacao_by_ano`     | Exportação agrupada por ano      |

### 🛒 Comercialização (`/api/v1/comercializacoes`)
| Método | Rota                              | Descrição                          |
|--------|-----------------------------------|-------------------------------------|
| GET    | `/`                               | Lista todos os dados de comercialização |
| GET    | `/get_comercializacao_ano_min_max`| Ano mínimo e máximo disponível       |
| GET    | `/get_comercializacao_by_ano`     | Comercialização agrupada por ano     |

---

## 🧪 Como testar a API

### 📘 Swagger UI
Acesse a [documentação interativa Swagger](https://techchallengeapi.onrender.com/docs) para testar cada rota diretamente no navegador.  
Use o botão **"Authorize"** para inserir o token JWT.
<img width="1137" alt="image" src="https://github.com/user-attachments/assets/3fd466c9-5591-4dc4-8a13-c90c553fb963" />


### 🧰 Exemplo de Login (via `curl`)
```bash
curl -X POST https://techchallengeapi.onrender.com/api/v1/users/login \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=usuario@email.com&password=suasenha"
```

### 📤 Exemplo de resposta com token JWT
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
  "token_type": "bearer"
}
```

### 🔐 Como usar o token
Copie o `access_token` retornado e inclua no cabeçalho das requisições autenticadas:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### 🧪 Testando com Postman
1. Importe o link `/openapi.json` no Postman.
2. Configure o token em **Authorization > Bearer Token**.
3. Teste as rotas protegidas como `GET /producoes`.

---
## 👥 Grupo

Este projeto foi desenvolvido em equipe para este corrente Tech Challenge do Curso Pós Tech - Machine Learning Engineering - FIAP

**Integrantes:**
- Joanna de Cássia Valadares - github: https://github.com/Decassia
- Matheus Pereira de Jesus - github: https://github.com/Matheuszovisk25

---
