# agents.md

## Project Name

Crisis Simulation Platform

## Purpose

This project is a SaaS B2B cybersecurity web platform for preparing, orchestrating and replaying cyber crisis simulation exercises.

The platform allows administrators and game masters to:
- manage users, roles and permissions;
- create crisis cells;
- create, import and export crisis scenarios;
- define scheduled stimuli;
- attach media files to stimuli;
- run live crisis exercises;
- manage real-time communication channels;
- monitor player activity;
- audit all messages and events;
- prepare future AI-driven simulated participants.

The platform must be designed as a professional enterprise-grade application, inspired by:
- crisis management platforms;
- GRC tools;
- SOC/CERT collaboration tools;
- Microsoft Teams / Slack-style communication;
- tabletop cyber exercise orchestration tools;
- serious cybersecurity dashboards.

The application is not a simple chat tool. It is a structured crisis exercise sandbox.

---

## Core Principles

When contributing to this project, always follow these principles:

1. Keep frontend and backend strictly separated.
2. Keep business logic in the backend.
3. Use APIs and WebSockets between frontend and backend.
4. Enforce permissions server-side.
5. Design for auditability.
6. Design for multilingual usage from the beginning.
7. Support both dark and light themes, with dark theme as default.
8. Avoid hardcoded UI text.
9. Avoid over-engineering the first version.
10. Prefer simple, explicit and maintainable code.
11. Use a serious B2B cybersecurity SaaS design language.
12. Avoid marketing-heavy visuals and gaming aesthetics.

---

## Architecture Overview

The project must be organized with a clear separation between frontend and backend.

Recommended structure:

```text
project-root/
├── agents.md
├── README.md
├── docker-compose.yml
├── frontend/
├── backend/
├── docs/
├── infra/
├── scripts/
└── scenarios/
```

---

## Frontend Requirements

The frontend must be developed as a separate application.

Use:

- Next.js
- TypeScript
- Tailwind CSS v4
- shadcn/ui
- lucide-react
- i18n support
- dark/light theme support
- WebSocket client
- REST API client

The frontend must communicate with the backend only through:
- REST APIs;
- WebSockets.

The frontend must never access the database directly.

Do not put backend business logic in frontend components.

---

## Frontend Design Direction

Create a premium, sober, professional B2B cybersecurity SaaS interface.

The UI must feel:
- serious;
- operational;
- enterprise-grade;
- dashboard-oriented;
- cybersecurity-focused;
- suitable for crisis management rooms;
- suitable for SOC/CERT and executive crisis teams.

Avoid:
- gaming aesthetics;
- neon cyberpunk;
- childish visuals;
- excessive gradients;
- marketing landing-page style;
- oversized decorative components;
- simplistic CRUD-only layouts.

---

## UI Theme Requirements

The default theme must be dark.

### Dark Theme

Use:
- dark blue-black backgrounds;
- dark cards;
- thin borders;
- subtle contrast;
- readable typography;
- compact dashboard density;
- clear hierarchy.

Recommended visual style:
- background: blue-tinted black;
- cards: dark navy / charcoal;
- borders: thin muted blue-gray;
- primary color: cyber blue;
- active status: green;
- warning status: orange;
- critical status: red.

### Light Theme

A light theme must exist, but it is secondary.

The design system must allow users to switch themes.

Theme preference must persist.

---

## Color Semantics

Use consistent semantic colors:

- Primary: cyber blue
- Active / running / online: green
- Warning / pending / delayed: orange
- Critical / failed / incident: red
- Muted / inactive / disabled: gray
- Informational: blue

Do not hardcode raw colors in many components. Prefer centralized tokens.

---

## UI Components

Use shadcn/ui components as the default design system.

Use lucide-react for icons.

Expected component usage:

- Button
- Card
- Badge
- Table
- Tabs
- Dialog
- DropdownMenu
- Tooltip
- Sheet
- Command
- Input
- Textarea
- Select
- Switch
- Separator
- ScrollArea
- Avatar
- Alert
- Toast / Sonner
- Progress
- Skeleton

Build reusable application-specific components on top of shadcn/ui.

---

## Layout Requirements

The main application must use a dashboard layout.

Required layout elements:

- fixed collapsible sidebar on the left;
- sticky topbar;
- search bar in the topbar;
- notification button/menu;
- user profile menu;
- responsive content area;
- grid-based dashboards;
- status badges;
- compact tables;
- activity feeds;
- timeline components.

The layout must be desktop-first but responsive.

---

## Sidebar Requirements

The sidebar must be fixed and collapsible.

It should contain navigation entries such as:

- Dashboard
- Exercises
- Scenarios
- Crisis Cells
- Users
- AI Agents
- Media Simulation
- Reports
- Audit Logs
- Settings

Sidebar behavior:
- expanded mode with labels;
- collapsed mode with icons only;
- active route indicator;
- smooth width transition;
- no excessive animation.

Use lucide-react icons.

---

## Topbar Requirements

The topbar must be sticky.

It must include:

- global search bar;
- notifications;
- user profile menu;
- current organization or workspace if relevant;
- theme switcher if appropriate;
- language switcher if appropriate.

The topbar should stay professional and compact.

---

## Animation Requirements

Use only discreet animations:

- hover transitions;
- subtle focus transitions;
- sidebar collapse transitions;
- pulse animation for live statuses;
- notification indicator pulse where useful.

Avoid:
- large animated gradients;
- flashy motion;
- gamified effects;
- decorative animations that reduce readability.

---

## Required Frontend Pages

The application should include these pages:

- Login
- Invitation acceptance
- MFA setup
- Dashboard
- Users
- AI Agents
- Crisis Cells
- Scenarios
- Scenario Detail
- Scenario Editor
- Exercises
- Exercise Room
- Game Master Control Room
- Reports
- Audit Logs
- Settings

---

## Login Page Requirements

Create a login page with:

- dark blue-black background;
- subtle grid background;
- centered authentication card;
- product logo / platform name;
- email/password fields;
- SSO-ready buttons or placeholders;
- MFA flow placeholder;
- clean enterprise style.

The login page must avoid marketing-heavy sections.

It should feel like a secure B2B SaaS product.

---

## Dashboard Requirements

The dashboard must include:

- KPI cards;
- list of active exercises;
- upcoming stimuli timeline;
- AI agents status panel;
- active participants;
- recent audit events;
- live exercise status indicators.

Example KPI cards:

- Active exercises
- Connected players
- Upcoming stimuli
- AI agents online
- Open alerts
- Critical events

Use:
- cards with dark backgrounds;
- thin borders;
- status badges;
- responsive grids;
- live pulse indicators for running exercises.

---

## Exercise Dashboard / Active Exercises

The dashboard must display active exercises with:

- exercise name;
- linked scenario;
- status;
- current exercise time;
- number of participants;
- number of active channels;
- next scheduled stimulus;
- severity indicator if applicable.

Statuses:

- draft;
- scheduled;
- running;
- paused;
- completed;
- archived.

Use semantic badges:
- running: green;
- paused: orange;
- completed: muted;
- critical: red.

---

## Timeline UI

Timeline components must be used for:

- upcoming stimuli;
- sent stimuli;
- exercise replay;
- audit events;
- scenario editor preview.

Timeline entries should display:

- planned time;
- actual delivery time if applicable;
- stimulus type;
- sender;
- recipient;
- status;
- attachment indicator.

---

## AI Agents Dashboard Panel

The dashboard must include an AI Agents panel showing:

- agent name;
- persona type;
- linked scenario or exercise;
- online/offline status;
- last activity;
- linked LLM connector if configured.

AI agent UI must be visually distinct from human users but still professional.

---

## Frontend Responsibilities

The frontend is responsible for:
- authentication screens;
- user interface;
- scenario editor;
- exercise room;
- real-time chat display;
- Game Master control panels;
- user management screens;
- AI agent screens;
- settings screens;
- i18n;
- theme switching.

---

## Backend Requirements

The backend must be developed as a separate application.

Recommended stack:

- Python
- Django
- Django REST Framework
- Django Channels
- PostgreSQL
- Redis
- Celery
- Celery Beat

### Backend Responsibilities

The backend is responsible for:
- authentication;
- MFA;
- SSO readiness;
- users;
- roles;
- permissions;
- crisis cells;
- scenario management;
- stimulus management;
- exercise orchestration;
- real-time messaging;
- audit logging;
- import/export;
- media/file management;
- AI agent placeholders;
- LLM connector settings.

---

## Infrastructure Requirements

The project should be Docker-ready.

Recommended components:

- frontend container;
- backend container;
- PostgreSQL container;
- Redis container;
- Celery worker container;
- Celery beat container;
- reverse proxy container;
- S3-compatible storage later if needed.

Use environment variables for configuration.

Do not commit secrets.

---

## Internationalization

The platform must support multiple languages from the beginning.

Default languages:

- French
- English

All visible UI strings must be translatable:
- menus;
- buttons;
- labels;
- errors;
- notifications;
- dialogs;
- tables;
- statuses.

Do not hardcode French-only or English-only text directly in components.

---

## Core Domain Objects

The backend data model should be built around these entities:

- User
- Role
- Permission
- CrisisCell
- Scenario
- Stimulus
- Attachment
- Exercise
- ExerciseRoom
- Channel
- Message
- DirectMessage
- AIAgent
- LLMConnector
- AuditLog

Keep the domain model explicit and auditable.

---

## IAM and User Management

Users must include:

- first name;
- last name;
- email;
- role;
- user type;
- MFA status;
- active/inactive status;
- crisis cell memberships;
- exercise participation history.

User types:

- human;
- ai_agent.

Roles:

- Admin;
- Game Master;
- Observer;
- Player.

### Admin

The Admin can:
- manage the full platform;
- manage users;
- manage roles;
- manage permissions;
- manage settings;
- view all exercises;
- view all messages;
- view all audit logs.

### Game Master

The Game Master can:
- create scenarios;
- modify scenarios;
- create exercises;
- manage exercises;
- invite players;
- invite crisis cells;
- manually inject stimuli;
- monitor exercise activity;
- view all messages in exercises they manage.

### Observer

The Observer can:
- view exercises;
- view all messages;
- view audit logs;
- observe activity;
- not modify anything.

### Player

The Player can:
- access assigned exercises;
- receive stimuli;
- participate in authorized channels;
- send messages;
- view their own exercise history.

Players must not see channels, messages or stimuli they are not authorized to access.

---

## Human Users Interface

The user management page must allow:

- creating users;
- inviting users;
- disabling users;
- searching users;
- filtering users;
- viewing MFA status;
- viewing assigned crisis cells;
- viewing assigned roles.

User table columns:

- first name;
- last name;
- email;
- role;
- MFA status;
- crisis cells;
- status.

Clicking a user should open a detail view with:

- profile information;
- effective permissions;
- assigned roles;
- crisis cell memberships;
- exercise history;
- audit activity;
- ability to add or remove permissions.

---

## AI Agents Interface

AI Agents must have a dedicated page separate from human users.

The AI Agents page must show only users with:

```text
user_type = ai_agent
```

Clicking an AI Agent should show:

- name;
- status;
- associated scenarios;
- associated exercises;
- Markdown persona;
- linked LLM connector if any;
- behavior settings.

AI agents are modeled as users, but they must remain visually and functionally distinct in the UI.

---

## Crisis Cells

A Crisis Cell is a group of players.

A user can belong to one or more crisis cells.

A crisis cell can be invited to an exercise.

Crisis cells should support:

- name;
- description;
- members;
- default roles;
- associated exercises.

Examples:

- Executive Crisis Cell
- IT Crisis Cell
- Communication Crisis Cell
- Legal Crisis Cell
- Business Continuity Cell

---

## Scenario Management

A scenario is a reusable package containing:

- scenario metadata;
- a list of stimuli;
- attached media files;
- optional AI agent personas.

A scenario is not an exercise.
A scenario is a template.
An exercise is a live execution of a scenario.

---

## Scenario Package Format

Supported structure:

```text
scenario.zip
├── scenario.yaml
├── media/
│   ├── image.png
│   ├── video.mp4
│   └── document.pdf
└── ai_agents/
    ├── journalist.md
    ├── customer.md
    └── employee.md
```

Do not add a `docs/` folder unless explicitly requested later.

---

## Scenario YAML

The `scenario.yaml` file should describe:

- scenario name;
- description;
- author;
- version;
- estimated duration;
- stimuli;
- media references;
- AI agent references.

Example structure:

```yaml
name: Ransomware Crisis Exercise
description: Cyber crisis exercise simulating ransomware propagation.
version: 1.0
duration: 04:00:00

stimuli:
  - id: stim-001
    planned_time: 00:05:00
    sender: game_master
    recipient: it_crisis_cell
    type: chat_message
    channel: general
    message: Several users report encrypted files on shared drives.
    attachment: null

  - id: stim-002
    planned_time: 00:20:00
    sender: fake_journalist
    recipient: communication_manager
    type: email
    channel: direct_message
    message: We have received reports of a cyberattack affecting your company. Can you confirm?
    attachment: media/journalist-email.pdf
```

---

## Stimulus Model

A stimulus is an event injected into an exercise.

Stimulus fields:

- planned time;
- sender;
- recipient;
- type;
- message;
- optional attachment;
- target channel;
- delivery status;
- linked scenario;
- linked exercise when executed.

Stimulus types:

- chat message;
- email;
- fake tweet;
- fake news;
- voice call;
- video;
- document;
- system notification.

A stimulus can be sent by:

- Game Master;
- AI Agent;
- system.

---

## Scenario UI

The scenario list page must include:

- list of existing scenarios;
- create scenario button;
- import scenario button;
- export scenario button;
- duplicate scenario action.

Scenario table columns:

- name;
- author;
- created at;
- updated at;
- number of stimuli;
- number of media files;
- number of AI agents;
- status.

Scenario detail page must include:

- metadata;
- stimuli table;
- media browser;
- AI agents;
- attachments preview.

Scenario editor must behave like a table/spreadsheet.

Stimuli table columns:

- planned time;
- sender;
- recipient;
- stimulus type;
- message preview;
- attachment;
- target channel.

The editor must support:

- add stimulus;
- edit stimulus;
- delete stimulus;
- reorder stimuli;
- attach media;
- validate scenario;
- import YAML;
- import CSV;
- import ZIP;
- export YAML;
- export CSV;
- export ZIP.

---

## Exercise Management

An exercise is the live execution of a scenario.

An exercise contains:

- exercise room;
- global chat;
- channels;
- direct messages;
- participants;
- crisis cells;
- game masters;
- observers;
- sent stimuli;
- message history;
- audit logs.

Exercise fields:

- name;
- scenario;
- status;
- start time;
- end time;
- current exercise time;
- participants;
- crisis cells;
- game masters;
- observers.

Exercise statuses:

- draft;
- scheduled;
- running;
- paused;
- completed;
- archived.

---

## Exercise Room

The exercise room must look like a professional collaborative chat interface.

It should be inspired by:
- Microsoft Teams;
- Slack;
- Discord enterprise layout.

The exercise room should contain:

- channel list;
- direct messages;
- participants;
- central message area;
- right-side context panel;
- exercise clock;
- active scenario information.

### Channels

There must be a general channel for the exercise.

Users may create additional channels if authorized.

Users may add participants to channels if authorized.

Players only see:
- channels they belong to;
- direct messages addressed to them;
- authorized stimuli.

Admins, Game Masters and Observers can see:
- all channels;
- all direct messages;
- all stimuli;
- full audit logs.

---

## Messages

Messages must include:

- sender;
- sender type;
- channel;
- timestamp;
- exercise timestamp;
- body;
- attachments;
- linked stimulus if applicable.

All messages must be persisted.

All messages must be auditable.

Do not rely only on frontend visibility filters for confidentiality.
Permissions must be enforced server-side.

---

## Real-Time Communication

Use WebSockets for:

- live messages;
- stimulus delivery;
- participant presence;
- typing indicators if implemented;
- exercise status updates;
- notifications;
- Game Master commands.

The backend must remain the source of truth.

---

## Game Master Control Room

The Game Master must have a dedicated control interface.

It must allow:

- launching an exercise;
- pausing an exercise;
- resuming an exercise;
- ending an exercise;
- accelerating or controlling the timeline;
- manually injecting a stimulus;
- resending a stimulus;
- monitoring all conversations;
- monitoring participants;
- monitoring AI agents;
- viewing upcoming stimuli;
- viewing delivery status;
- viewing unanswered questions.

Suggested panels:

- global exercise timeline;
- upcoming stimuli;
- active channels;
- direct messages;
- unanswered player questions;
- AI activity;
- audit stream;
- quick actions.

---

## Celery Usage

Use Celery for asynchronous and scheduled tasks.

Use Celery Beat for periodic or scheduled checks.

Recommended Celery use cases:

- sending scheduled stimuli;
- importing scenario ZIP files;
- exporting scenarios;
- generating exercise reports;
- processing media;
- generating thumbnails;
- calling LLM providers;
- running AI agent responses;
- sending notifications.

Do not block HTTP requests with long-running operations.

---

## AI Agents

AI agents are a future-oriented feature but should be modeled early.

For the first version:

- model AI agents as users with `user_type = ai_agent`;
- store a Markdown persona;
- allow association with scenarios;
- allow association with exercises;
- keep autonomous behavior minimal.

AI agent personas may be stored in scenario packages under:

```text
ai_agents/
```

Each persona is a Markdown file.

Example:

```markdown
# Name
Cyber Journalist

# Role
Technology journalist working for a major news website.

# Personality
Curious, reactive, persistent.

# Objectives
- Obtain confirmation of the incident.
- Request impact assessment.
- Increase external pressure.
- Push the communication team to respond.

# Communication Style
Professional but insistent.

# Behavior Rules
- Do not reveal internal exercise mechanics.
- Escalate pressure if ignored.
- Stay realistic.
```

---

## LLM Connectors

LLM connectors belong to global platform settings, not scenarios.

Plan support for:

- OpenAI-compatible APIs;
- Ollama;
- Azure OpenAI;
- custom local endpoints.

LLM connector fields may include:

- name;
- provider;
- base URL;
- model name;
- API key;
- default temperature;
- timeout;
- active status.

Secrets must be stored only server-side.

Never expose API keys to the frontend.

---

## Import and Export

The platform must support scenario import and export.

Supported formats:

- YAML;
- CSV;
- ZIP with media files.

When importing:

- validate the package structure;
- validate required fields;
- verify media references;
- return clear validation errors;
- do not silently discard invalid data.

When exporting:

- generate deterministic package structure;
- include scenario YAML;
- include media files;
- include AI agent Markdown files if present.

---

## Audit Logging

Auditability is a core requirement.

Log important actions, including:

- user creation;
- user invitation;
- role changes;
- permission changes;
- MFA changes;
- scenario creation;
- scenario modification;
- scenario import;
- scenario export;
- exercise creation;
- exercise start;
- exercise pause;
- exercise resume;
- exercise end;
- stimulus sending;
- manual stimulus injection;
- message creation;
- file upload;
- AI agent action;
- LLM connector change.

Audit logs should include:

- actor;
- action;
- target object;
- timestamp;
- IP address if available;
- metadata.

---

## Security Requirements

Implement or prepare for:

- MFA;
- SSO;
- RBAC;
- secure password handling;
- server-side permissions;
- audit logs;
- secure file upload validation;
- safe media serving;
- secret management;
- CSRF protection;
- secure cookies;
- rate limiting where relevant.

Never trust frontend-side permission checks alone.

---

## SSO Requirements

The platform must be SSO-ready.

Prepare support for:

- OIDC;
- SAML;
- Microsoft Entra ID;
- Google Workspace;
- Keycloak.

SSO does not need to be fully implemented in the first version, but the architecture must not prevent it.

---

## MFA Requirements

The platform must support or prepare support for MFA.

Recommended first implementation:

- TOTP;
- QR code enrollment;
- backup codes later.

MFA status must be visible in user management.

---

## API Guidelines

APIs must be:

- explicit;
- versionable;
- documented;
- permission-protected;
- predictable.

Prefer API paths such as:

```text
/api/v1/users/
/api/v1/ai-agents/
/api/v1/crisis-cells/
/api/v1/scenarios/
/api/v1/stimuli/
/api/v1/exercises/
/api/v1/channels/
/api/v1/messages/
/api/v1/audit-logs/
/api/v1/settings/llm-connectors/
```

---

## WebSocket Guidelines

Use WebSockets for real-time interactions.

Suggested channels:

```text
/ws/exercises/{exercise_id}/
/ws/exercises/{exercise_id}/channels/{channel_id}/
/ws/exercises/{exercise_id}/gm-control/
```

All WebSocket connections must be authenticated.

Permissions must be checked when connecting and when sending events.

---

## Development Priorities

Build in this order:

1. Project structure
2. Backend foundation
3. Frontend foundation with Next.js, Tailwind CSS v4, shadcn/ui and lucide-react
4. Design system tokens, dark/light theme and layout shell
5. Authentication
6. User model
7. Role and permission model
8. MFA preparation
9. Crisis cells
10. Scenario model
11. Stimulus model
12. Attachment model
13. Scenario list page
14. Scenario detail page
15. Scenario editor
16. Scenario import/export
17. Exercise model
18. Channel model
19. Message model
20. WebSocket messaging
21. Exercise room
22. Game Master control room
23. Celery stimulus scheduling
24. Audit logs
25. AI agent placeholders
26. LLM connector settings
27. Reporting and debriefing

---

## Coding Guidelines

- Use clear names.
- Keep files focused.
- Avoid large monolithic components.
- Keep serializers explicit.
- Keep permissions explicit.
- Keep UI components reusable.
- Keep service functions testable.
- Avoid hidden side effects.
- Validate inputs.
- Return clear errors.
- Log audit-relevant actions.
- Do not silently ignore failures.
- Do not introduce unrelated dependencies without justification.

---

## Frontend Coding Guidelines

- Use TypeScript consistently.
- Use typed API clients.
- Use shadcn/ui components.
- Use lucide-react icons.
- Use Tailwind CSS v4 design tokens.
- Keep UI strings in translation files.
- Keep theme tokens centralized.
- Build reusable components.
- Avoid hardcoded colors in components.
- Use layout components for repeated structures.
- Handle loading states.
- Handle error states.
- Handle empty states.
- Keep dashboard density professional and readable.
- Prefer sober product UI over visual decoration.

---

## Backend Coding Guidelines

- Keep business logic server-side.
- Use Django models for core entities.
- Use DRF serializers for validation.
- Use permissions for access control.
- Use services for complex operations.
- Use Celery for long-running tasks.
- Use transactions where consistency matters.
- Use audit logging for important actions.
- Write migrations carefully.
- Avoid putting business logic in views when it should be in services.

---

## Testing Guidelines

Add tests progressively for:

- user permissions;
- scenario import validation;
- scenario export;
- stimulus scheduling;
- message visibility;
- exercise access control;
- audit logging;
- API validation.

At minimum, every critical business rule should have a test or a clear validation path.

---

## Definition of Done

A feature is complete only when:

- backend model/API exists;
- frontend view exists if relevant;
- permissions are enforced server-side;
- UI strings are translated;
- dark and light modes are supported;
- errors are handled;
- loading states are handled;
- audit-relevant actions are logged;
- basic tests or validation paths exist;
- documentation is updated if the behavior is important.

---

## Important Product Constraints

Do not implement the media simulation platform yet unless explicitly requested.

Media simulation will be addressed later.

For now, prepare the architecture so future modules can support:

- fake Twitter/X;
- fake news websites;
- fake customer portals;
- fake employee intranet;
- fake email interfaces;
- simulated phone calls;
- voice messages.

Do not block future extension with overly rigid models.

---

## Current MVP Scope

The MVP should focus on:

- B2B SaaS cybersecurity UI foundation;
- login page with subtle grid background;
- dashboard layout;
- collapsible sidebar;
- sticky topbar;
- KPI dashboard;
- active exercises list;
- exercise timeline;
- AI agents panel;
- IAM;
- users;
- AI agent placeholders;
- crisis cells;
- scenarios;
- stimuli;
- attachments;
- scenario import/export;
- exercises;
- real-time chat;
- Game Master visibility;
- audit logs.

Reporting, advanced AI behavior and full media simulation are later phases.
