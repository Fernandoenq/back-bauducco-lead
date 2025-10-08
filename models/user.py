from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer, DateTime, func
from db.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome_completo: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    
    # CPF agora é opcional (nullable=True). Se não quiser mais usar, pode remover.
    cpf: Mapped[str] = mapped_column(String(11), nullable=True, unique=False, index=True)

    celular: Mapped[str] = mapped_column(String(20), nullable=False)
    aceita_termos: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
