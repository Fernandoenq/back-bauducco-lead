from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import Base, engine
from routes.user import router as users_router

app = FastAPI(title="Cadastro de Pessoas", version="1.0.0")

# === CORS ===
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://192.168.0.73:3000",   # front Next na tua máquina (ajuste IP/porta)
    "http://192.168.0.73:3334",        # se usar porta 80
    # "http://<ip-do-tablet>:<porta>",  # se servir o front no próprio tablet (raro)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    # opcional: libera toda a sub-rede 192.168.0.x
    allow_origin_regex=r"^https?://192\.168\.0\.\d{1,3}(:\d+)?$",
    allow_credentials=True,   # OK porque NÃO estamos usando "*" em allow_origins
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# rotas
app.include_router(users_router, prefix="")

# opcional: healthcheck p/ testar no tablet
@app.get("/health")
def health():
    return {"ok": True}
