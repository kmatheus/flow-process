#!/bin/bash

echo "🔄 Resetando banco de dados de desenvolvimento..."

# 1. Dropa e recria o schema public
docker exec -i flow_postgres psql -U flow_user -d flow_process <<EOF
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO flow_user;
EOF

echo "✅ Schema limpo."

# 2. Roda todas as migrações do zero
uv run alembic upgrade head

echo "🎉 Banco de dados resetado e migrações aplicadas!"