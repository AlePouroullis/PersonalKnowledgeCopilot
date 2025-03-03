import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API settings
    API_V1_STR: str = "/api/v1"

    # CORS settings
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    # Storage paths
    DATA_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data")
    DOCUMENTS_DIR: str = os.path.join(DATA_DIR, "documents")
    VECTOR_DB_DIR: str = os.path.join(DATA_DIR, "vector_db")

    # Make sure directories exist
    @property
    def setup_directories(self):
        os.makedirs(self.DOCUMENTS_DIR, exist_ok=True)
        os.makedirs(self.VECTOR_DB_DIR, exist_ok=True)
        return True

settings = Settings()
settings.setup_directories