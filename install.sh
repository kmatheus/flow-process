#!/bin/bash
# install.sh - Configuração automática do ambiente

echo "🚀 Instalando UV (gerenciador de pacotes ultra-rápido)..."

# Instala o UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recarrega o PATH
export PATH="$HOME/.cargo/bin:$PATH"

echo "✅ UV instalado! Versão: $(uv --version)"

# Inicializa o projeto
echo "📦 Inicializando projeto..."
uv init flow-process

# Adiciona dependências
echo "🔧 Adicionando dependências principais..."
uv add fastapi sqlalchemy asyncpg psycopg2-binary pydantic python-jose[cryptography] passlib[bcrypt] python-multipart redis celery

echo "🧪 Adicionando dependências de desenvolvimento..."
uv add --dev pytest pytest-asyncio pytest-cov httpx ruff black mypy

echo "✅ Setup completo!"
echo ""
echo "Para ativar o ambiente virtual:"
echo "  source .venv/bin/activate"
echo ""
echo "Para rodar o servidor:"
echo "  uv run uvicorn app.main:app --reload"