import asyncio
from app.core.database import AsyncSessionLocal
from app.models.usuario import Usuario
from app.core.security import gerar_hash_senha

async def criar_admin():
    async with AsyncSessionLocal() as db:
        # Verifica se o admin já existe para evitar duplicatas
        from sqlalchemy import select
        query = select(Usuario).where(Usuario.email == "admin@flowprocess.com")
        result = await db.execute(query)
        if result.scalar_one_or_none():
            print("⚠️  Admin já existe no banco.")
            return

        admin = Usuario(
            email="admin@flowprocess.com",
            senha_hash=gerar_hash_senha("admin123456"),
            nome="Administrador",
            is_admin=True,
            ativo=True
        )
        db.add(admin)
        await db.commit()
        print("✅ Admin criado com sucesso!")
        print("   Email: admin@flowprocess.com")
        print("   Senha: admin123456")

if __name__ == "__main__":
    asyncio.run(criar_admin())