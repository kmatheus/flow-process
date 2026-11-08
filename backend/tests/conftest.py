import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.main import app
from app.core.database import Base, get_db
from app.core.redis_config import get_redis
from app.core.security import criar_access_token, gerar_hash_senha
from app.models.usuario import Usuario

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture
async def admin_token(db_session):
    """Fixture para criar um admin e retornar seu token."""
    admin = Usuario(
        email="admin_maq@teste.com",
        senha_hash=gerar_hash_senha("senha123"),
        nome="Admin Maq",
        is_admin=True
    )
    db_session.add(admin)
    await db_session.commit()
    return criar_access_token(subject=str(admin.id))

@pytest_asyncio.fixture(scope="function")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with TestingSessionLocal() as session:
        yield session
        
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


class FakeRedis:
    def __init__(self):
        self.data = {}
    
    async def get(self, key):
        return self.data.get(key)
    
    async def setex(self, key, ttl, value):
        self.data[key] = value
    
    async def set(self, key, value):
        self.data[key] = value
    
    async def delete(self, key):
        self.data.pop(key, None)


@pytest_asyncio.fixture(scope="function")
async def client(db_session):
    """Cria um cliente HTTP fake com banco e Redis mockados."""
    async def override_get_db():
        yield db_session

    fake_redis = FakeRedis()
    async def override_get_redis():
        return fake_redis

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_redis] = override_get_redis
    
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
        
    app.dependency_overrides.clear()