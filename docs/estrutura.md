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
