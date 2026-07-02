# Sistema de Inspeção de Qualidade Têxtil

Automação da inspeção de qualidade de tecidos durante o rebobinamento usando câmera industrial + laser + inteligência artificial.

## Stack

- **Backend:** Python + FastAPI + SQLAlchemy + PostgreSQL
- **Frontend:** React + Vite + Tailwind CSS + Recharts
- **Visão Computacional:** OpenCV + modelos de detecção de defeitos
- **Tempo Real:** WebSocket + MQTT
- **Infra:** Docker + Docker Compose + GitHub Actions
- **Relatórios:** WeasyPrint / ReportLab

## Funcionalidades

- [x] Monitoramento em tempo real de defeitos têxteis
- [x] Dashboard com indicadores por tinturaria, malharia, artigo, cor, máquina, lote, data
- [x] Detecção automática de: defeitos, falhas de malha, marcas, vincos, irregularidades
- [x] Relatórios automáticos de qualidade
- [x] Histórico completo de defeitos
- [ ] Integração com sensores laser
- [ ] Alertas em tempo real

## Estrutura

```
tecido-qualidade/
├── backend/          # API FastAPI
│   ├── app/
│   │   ├── models/   # SQLAlchemy models
│   │   ├── routes/   # API endpoints
│   │   └── services/ # Business logic
│   └── Dockerfile
├── frontend/         # React dashboard
├── hardware/         # Camera + laser interfaces
├── data/             # Datasets e CSVs
├── docs/             # Documentação
└── docker-compose.yml
```

## Começando

```bash
docker compose up -d
# Acessar: http://localhost:8000
# Dashboard: http://localhost:5173
```
