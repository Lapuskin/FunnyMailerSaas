import os

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL, echo=os.environ.get('DB_ECHO'))
Session = sessionmaker(bind=engine, class_=AsyncSession)

metadata = MetaData()
metadata.bind = engine


async def get_db():
    '''Метод для доступа к базе данных'''
    db = AsyncSession()
    try:
        yield db
    finally:
        await db.close()