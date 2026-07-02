# Sprint 1 — Inspeção de Qualidade Têxtil

**Prazo:** 2 meses (Julho–Agosto 2026)
**Repo:** github.com/guilhermecrepaldi/tecido-qualidade

---

## Sprint 1.1 — Fundação (Dias 1–10)

| Tarefa | Status | Prioridade |
|--------|--------|:----------:|
| Setup ambiente (Docker, DB, Redis) | ✅ Feito | 🔴 |
| API FastAPI + modelos (Defeito, Lote) | ✅ Feito | 🔴 |
| Rotas CRUD defeitos | ✅ Feito | 🔴 |
| Rotas indicadores (7 filtros) | ✅ Feito | 🔴 |
| Dashboard React + gráficos | ✅ Feito | 🔴 |
| WebSocket tempo real | ✅ Feito | 🟡 |
| Detector OpenCV (7 tipos defeito) | ✅ Feito | 🔴 |
| Relatórios CSV | ✅ Feito | 🟡 |

## Sprint 1.2 — Núcleo (Dias 11–25)

| Tarefa | Status | Prioridade |
|--------|--------|:----------:|
| Integração câmera industrial real | ⬜ Pendente | 🔴 |
| Calibração laser/metragem | ⬜ Pendente | 🔴 |
| Pipeline captura → detecção → banco | ⬜ Pendente | 🔴 |
| Filtros combinados no dashboard | ⬜ Pendente | 🔴 |
| Testes de integração | ⬜ Pendente | 🔴 |
| Tratamento de erros (câmera offline, etc) | ⬜ Pendente | 🟡 |

## Sprint 1.3 — Refino (Dias 26–40)

| Tarefa | Status | Prioridade |
|--------|--------|:----------:|
| Relatório PDF formatado | ⬜ Pendente | 🟡 |
| Alertas em tempo real (WS) | ⬜ Pendente | 🟡 |
| Performance (frame rate, latência) | ⬜ Pendente | 🔴 |
| Modo simulação (sem câmera) | ⬜ Pendente | 🟡 |
| Autenticação básica | ⬜ Pendente | 🟢 |

## Sprint 1.4 — Entrega (Dias 41–60)

| Tarefa | Status | Prioridade |
|--------|--------|:----------:|
| Testes com dados reais de fábrica | ⬜ Pendente | 🔴 |
| Documentação de operação | ⬜ Pendente | 🟡 |
| Deploy em homologação | ⬜ Pendente | 🔴 |
| Treinamento operadores | ⬜ Pendente | 🟡 |
| Ajustes finais | ⬜ Pendente | 🔴 |

---

## Entregáveis por Sprint

| Sprint | Data | Entregável |
|--------|------|-----------|
| 1.1 | Dia 10 | API + Dashboard + Detector protótipo |
| 1.2 | Dia 25 | Sistema integrado com câmera real |
| 1.3 | Dia 40 | Performance + alertas + PDF |
| 1.4 | Dia 60 | Sistema em produção homologado |

## Tech Stack

`Python` `FastAPI` `OpenCV` `PostgreSQL` `Redis` `React` `Tailwind` `Docker`
