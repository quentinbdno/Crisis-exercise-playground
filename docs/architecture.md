# Architecture

The platform is split into a SvelteKit frontend and a Django backend.

## Backend

The backend is the authority for:

- authentication and session security
- RBAC/IAM and crisis-cell membership
- scenario and stimulus persistence
- exercise orchestration
- real-time message authorization
- AI agent orchestration
- audit logging
- import/export validation

REST APIs expose durable resources. WebSockets expose exercise-room events.

## Frontend

The frontend is a pure API client. It never reads from the database directly.

It owns:

- responsive enterprise UI
- dark/light theme switching
- English and French translations
- typed REST client
- WebSocket client
- collaborative exercise views

## Runtime

PostgreSQL stores durable data. Redis backs Channels and Celery. Celery workers
handle scheduled stimuli, imports/exports and AI calls.
