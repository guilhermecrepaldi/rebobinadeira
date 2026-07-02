from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Defeito, Lote

router = APIRouter()


@router.get("/gerar")
async def gerar_relatorio(
    tinturaria: str | None = None,
    malharia: str | None = None,
    data_inicio: str | None = None,
    data_fim: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    """Gera relatório CSV consolidado."""
    query = select(Defeito, Lote).join(Defeito.lote)

    if tinturaria:
        query = query.where(Lote.tinturaria == tinturaria)
    if malharia:
        query = query.where(Lote.malharia == malharia)
    if data_inicio:
        query = query.where(Defeito.created_at >= datetime.fromisoformat(data_inicio))
    if data_fim:
        query = query.where(Defeito.created_at <= datetime.fromisoformat(data_fim))

    result = await db.execute(query)
    rows = result.all()

    # Gera CSV
    import csv, io, os
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Tipo", "Severidade", "Status", "Metragem", "Lote", "Artigo", "Cor", "Tinturaria", "Malharia", "Data"])
    for defeito, lote in rows:
        writer.writerow([defeito.id, defeito.tipo.value, defeito.severidade, defeito.status.value,
                        defeito.metragem, lote.codigo, lote.artigo, lote.cor, lote.tinturaria, lote.malharia,
                        defeito.created_at.isoformat()])

    path = f"/data/relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    os.makedirs("/data", exist_ok=True)
    with open(path, "w") as f:
        f.write(output.getvalue())

    return {"relatorio": path, "linhas": len(rows)}
