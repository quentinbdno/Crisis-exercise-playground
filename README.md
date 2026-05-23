# Crisis Exercise Playground

Enterprise-grade cyber and business crisis exercise platform.

This repository is organized as an API-first monorepo with a strict separation between:

- `frontend/`: SvelteKit, TypeScript, TailwindCSS, i18n and themeable UI
- `backend/`: Django, Django REST Framework, Channels, Celery and PostgreSQL
- `infra/`: Docker Compose, nginx and deployment-oriented configuration
- `docs/`: architecture notes and implementation decisions

## Quick Start

```bash
cp .env.example .env
docker compose up --build
```

Services:

- Frontend: <http://localhost:5173>
- Backend API: <http://localhost:8000/api/>
- Reverse proxy: <http://localhost:8080>

## Architecture Principles

- Frontend communicates only through REST APIs and WebSockets.
- Backend owns authentication, RBAC, exercise isolation, orchestration and audit.
- Real-time collaboration is implemented through Django Channels and Redis.
- Scheduled stimulus injection and AI orchestration are handled by Celery.
- Scenario import/export is designed around ZIP, YAML and CSV workflows.
