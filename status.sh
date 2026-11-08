#!/bin/bash

echo "📊 Status dos containers Docker:"
docker ps

echo ""
echo "💡 Comandos úteis:"
echo "   ./start.sh  - Inicia todos os serviços"
echo "   ./stop.sh   - Para todos os serviços"
echo "   ./logs.sh   - Mostra logs de todos os serviços"
echo "   ./logs.sh backend - Mostra logs apenas do backend"