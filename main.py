from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import Base, engine
from routes.user import router as users_router

app = FastAPI(
    title="Cadastro de Pessoas",
    version="1.0.0",
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera para qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # libera todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # libera todos os headers
)

# cria as tabelas ao subir a aplicação
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users_router, prefix="")
