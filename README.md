# Flow Process - Sistema de Controle para Confecções 👖

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Sobre o Projeto

O Flow Process nasceu de um Trabalho de Conclusão de Curso (TCC) em Sistemas de Informação e está sendo reconstruído como um produto real. É um sistema de gestão operacional focado em microempresas de confecção de roupas jeans, permitindo controle de:

- 👥 **Operadores** (funcionários e suas funções)
- ⚙️ **Maquinários** (controle de ativos, manutenções)
- 🧵 **Aviamentos/Recursos** (estoque de insumos)
- 📋 **Processos** (fluxo de produção)

### 📌 Problema que Resolve
Microempresas têxteis frequentemente perdem produtividade e dinheiro devido à gestão manual (planilhas, papéis) e falta de integração entre setores. O Flow Process oferece uma solução simples, acessível e eficaz.

---

# 🌳 Estrutura do Projeto - Flow Process

*Gerado em: 09/11/2026 15:02:44*

```bash
Flow Process/
├── 📁 backend       # Configurações principais do Backend
│   ├── 📁 alembic
│   │   ├── 📁 versions
│   │   │   └── 🐍 a77a370727e9_criar_tabelas_iniciais.py
│   │   ├── 📄 README
│   │   ├── 🐍 env.py
│   │   └── 📄 script.py.mako
│   ├── 📁 app
│   │   ├── 📁 api       # Endpoints da API REST
│   │   │   ├── 📁 routes           # API de Routes
│   │   │   │   ├── 🐍 auth.py
│   │   │   │   ├── 🐍 aviamentos.py
│   │   │   │   ├── 🐍 health.py
│   │   │   │   ├── 🐍 maquinarios.py
│   │   │   │   ├── 🐍 operadores.py
│   │   │   │   └── 🐍 processos.py
│   │   │   └── 🐍 dependencies.py
│   │   ├── 📁 core      # Núcleo da aplicação - Funcionalidades compartilhadas
│   │   │   ├── 🐍 config.py
│   │   │   ├── 🐍 database.py
│   │   │   ├── 🐍 redis_config.py
│   │   │   └── 🐍 security.py
│   │   ├── 📁 models    # Modelos de dados
│   │   │   ├── 🐍 aviamento.py
│   │   │   ├── 🐍 maquinario.py
│   │   │   ├── 🐍 operador.py
│   │   │   ├── 🐍 processo.py
│   │   │   └── 🐍 usuario.py
│   │   ├── 📁 schemas
│   │   │   ├── 🐍 aviamento.py
│   │   │   ├── 🐍 maquinario.py
│   │   │   ├── 🐍 operador.py
│   │   │   ├── 🐍 processo.py
│   │   │   ├── 🐍 token.py
│   │   │   └── 🐍 usuario.py
│   │   ├── 📁 services  # Lógica de negócio e serviços
│   │   │       └── ...
│   │   ├── 📁 utils     # Funções utilitárias
│   │   │       └── ...
│   │   └── 🐍 main.py
│   ├── 📁 tests           # Testes unitários e de integração
│   │   ├── 📁 integration
│   │   │   ├── 🐍 test_integracao_auth.py         # Testes unitários
│   │   │   ├── 🐍 test_integracao_aviamentos.py   # Testes unitários
│   │   │   ├── 🐍 test_integracao_maquinarios.py  # Testes unitários
│   │   │   ├── 🐍 test_integracao_operadores.py   # Testes unitários
│   │   │   └── 🐍 test_integracao_processos.py    # Testes unitários
│   │   ├── 📁 unit
│   │   │   └── 🐍 test_security.py  # Testes unitários
│   │   ├── 🐍 conftest.py   # Testes unitários
│   │   └── 🐍 factories.py
│   ├── 📄 Dockerfile      # Imagem Docker para desenvolvimento
│   ├── 📄 alembic.ini
│   ├── 🐍 main.py
│   ├── 📦 pyproject.toml  # Configuração do projeto e dependências
│   ├── 📄 pytest.ini      # Configuração do Pytest
│   ├── </> reset_db.sh
│   ├── 🐍 seed_admin.py   # Configuração do Admin
│   └── 🔒uv.lock
├── 📁 docker        # Configurações Docker
│   └── ⚙️ docker-compose.yml  # Orquestração de containers Docker
├── 📁 frontend      # Configurações principais do Frontend
│   ├── 📁 public
│   │   ├── 📄 favicon.svg
│   │   └── 📄 icons.svg
│   ├── 📁 src
│   │   ├── 📁 assets
│   │   │   ├── 📄 hero.png
│   │   │   ├── 📄 react.svg
│   │   │   └── 📄 vite.svg
│   │   ├── 📁 components
│   │   │       └── ...
│   │   ├── 📁 contexts
│   │   │   └── ⚛️ AuthContext.tsx
│   │   ├── 📁 pages
│   │   │   ├── ⚛️ Dashboard.tsx
│   │   │   └── ⚛️ Login.tsx
│   │   ├── 📁 services    # Lógica de negócio e serviços
│   │   │   └── 📘 api.ts
│   │   ├── 🎨 App.css
│   │   ├── ⚛️ App.tsx
│   │   ├── 🎨 index.css
│   │   └── ⚛️ main.tsx
│   ├── 📄 Dockerfile          # Imagem Docker para desenvolvimento
│   ├── 📝 README.md           # Documentação principal do projeto
│   ├── 🌐 index.html
│   ├── 📊 package-lock.json   # Lock de dependências Node
│   ├── 📊 package.json        # Dependências Node.js
│   ├── 📊 tsconfig.app.json
│   ├── 📊 tsconfig.json       # Configuração TypeScript
│   ├── 📊 tsconfig.node.json
│   └── 📘 vite.config.ts
├── 📁 scripts       # Scripts auxiliares
│       └── ...
├── 📝 README.md     # Documentação principal do projeto
├── 📄 backend.log
├── 📄 frontend.log
├── </> logs.sh
├── 🐍 main.py
├── </> start.sh    # Script de inicialização
├── </> status.sh
└── </> stop.sh
```

## 📖 Legenda

| Emoji | Significado |
|-------|-------------|
| 📁 | Pasta/Diretório |
| 🐍 | Arquivo Python |
| 📝 | Documentação (MD) |
| ⚙️ | Configuração (YAML) |
| </> | Script Shell |
| 📊 | Dados (JSON) |
| 📄 | Arquivo texto |
| 🌿 | Variáveis de ambiente |
| ♦️ | Git |
| 🐳 | Docker |
| 📦 | Pacote Python |
| 🔒 | Arquivo de lock |

> **Nota:** Pastas marcadas com `...` estão vazias ou contêm apenas arquivos ignorados.

---

## 🛠️ Stack Tecnológico (Por quê?)

| Camada | Tecnologia | Justificativa |
|--------|------------|---------------|
| **Backend** | FastAPI + SQLAlchemy | Performance, tipagem forte, documentação automática (OpenAPI) |
| **Banco de Dados** | PostgreSQL | Robustez, confiabilidade, recursos avançados |
| **Cache/Filas** | Redis | Tarefas assíncronas, cache de consultas |
| **Task Queue** | Celery | Processamento em background (relatórios, notificações) |
| **Autenticação** | JWT + OAuth2 | Padrão de mercado, stateless |
| **Migrations** | Alembic | Controle de versão do banco |
| **Testes** | Pytest + Factory Boy | Qualidade e confiabilidade |
| **Frontend** | React + Vite | Performance, ecossistema maduro |
| **Estilização** | Tailwind CSS | Desenvolvimento rápido, responsivo |
| **Container** | Docker | Ambiente consistente |

---

## 🚀 Tecnologias Aprendidas Neste Projeto

- **UV** - Gerenciamento de dependências moderno (2026)
- **FastAPI** - APIs assíncronas com type hints
- **SQLAlchemy 2.0** - ORM poderoso e flexível
- **Pydantic V3** - Validação com performance em Rust
- **Ruff** - Linting e formatação unificados
- **Pytest + Hypothesis** - Testes com propriedades
- **Celery + Redis** - Tarefas assíncronas e cache
- **Redis** - Cache e blacklist de tokens JWT
- **Docker** - Containerização
- **GitHub Actions** - CI/CD automatizado

---

## 📦 MVP - Escopo Inicial (Entrega 1)

**Foco:** Fazer o básico com excelência.

### ✅ Funcionalidades Prioritárias

#### 1. Autenticação e Usuários 🔐
- [x] Cadastro de usuário (apenas admin)
- [x] Login com JWT
- [x] Refresh token
- [x] Logout (invalidação de token)
- [x] Proteção de rotas (dependendo do perfil)

#### 2. Gestão de Operadores 👥 (RF001)
- [x] Criar operador (com validação de CPF único)
- [x] Listar operadores (com filtros)
- [x] Detalhar operador
- [x] Atualizar operador
- [x] Remover operador (soft delete)
- [x] Regra: não remover se estiver em processo ativo

#### 3. Gestão de Maquinários ⚙️ (RF002)
- [x] Criar maquinário (Nº único)
- [x] Listar maquinários (filtros por status)
- [x] Detalhar maquinário
- [x] Atualizar maquinário
- [x] "Baixar" maquinário (soft delete)
- [x] Histórico básico de alterações

#### 4. Gestão de Aviamentos/Recursos 🧵 (RF003)
- [x] Criar recurso (controle de quantidade)
- [x] Listar recursos
- [x] Atualizar quantidade (entrada/saída)
- [x] Histórico de movimentações

#### 5. Gestão de Processos 📋 (RF004) - Simplificado
- [x] Criar processo (vinculando operadores, maquinários, recursos)
- [x] Listar processos (filtros por status)
- [x] Atualizar status (executar, pausar, encerrar)
- [x] Regra: não remover processo em execução

#### 6. Testes Automatizados 🧪
- [x] Testes unitários (segurança, JWT)
- [x] Testes de integração (rotas, regras de negócio)
- [x] Cobertura de cenários de erro (CPF duplicado, saldo insuficiente)
- [x] Mock de Redis para testes isolados

---

## 🚀 Como Começar (Guia para Devs)

### Pré-requisitos
- Docker e Docker Compose
- Python 3.11+
- UV (gerenciador de pacotes)

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/kmatheus/flow-process.git
cd flow-process

# 2. Configure as permissões dos scripts (primeira vez apenas)
chmod +x start.sh stop.sh status.sh logs.sh

# 3. Inicie o projeto (Docker Compose sobe tudo: DB, Backend e Frontend)
./start.sh

# O servidor estará disponível em:
# API: http://localhost:8000/docs
# Documentação interativa: http://localhost:8000/redoc
# Frontend: http://localhost:5173

# 4. Para parar o projeto (quando terminar)
./stop.sh

# 5. Para ver o status dos containers
./status.sh
```

### 🛠️ Scripts Utilitários

O projeto possui scripts para facilitar o dia a dia:

| Script | Descrição |
|--------|-----------|
| `start.sh` | Inicia todos os serviços (Docker Compose) |
| `stop.sh` | Para todos os serviços |
| `status.sh` | Mostra o status dos containers e dicas |
| `logs.sh` | Mostra logs de todos os serviços (ou de um específico) |

**Exemplos de uso:**

```bash
./logs.sh            # Logs de todos os serviços
./logs.sh backend    # Logs apenas do backend
./logs.sh frontend   # Logs apenas do frontend
```

### 📁 Árvore do Projeto (tree-docs)

Para gerar ou atualizar a árvore de diretórios do projeto automaticamente, utilize a ferramenta [`tree-docs`](https://tree-docs.readthedocs.io/), que está configurada como dependência de desenvolvimento no backend.

**Comando (a partir da pasta `backend/`):**

```bash
cd backend
uv run tree-docs -d .. -o ../docs/estrutura.md -n "Flow Process"
```
Isso gera o arquivo `docs/estrutura.md` na raiz do projeto, contendo a árvore completa de pastas e arquivos. O arquivo pode ser commitado para manter a documentação visual sempre atualizada.

---

### ⚠️ Nota sobre permissões do Docker

Se encontrar erros de permissão (`permission denied`), execute:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### 👤 Criando o primeiro usuário admin

Após iniciar o projeto pela primeira vez (`./start.sh`), o banco de dados estará vazio. Para criar o usuário administrador inicial, execute:

```bash
docker exec -it flow_backend /app/.venv/bin/python seed_admin.py
```

Credenciais padrão:
- Email: `admin@flowprocess.com`
- Senha: `admin123456`
> ⚠️ Importante: Em produção, altere a senha do admin imediatamente após o primeiro login.

---

## 🔧 Configuração de Ambiente

### Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configuração, seguindo as melhores práticas de segurança:

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `DATABASE_URL` | Conexão com PostgreSQL | `postgresql+asyncpg://usuario:senha@localhost:5432/db` |
| `REDIS_URL` | Conexão com Redis | `redis://localhost:6379/0` |
| `SECRET_KEY` | Chave secreta para JWT | `minha-chave-super-secreta` |
| `ALGORITHM` | Algoritmo JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token | `30` |
| `APP_NAME` | Nome da aplicação | `Flow Process API` |
| `APP_VERSION` | Versão | `0.1.0` |
| `DEBUG` | Modo debug | `True` ou `False` |
| `ENVIRONMENT` | Ambiente | `development`, `staging`, `production` |
| `CORS_ORIGINS` | URLs permitidas (separadas por vírgula) | `http://localhost:5173,http://localhost:3000` |

### Arquivos de Configuração
```bash
backend/
├── .env                 # SEUS DADOS REAIS (NÃO versionar)
├── .env.example         # Template para outros devs (VERSIONAR)
└── app/core/config.py   # Carrega as configurações (VERSIONAR)
```

### ⚠️ Importante

- **NUNCA** commite o arquivo `.env` com senhas reais
- **SEMPRE** use `.env.example` como template
- Ao clonar o projeto, copie `.env.example` para `.env`:
  ```bash
  cp backend/.env.example backend/.env
  ```
- Edite o .env com suas configurações locais

### 🔐 Gerando uma SECRET_KEY segura
Para produção, gere uma chave aleatória forte:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 🌍 Ambientes Diferentes
| Ambiente | DEBUG | ENVIRONMENT | Uso |
|----------|-----------|---------|-----|
| Desenvolvimento | `True` | `development` | Local |
| Testes | `True` | `testing` | CI/CD |
| Produção | `False` | `production` | Servidor real |

---

## 🔐 Autenticação

O sistema utiliza **JWT (JSON Web Tokens)** para autenticação, com dois tipos de tokens:

| Token | Duração | Uso |
|-------|---------|-----|
| `access_token` | 30 minutos | Acesso às rotas protegidas |
| `refresh_token` | 7 dias | Renovar o access token |

### Fluxo de Autenticação

1. **Login** → Recebe `access_token` e `refresh_token`
2. **Requisições** → Envia `access_token` no header `Authorization: Bearer <token>`
3. **Expiração** → Use `refresh_token` para obter novos tokens

### Endpoints de Autenticação

| Método | Endpoint | Descrição | Protegido? |
|--------|----------|-----------|------------|
| `POST` | `/api/v1/auth/login` | Login com email e senha | ❌ Não |
| `POST` | `/api/v1/auth/register` | Cadastrar novo usuário | ✅ Admin |
| `POST` | `/api/v1/auth/refresh` | Renovar o access_token | ❌ Não (requer refresh_token) |
| `POST` | `/api/v1/auth/logout` | Encerrar sessão (blacklist) | ✅ Usuário logado |

### 🛡️ Proteção de Rotas

A partir desta versão, **TODAS** as rotas de negócio (Operadores, Maquinários, Aviamentos e Processos) estão protegidas. É obrigatório enviar o `access_token` no header `Authorization: Bearer <token>` para acessá-las.

### 🚪 Logout e Revogação de Token

O logout invalida o token imediatamente. Internamente, o sistema adiciona o identificador único do token (`jti`) em uma **blacklist no Redis**. O Redis é configurado para apagar essa entrada automaticamente quando o token expiraria naturalmente, evitando acúmulo de lixo no banco.

### 💡 Dica: Testando o Refresh Token via curl

Como o endpoint de refresh espera o token no corpo da requisição (e não no header), use o seguinte comando:

```bash
curl -X POST "http://localhost:8000/api/v1/auth/refresh" \
  -H "Content-Type: application/json" \
  -d '"SEU_REFRESH_TOKEN_AQUI"'
```

---

### Como testar no Swagger

1. No Swagger, vá até **`POST /api/v1/auth/login`** e clique em "Try it out"
2. Preencha `username` e `password` com as credenciais do admin:
   - **username:** `admin@flowprocess.com`
   - **password:** `admin123456`
3. Clique em "Execute". O Swagger guardará o token automaticamente.
4. Clique no cadeado **"Authorize"** 🔓. Como o token já foi capturado, você verá **"Authorized"** em verde.
5. Agora você pode testar as rotas protegidas!

### Exemplo de Login (curl)

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@flowprocess.com&password=admin123456"
```

### Exemplo de Requisição Autenticada (curl)

```bash
# Use o access_token retornado no login
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "novo@flowprocess.com",
    "nome": "Novo Usuário",
    "senha": "senha123456",
    "is_admin": false
  }'
```

---

## 🧪 Testes Automatizados

O projeto possui uma suíte completa de testes automatizados para garantir a qualidade e a consistência do código, sendo a base para um ambiente de produção robusto.

### Ferramentas
- **Pytest**: Framework de testes
- **Pytest-AsyncIO**: Suporte a testes assíncronos
- **Factory Boy**: Geração de dados fakes
- **SQLite em memória**: Banco isolado para testes rápidos

### Estrutura de Testes
```bash
tests/
├── conftest.py              # Configurações, fixtures globais e mock do Redis
├── factories.py             # Fábricas de dados fake
├── unit/                    # Testes isolados (não dependem de banco/rede)
│   └── test_security.py     # Hash de senha, JWT
└── integration/             # Testes de fluxo completo (banco de dados, API)
    ├── test_integracao_auth.py
    ├── test_integracao_aviamentos.py
    ├── test_integracao_maquinarios.py
    ├── test_integracao_operadores.py
    └── test_integracao_processos.py
```

---

### Como rodar os testes
```bash
cd backend
uv run pytest -v
```

### Cobertura de testes
Para gerar um relatório de cobertura (percentual do código testado):

```bash
uv run pytest --cov=app tests/ --cov-report=html
# Abra o arquivo htmlcov/index.html no navegador para visualizar
```

### ⚠️ Importante
- Os testes usam **SQLite em memória**, portanto **não afetam** seu banco PostgreSQL de desenvolvimento.
- Cada teste é isolado: as tabelas são criadas e destruídas automaticamente.
- Os testes de integração provam que a **autenticação JWT** está funcionando de ponta a ponta.

---

## 🗄️ Migrações de Banco de Dados (Alembic)

O projeto utiliza **Alembic** para versionar o esquema do banco de dados. Isso significa que qualquer alteração na estrutura das tabelas é registrada em um script de migração, que pode ser aplicado ou revertido de forma segura.

### Comandos Essenciais

| Comando | Descrição |
|---------|-----------|
| `alembic revision --autogenerate -m "descrição"` | Gerar um novo script de migração comparando os modelos com o banco |
| `alembic upgrade head` | Aplicar todas as migrações pendentes |
| `alembic downgrade -1` | Reverter a última migração aplicada |
| `alembic history` | Ver o histórico de migrações |
| `alembic current` | Ver qual migração está aplicada no momento |

### Fluxo de Trabalho

1.  **Alterou um modelo?** (ex: adicionou uma coluna)
2.  Gere a migração: `uv run alembic revision --autogenerate -m "adiciona coluna X"`
3.  Revise o arquivo gerado em `alembic/versions/`
4.  Aplique: `uv run alembic upgrade head`
5.  **Commite o arquivo de migração junto com o código!**

### 🔄 Resetando o Banco de Dados (Apenas Desenvolvimento)

Se precisar limpar o banco e recriar as tabelas do zero, use o script:

```bash
cd backend
./reset_db.sh
```
❗️ Cuidado: Isso apaga todos os dados do banco de desenvolvimento!

### ⚠️ Importante
- Nunca use `Base.metadata.create_all()` manualmente em produção. O Alembic é a única fonte de verdade para a estrutura do banco.
- Os scripts de migração são versionados no Git e devem ser commitados junto com as alterações nos modelos.
- O Alembic mantém a tabela `alembic_version` para saber qual migração está aplicada.

---

## 🔒 Princípios de Design (Nossos Compromissos)

### 1. **Idempotência**
Todas as operações de escrita (POST, PUT, PATCH, DELETE) serão idempotentes sempre que fizer sentido.

### 2. **Consistência de Dados**
- Transações de banco para operações críticas
- Validações em nível de banco (unique constraints, foreign keys)
- Soft delete para auditoria

### 3. **Resiliência**
- Retry com backoff para operações externas
- Circuit breaker para serviços dependentes (futuro)
- Graceful degradation

### 4. **Observabilidade**
- Logs estruturados (JSON)
- Métricas de negócio e sistema
- Tracing distribuído (futuro)

### 5. **Testabilidade**
- Cobertura de testes > 80% no backend
- Testes unitários para lógica de negócio
- Testes de integração para APIs
- Testes E2E para fluxos críticos

---

## 🗺️ Roadmap do Projeto
```bash
FASE 0 - Fundação ✅ CONCLUÍDA
├── Setup do projeto (git, estrutura) ✅
├── Configuração do ambiente Docker ✅
├── Modelagem inicial do banco ✅
└── CI/CD básico (lint, testes) ⏳ (a fazer)

FASE 1 - Core ✅ CONCLUÍDA
├── Autenticação (JWT) ✅
├── CRUD Operadores ✅
├── CRUD Maquinários ✅
└── Testes unitários do core ✅

FASE 2 - Negócio ✅ CONCLUÍDA
├── CRUD Aviamentos ✅
├── CRUD Processos ✅
├── Regras de negócio (validações) ✅
└── Testes de integração ✅

FASE 3 - Frontend ⏳ (a fazer)
├── Setup React + Tailwind ✅
├── Tela de login ✅
├── Telas de listagem (com filtros)
├── Telas de cadastro/edição
└── Integração com API

FASE 4 - Avançado ⏳ (a fazer)
├── Cache com Redis
├── Tarefas assíncronas (Celery)
├── Relatórios em background
├── Dashboard com métricas
└── Testes E2E
```

---

## 📊 Modelagem de Dados (Versão Inicial)
```sql
usuarios (
    id UUID PK,
    email VARCHAR UNIQUE,
    senha_hash VARCHAR,
    nome VARCHAR,
    is_admin BOOLEAN DEFAULT FALSE,
    ativo BOOLEAN,
    created_at TIMESTAMP
)

operadores (
    id UUID PK,
    nome_completo VARCHAR,
    cpf VARCHAR(11) UNIQUE,
    data_nascimento DATE,
    telefone1 VARCHAR,
    funcoes JSONB, -- Simplificado inicialmente
    ativo BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
)

maquinarios (
    id UUID PK,
    numero VARCHAR UNIQUE,
    nome VARCHAR,
    modelo VARCHAR,
    status VARCHAR,
    ativo BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
)
```

---

## 🤝 Como Contribuir (Evolução do Projeto)
Este projeto é construído em público com objetivos educacionais e profissionais. Se quiser contribuir ou sugerir melhorias, fique à vontade!

---

## 📝 Licença
MIT License - use, estude, modifique e até comercialize, mas lembre-se de dar os créditos.

---

## 👨‍💻 Autor
Kelvin Matheus Vieira Dias
[LinkedIn](https://www.linkedin.com/in/kelvin-matheusdev/) | [GitHub](https://github.com/kmatheus)

---

## ⭐ Se este projeto te ajudou, considere dar uma estrela!