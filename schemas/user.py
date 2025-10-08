from pydantic import BaseModel, EmailStr, constr, field_validator
from datetime import datetime
from typing import Optional
from utils.phone import normalize_and_validate_phone


class UserBase(BaseModel):
    nome_completo: constr(min_length=3, max_length=120)
    email: EmailStr
    celular: str
    aceita_termos: bool = True  # default True

    @field_validator("email", mode="before")
    @classmethod
    def _email_lower(cls, v):
        return str(v).lower()

    @field_validator("celular")
    @classmethod
    def _phone_val(cls, v: str) -> str:
        return normalize_and_validate_phone(v)


class UserCreate(UserBase):
    """Payload para criação de usuário (sem CPF)."""
    pass


class UserUpdate(BaseModel):
    nome_completo: Optional[constr(min_length=3, max_length=120)] = None
    email: Optional[EmailStr] = None
    celular: Optional[str] = None
    aceita_termos: Optional[bool] = None

    @field_validator("email", mode="before")
    @classmethod
    def _email_lower(cls, v):
        return None if v is None else str(v).lower()

    @field_validator("celular")
    @classmethod
    def _phone_val(cls, v: str) -> str:
        return normalize_and_validate_phone(v)


class UserOut(BaseModel):
    id: int
    nome_completo: str
    email: EmailStr
    celular: str
    aceita_termos: bool
    created_at: datetime

    model_config = {"from_attributes": True}
