from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.src.models.base import Base


class Template(Base):
    __tablename__ = 'templates'

    path: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    name: Mapped[str]


class Email(Base):
    __tablename__ = 'emails'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    name: Mapped[str]
    is_sender: Mapped[bool]


class TemplateParam(Base):
    __tablename__ = 'template_params'

    template_id: Mapped[int] = mapped_column(ForeignKey('templates.id', ondelete="CASCADE"))
    name: Mapped[str]


class EmailParams(Base):
    __tablename__ = 'email_params'

    email_id: Mapped[int] = mapped_column(ForeignKey('emails.id', ondelete="CASCADE"))
    name: Mapped[str]
    value: Mapped[str]

