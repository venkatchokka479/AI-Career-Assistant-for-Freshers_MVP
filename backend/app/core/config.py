from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai-ats"
    app_env: str = "dev"
    database_url: str
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    vector_backend: str = "faiss"
    similarity_threshold: float = 0.45

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
