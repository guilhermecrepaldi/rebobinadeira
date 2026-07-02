from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Defeito, TipoDefeito, StatusInspecao, Lote

router = APIRouter()


@router.get("/")
async def listar_defeitos(
    tipo: TipoDefeito | None = None,
    status: StatusInspecao | None = None,
    lote_id: int | None = None,
    tinturaria: str | None = None,
    malharia: str | None = None,
    maquina: str | None = None,
    offset: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    query = select(Defeito).join(Defeito.lote)

    if tipo:
        query = query.where(Defeito.tipo == tipo)
    if status:
        query = query.where(Defeito.status == status)
    if lote_id:
        query = query.where(Defeito.lote_id == lote_id)
    if tinturaria:
        query = query.where(Lote.tinturaria == tinturaria)
    if malharia:
        query = query.where(Lote.malharia == malharia)
    if maquina:
        query = query.where(Lote.maquina == maquina)

    query = query.order_by(Defeito.created_at.desc()).offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{defeito_id}")
async def detalhe_defeito(defeito_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Defeito).where(Defeito.id == defeito_id))
    defeito = result.scalar_one_or_none()
    if not defeito:
        raise HTTPException(status_code=404, detail="Defeito não encontrado")
    return defeito


@router.post("/")
async def criar_defeito(
    tipo: TipoDefeito,
    severidade: float = 0.0,
    posicao_x: float = 0,
    posicao_y: float = 0,
    metragem: float = 0,
    lote_id: int = 0,
    db: AsyncSession = Depends(get_db),
):
    defeito = Defeito(
        tipo=tipo, severidade=severidade, posicao_x=posicao_x,
        posicao_y=posicao_y, metragem=metragem, lote_id=lote_id,
    )
    db.add(defeito)
    await db.commit()
    await db.refresh(defeito)
    return defeito
