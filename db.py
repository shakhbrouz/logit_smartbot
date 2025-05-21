import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

async def create_user_table():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT UNIQUE,
        full_name TEXT
    )
    """)
    await conn.close()

async def add_user(telegram_id: int, full_name: str):
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("INSERT INTO users (telegram_id, full_name) VALUES ($1, $2) ON CONFLICT DO NOTHING", telegram_id, full_name)
    await conn.close()