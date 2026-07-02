from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import defeitos, indicadores, relatorios, ws

app = FastAPI(
    title="Tecido Qualidade - Inspeção Têxtil",
    version="1.0.0",
    description="API do sistema de inspeção de qualidade de tecidos",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(defeitos.router, prefix="/api/defeitos", tags=["Defeitos"])
app.include_router(indicadores.router, prefix="/api/indicadores", tags=["Indicadores"])
app.include_router(relatorios.router, prefix="/api/relatorios", tags=["Relatórios"])
app.include_router(ws.router, prefix="/ws", tags=["WebSocket"])


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health():
    return {"status": "ok"}
