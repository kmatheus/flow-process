from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # App
    APP_NAME: str = Field(default="Flow Process API")
    APP_VERSION: str = Field(default="0.1.0")
    DEBUG: bool = Field(default=True)
    ENVIRONMENT: str = Field(default="development")
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://flow_user:flow_password@localhost:5432/flow_process"
    )
    
    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379/0")
    
    # JWT
    SECRET_KEY: str = Field(default="dev-secret-key-change-in-production")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    
    # CORS
    CORS_ORIGINS: str = Field(default="http://localhost:5173")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "forbid"  # Explicitamente proibir campos extras (padrão, mas deixamos claro)

# Instância única das configurações
settings = Settings()