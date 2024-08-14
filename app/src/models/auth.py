from sqlalchemy.orm import Mapped, mapped_column

from app.src.models.base import Base


class User(Base):
    __tablename__ = 'users'

    login: Mapped[str]
    password: Mapped[str]
    token: Mapped[str] = mapped_column(unique=True)