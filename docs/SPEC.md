# Sistema de Inspeção de Qualidade Têxtil

## SPEC — v1.0

### Visão Geral

Automatizar a inspeção de qualidade dos tecidos durante o rebobinamento.
Uma câmera industrial e um laser monitoram 100% do tecido em tempo real,
identificando automaticamente defeitos, falhas de malha, marcas, vincos e
irregularidades que hoje dependem da inspeção visual humana.

### Indicadores por Filtro

- Tinturaria
- Malharia
- Artigo
- Cor
- Máquina
- Lote
- Data

### Benefícios

- Redução de perdas, retrabalho e devoluções
- Dados concretos vs avaliação visual
- Rastreabilidade por fornecedor, processo e máquina
- Relatórios automáticos
- Histórico completo de defeitos

### Stack Técnica

| Componente | Tecnologia |
|------------|-----------|
| API | FastAPI (Python 3.11) |
| Banco | PostgreSQL 16 |
| Cache/Fila | Redis |
| Dashboard | React + Vite + Tailwind |
| Visão | OpenCV + Modelo CNN |
| Tempo Real | WebSocket |
| Relatórios | WeasyPrint |
| Infra | Docker Compose |
| CI/CD | GitHub Actions |

### Arquitetura

```
[ Câmera Industrial ] ──┐
                         ├──→ [ Serviço de Captura ] ──→ [ Detecção de Defeitos ]
[ Sensor Laser ] ───────┘                                   │
                                                             ▼
                                                    [ Banco PostgreSQL ]
                                                             │
                                                             ▼
                                              ┌── [ API REST ] ──→ [ Dashboard React ]
                                              │
                                              └── [ WebSocket ] ──→ [ Tempo Real ]

[ Serviço de Relatórios ] ←── [ Fila Redis ]
```

### Endpoints da API (planejados)

```
GET    /api/defeitos           - Listar defeitos (com filtros)
GET    /api/defeitos/{id}      - Detalhe do defeito
POST   /api/defeitos           - Registrar defeito (hardware)
GET    /api/indicadores        - Dashboard agregado
GET    /api/indicadores/por-tinturaria
GET    /api/indicadores/por-malharia
GET    /api/indicadores/por-artigo
GET    /api/indicadores/por-cor
GET    /api/indicadores/por-maquina
GET    /api/indicadores/por-lote
GET    /api/indicadores/por-data
GET    /api/relatorios/gerar   - Gerar relatório PDF
WS     /ws/defeitos            - Streaming em tempo real
```
