from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class NotePad(Base):
    __tablename__ = "NotePad"
    id:Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    note:Mapped[str] = mapped_column(unique=False)
    created_at:Mapped[str] = mapped_column(default=lambda:datetime.now(), onupdate=lambda:datetime.now())