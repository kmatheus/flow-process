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

## 🏗️ Arquitetura do Sistema
```bash
flow-process/
├── backend/ # API FastAPI
│ ├── app/
│ │ ├── api/ # Rotas e endpoints
│ │ ├── core/ # Configurações, segurança
│ │ ├── models/ # Modelos SQLAlchemy
│ │ ├── schemas/ # Schemas Pydantic
│ │ ├── services/ # Lógica de negócio
│ │ └── utils/ # Utilitários
│ ├── tests/ # Testes (pytest)
│ └── alembic/ # Migrations
├── frontend/ # React + Vite
│ ├── src/
│ │ ├── components/ # Componentes reutilizáveis
│ │ ├── pages/ # Páginas da aplicação
│ │ ├── services/ # Chamadas à API
│ │ └── utils/ # Utilitários
│ └── public/
├── docker/ # Configurações Docker
├── docs/ # Documentação adicional
└── scripts/ # Scripts utilitários
```

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
- **Docker** - Containerização
- **GitHub Actions** - CI/CD automatizado

---

## 📦 MVP - Escopo Inicial (Entrega 1)

**Foco:** Fazer o básico com excelência.

### ✅ Funcionalidades Prioritárias

#### 1. Autenticação e Usuários 🔐
- [ ] Cadastro de usuário (apenas admin)
- [ ] Login com JWT
- [ ] Refresh token
- [ ] Logout (invalidação de token)
- [ ] Proteção de rotas (dependendo do perfil)

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
FASE 0 - Fundação (2 semanas)
├── Setup do projeto (git, estrutura)
├── Configuração do ambiente Docker
├── Modelagem inicial do banco
└── CI/CD básico (lint, testes)

FASE 1 - Core (3 semanas)
├── Autenticação (JWT)
├── CRUD Operadores
├── CRUD Maquinários
└── Testes unitários do core

FASE 2 - Negócio (3 semanas)
├── CRUD Aviamentos
├── CRUD Processos
├── Regras de negócio (validações)
└── Testes de integração

FASE 3 - Frontend (4 semanas)
├── Setup React + Tailwind
├── Tela de login
├── Telas de listagem (com filtros)
├── Telas de cadastro/edição
└── Integração com API

FASE 4 - Avançado (3 semanas)
├── Cache com Redis
├── Tarefas assíncronas (Celery)
├── Relatórios em background
├── Dashboard com métricas
└── Testes E2E
```

---

## 🚀 Como Começar (Guia para Devs)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/flow-process.git
cd flow-process

# Suba os containers
docker-compose up -d

# Backend
cd backend
cp .env.example .env
poetry install
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload

# Frontend (em outro terminal)
cd frontend
cp .env.example .env
npm install
npm run dev

# Acesse
# API: http://localhost:8000/docs
# Frontend: http://localhost:5173
```

---

## 📊 Modelagem de Dados (Versão Inicial)
```sql
-- Versão simplificada para começar
-- Detalharemos isso na Etapa 2

usuarios (
    id UUID PK,
    email VARCHAR UNIQUE,
    senha_hash VARCHAR,
    nome VARCHAR,
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

-- ... demais tabelas
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