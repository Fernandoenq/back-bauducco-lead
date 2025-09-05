from pydantic import BaseModel, EmailStr, field_validator, constr
from datetime import datetime
from typing import Optional
from utils.cpf import normalize_and_validate_cpf
from utils.phone import normalize_and_validate_phone

class UserBase(BaseModel):
    nome_completo: constr(min_length=3, max_length=120)
    email: EmailStr
    cpf: str
    celular: str
    aceita_termos: bool

    @field_validator("email", mode="before")
    @classmethod
    def _email_lower(cls, v):
        # retorna string minúscula; Pydantic fará o cast/validação para EmailStr depois
        return str(v).lower()

    @field_validator("cpf")
    @classmethod
    def _cpf_val(cls, v: str) -> str:
        return normalize_and_validate_cpf(v)

    @field_validator("celular")
    @classmethod
    def _phone_val(cls, v: str) -> str:
        return normalize_and_validate_phone(v)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nome_completo: Optional[constr(min_length=3, max_length=120)] = None
    email: Optional[EmailStr] = None

    @field_validator("email", mode="before")
    @classmethod
    def _email_lower(cls, v):
        return None if v is None else str(v).lower()

    cpf: Optional[str] = None
    celular: Optional[str] = None
    aceita_termos: Optional[bool] = None

    @field_validator("cpf")
    @classmethod
    def _cpf_val(cls, v: str) -> str:
        return normalize_and_validate_cpf(v)

    @field_validator("celular")
    @classmethod
    def _phone_val(cls, v: str) -> str:
        return normalize_and_validate_phone(v)

class UserOut(BaseModel):
    id: int
    nome_completo: str
    email: EmailStr
    cpf: str
    celular: str
    aceita_termos: bool
    created_at: datetime

    model_config = {"from_attributes": True}
