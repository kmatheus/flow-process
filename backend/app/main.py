from fastapi import FastAPI
from app.api.routes import health, operadores, maquinarios, aviamentos, processos

app = FastAPI(
    title="Flow Process API",
    description="Sistema de Controle para Confecções",
    version="0.1.0"
)

# Incluir rotas
app.include_router(health.router, prefix="/api/v1")
app.include_router(operadores.router, prefix="/api/v1")
app.include_router(maquinarios.router, prefix="/api/v1")
app.include_router(aviamentos.router, prefix="/api/v1")
app.include_router(processos.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Flow Process API",
        "version": "0.1.0",
        "endpoints": {
            "docs": "/docs",
            "health": "/api/v1/health",
            "operadores": "/api/v1/operadores",
            "maquinarios": "/api/v1/maquinarios",
            "aviamentos": "/api/v1/aviamentos",
            "processos": "/api/v1/processos"
        }
    }