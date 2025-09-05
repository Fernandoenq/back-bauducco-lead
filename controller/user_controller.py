from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserUpdate, UserOut
from service import user_service

def create_user(db: Session, payload: UserCreate) -> UserOut:
    user = user_service.create_user(db, payload)
    return UserOut.model_validate(user)

def get_user(db: Session, user_id: int) -> UserOut:
    user = user_service.get_user(db, user_id)
    return UserOut.model_validate(user)

def get_user_by_cpf(db: Session, cpf: str) -> UserOut:
    user = user_service.get_user_by_cpf(db, cpf)
    return UserOut.model_validate(user)

def list_users(db: Session, skip: int, limit: int, q: str | None) -> list[UserOut]:
    users = user_service.list_users(db, skip=skip, limit=limit, q=q)
    return [UserOut.model_validate(u) for u in users]

def update_user(db: Session, user_id: int, payload: UserUpdate) -> UserOut:
    user = user_service.update_user(db, user_id, payload)
    return UserOut.model_validate(user)

def delete_user(db: Session, user_id: int) -> None:
    user_service.delete_user(db, user_id)
