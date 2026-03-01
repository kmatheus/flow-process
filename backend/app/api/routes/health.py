from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Verifica se a API está funcionando
    """
    return {
        "status": "healthy",
        "version": "0.1.0",
        "service": "flow-process"
    }