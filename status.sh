#!/bin/bash
echo "📊 Status dos containers:"
sudo docker ps

echo ""
echo "📊 Portas em uso:"
sudo lsof -i :8000,5432,6379 2>/dev/null || echo "Nenhum serviço do projeto rodando."