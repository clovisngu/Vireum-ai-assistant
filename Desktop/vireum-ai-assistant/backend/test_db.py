from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import asyncio

DATABASE_URL = "postgresql+asyncpg://admin:password@localhost:5432/vireum_ai"

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True prints SQL statements

async def test_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        # Do NOT await fetchone()
        print(result.fetchone())

# Run the async function
asyncio.run(test_connection())
