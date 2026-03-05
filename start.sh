#!/bin/bash
echo "🚀 Iniciando containers Docker..."
cd docker && sudo docker compose up -d
echo "📦 Iniciando servidor FastAPI..."
cd ../backend && uv run uvicorn app.main:app --reload