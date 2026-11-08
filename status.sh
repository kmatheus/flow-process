#!/bin/bash

echo "📊 Status dos containers Docker:"
docker ps

echo ""
echo "💡 Para ver os logs do Backend: tail -f backend.log"
echo "💡 Para ver os logs do Frontend: tail -f frontend.log"