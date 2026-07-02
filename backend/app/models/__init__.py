import enum
from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime, Enum, ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class TipoDefeito(str, enum.Enum):
    FALHA_MALHA = "falha_malha"
    MARCA = "marca"
    VINCO = "vinco"
    IRREGULARIDADE = "irregularidade"
    MANCHA = "mancha"
    FURO = "furo"
    OUTRO = "outro"


class StatusInspecao(str, enum.Enum):
    DETECTADO = "detectado"
    CONFIRMADO = "confirmado"
    DESCARTADO = "descartado"
    CORRIGIDO = "corrigido"


class Defeito(Base):
    __tablename__ = "defeitos"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[TipoDefeito] = mapped_column(Enum(TipoDefeito))
    severidade: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[StatusInspecao] = mapped_column(Enum(StatusInspecao), default=StatusInspecao.DETECTADO)
    posicao_x: Mapped[float] = mapped_column(Float)
    posicao_y: Mapped[float] = mapped_column(Float)
    metragem: Mapped[float] = mapped_column(Float, comment="Metragem onde o defeito foi encontrado")
    dimensoes: Mapped[dict] = mapped_column(JSON, default=dict, comment="Largura/altura em mm")
    imagem_ref: Mapped[str | None] = mapped_column(String(500), comment="Caminho da imagem do defeito")

    # Chaves estrangeiras
    lote_id: Mapped[int] = mapped_column(ForeignKey("lotes.id"))
    lote: Mapped["Lote"] = relationship(back_populates="defeitos")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Lote(Base):
    __tablename__ = "lotes"

    id: Mapped[int] = mapped_column(primary_key=True)
    codigo: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    artigo: Mapped[str] = mapped_column(String(100))
    cor: Mapped[str] = mapped_column(String(50))
    tinturaria: Mapped[str] = mapped_column(String(100))
    malharia: Mapped[str] = mapped_column(String(100))
    maquina: Mapped[str] = mapped_column(String(100))
    metragem_total: Mapped[float] = mapped_column(Float, default=0.0)
    metragem_inspecionada: Mapped[float] = mapped_column(Float, default=0.0)
    data_producao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    defeitos: Mapped[list["Defeito"]] = relationship(back_populates="lote", cascade="all, delete-orphan")
