# service/user_service.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.user import User
from repository import user_repository as repo
from schemas.user import UserCreate, UserUpdate

def create_user(db: Session, data: UserCreate) -> User:
    if not data.aceita_termos:
        raise HTTPException(status_code=400, detail="É necessário aceitar os termos.")

    if repo.get_by_email(db, str(data.email)):
        raise HTTPException(status_code=409, detail="E-mail já cadastrado.")

    if repo.get_by_cpf(db, data.cpf):
        raise HTTPException(status_code=409, detail="CPF já cadastrado.")

    user = User(
        nome_completo=data.nome_completo.strip(),
        email=str(data.email),
        cpf=data.cpf,
        celular=data.celular,
        aceita_termos=data.aceita_termos,
    )
    return repo.create(db, user=user)

def get_user(db: Session, user_id: int) -> User:
    user = repo.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user

def get_user_by_cpf(db: Session, cpf: str) -> User:
    user = repo.get_by_cpf(db, cpf)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user

def list_users(db: Session, skip: int = 0, limit: int = 50, q: str | None = None):
    return repo.list_users(db, skip=skip, limit=limit, q=q)

def update_user(db: Session, user_id: int, data: UserUpdate) -> User:
    user = get_user(db, user_id)

    if data.email is not None:
        exists = repo.get_by_email(db, str(data.email))
        if exists and exists.id != user.id:
            raise HTTPException(status_code=409, detail="E-mail já cadastrado em outro usuário.")
        user.email = str(data.email)

    if data.cpf is not None:
        exists = repo.get_by_cpf(db, data.cpf)
        if exists and exists.id != user.id:
            raise HTTPException(status_code=409, detail="CPF já cadastrado em outro usuário.")
        user.cpf = data.cpf

    if data.nome_completo is not None:
        user.nome_completo = data.nome_completo.strip()

    if data.celular is not None:
        user.celular = data.celular

    if data.aceita_termos is not None:
        user.aceita_termos = data.aceita_termos

    return repo.update(db, user)

def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db, user_id)
    repo.delete(db, user)
