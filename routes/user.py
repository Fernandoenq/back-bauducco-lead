from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from deps import get_db
from schemas.user import UserCreate, UserOut, UserUpdate
from controller import user_controller

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, payload)

@router.get("", response_model=list[UserOut])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    q: str | None = Query(None, description="Filtro por nome (ilike)"),
    db: Session = Depends(get_db),
):
    return user_controller.list_users(db, skip=skip, limit=limit, q=q)

@router.get("/{cpf}", response_model=UserOut)   # <-- NOVO
def get_user_by_cpf(cpf: str, db: Session = Depends(get_db)):
    return user_controller.get_user_by_cpf(db, cpf)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    return user_controller.update_user(db, user_id, payload)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_controller.delete_user(db, user_id)
    return None
