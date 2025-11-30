import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Vireum AI Assistant"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://admin:password@localhost:5432/vireum_ai")
    
settings = Settings()
