# SRE Agent

[![CI](https://github.com/kogunlowo123/sre-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/sre-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Site Reliability Engineering agent that defines and monitors SLOs/SLIs, manages error budgets, performs capacity planning, automates toil reduction, conducts chaos engineering experiments, and provides reliability scoring across services.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `define_slo` | Define an SLO with SLIs and error budget |
| `check_error_budget` | Check remaining error budget for a service |
| `plan_capacity` | Forecast capacity needs based on growth trends |
| `identify_toil` | Identify repetitive manual tasks that can be automated |
| `run_chaos_experiment` | Run a controlled chaos engineering experiment |
| `score_reliability` | Calculate reliability score for a service |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/slo/define` | Define SLO |
| `GET` | `/api/v1/slo/{service}/budget` | Check error budget |
| `POST` | `/api/v1/capacity/plan` | Plan capacity |
| `POST` | `/api/v1/toil/identify` | Identify toil |
| `POST` | `/api/v1/chaos/run` | Run chaos experiment |
| `GET` | `/api/v1/reliability/{service}/score` | Get reliability score |

## Features

- Slo Management
- Error Budgets
- Capacity Planning
- Toil Reduction
- Chaos Engineering
- Reliability Scoring

## Integrations

- Prometheus
- Grafana
- Openslo
- Litmus Chaos
- Pagerduty

## Architecture

```
sre-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── sre_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Prometheus + Grafana + OpenSLO**

---

Built as part of the Enterprise AI Agent Platform.
