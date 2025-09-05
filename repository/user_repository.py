from typing import Optional, Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User


def get_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.get(User, user_id)


def get_by_email(db: Session, email: str) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    return db.execute(stmt).scalars().first()


def get_by_cpf(db: Session, cpf: str) -> Optional[User]:
    stmt = select(User).where(User.cpf == cpf)
    return db.execute(stmt).scalars().first()


def list_users(db: Session, skip: int = 0, limit: int = 50, q: Optional[str] = None) -> Sequence[User]:
    stmt = select(User)
    if q:
        like = f"%{q}%"
        stmt = stmt.where(User.nome_completo.ilike(like))
    stmt = stmt.offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()


def create(db: Session, *, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
