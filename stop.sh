#!/bin/bash
echo "🛑 Parando containers Docker..."
cd docker && sudo docker compose down
echo "✅ Containers parados. Memória liberada!"