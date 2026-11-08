#!/bin/bash

if [ -z "$1" ]; then
    echo "📋 Mostrando logs de TODOS os serviços (Ctrl+C para sair)..."
    cd docker && docker compose logs -f
else
    echo "📋 Mostrando logs do serviço: $1 (Ctrl+C para sair)..."
    cd docker && docker compose logs -f "$1"
fi