from fastapi import FastAPI
from db.session import Base, engine
from routes.user import router as users_router

app = FastAPI(
    title="Cadastro de Pessoas",
    version="1.0.0",
)

# cria as tabelas ao subir a aplicação
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users_router, prefix="")
