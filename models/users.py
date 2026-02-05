from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql.functions import now

from models.base import Base


class User(Base):
    first_name: Mapped[str] = mapped_column(String(255), )
    phone: Mapped[str] = mapped_column(String(12), unique=True)
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now())
    adverts: Mapped[list['Advert']] = relationship('Advert', back_populates='owner')
