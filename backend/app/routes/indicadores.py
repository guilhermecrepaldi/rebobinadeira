from fastapi import APIRouter, Depends
from sqlalchemy import select, func, case
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Defeito, Lote, StatusInspecao, TipoDefeito

router = APIRouter()


@router.get("/dashboard")
async def dashboard(db: AsyncSession = Depends(get_db)):
    """Indicadores agregados do dashboard principal."""
    total_defeitos = await db.scalar(select(func.count(Defeito.id)))
    total_lotes = await db.scalar(select(func.count(Lote.id)))

    # Defeitos por status
    status_counts = await db.execute(
        select(Defeito.status, func.count(Defeito.id))
        .group_by(Defeito.status)
    )

    # Defeitos por tipo
    tipo_counts = await db.execute(
        select(Defeito.tipo, func.count(Defeito.id))
        .group_by(Defeito.tipo)
    )

    return {
        "total_defeitos": total_defeitos or 0,
        "total_lotes": total_lotes or 0,
        "por_status": dict(status_counts.all()),
        "por_tipo": dict(tipo_counts.all()),
    }


@router.get("/por-tinturaria")
async def por_tinturaria(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.tinturaria, func.count(Defeito.id))
        .join(Defeito, Defeito.lote_id == Lote.id)
        .group_by(Lote.tinturaria)
    )
    return [{"tinturaria": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-malharia")
async def por_malharia(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.malharia, func.count(Defeito.id))
        .join(Defeito)
        .group_by(Lote.malharia)
    )
    return [{"malharia": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-artigo")
async def por_artigo(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.artigo, func.count(Defeito.id))
        .join(Defeito)
        .group_by(Lote.artigo)
    )
    return [{"artigo": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-cor")
async def por_cor(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.cor, func.count(Defeito.id))
        .join(Defeito)
        .group_by(Lote.cor)
    )
    return [{"cor": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-maquina")
async def por_maquina(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.maquina, func.count(Defeito.id))
        .join(Defeito)
        .group_by(Lote.maquina)
    )
    return [{"maquina": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-lote")
async def por_lote(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Lote.codigo, func.count(Defeito.id))
        .join(Defeito)
        .group_by(Lote.id)
        .order_by(func.count(Defeito.id).desc())
        .limit(20)
    )
    return [{"lote": r[0], "defeitos": r[1]} for r in result.all()]


@router.get("/por-data")
async def por_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(func.date(Defeito.created_at), func.count(Defeito.id))
        .group_by(func.date(Defeito.created_at))
        .order_by(func.date(Defeito.created_at).desc())
        .limit(30)
    )
    return [{"data": str(r[0]), "defeitos": r[1]} for r in result.all()]
