# StudyMate

AI-powered study companion for GCSE and Matric learners — personalised check-ins, quizzes, and progress tracking for students, parents, and teachers.

## Monorepo Structure

```
studymate/
├── src/
│   ├── web/          # Next.js 14 PWA — student, parent, and teacher interfaces
│   ├── api/          # ASP.NET Core 8 — StudyMate.Api, .Domain, .Application, .Infrastructure
│   └── bot/          # Telegram bot agent — creates GitHub user stories via conversational AI
├── db/
│   └── changelog/    # Liquibase migration scripts
├── .github/
│   └── workflows/    # CI pipelines
└── docker-compose.yml  # Full local stack
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind CSS |
| Backend | ASP.NET Core 8 Minimal API, MediatR, EF Core |
| Database | PostgreSQL (Supabase in production) |
| Migrations | Liquibase |
| Auth | Supabase Auth |
| Background jobs | Hangfire |
| Email | SendGrid |
| Payments | Stripe |
| Hosting | Azure Container Apps |

## DDD Bounded Contexts

- **Learning** — check-ins, quizzes, sessions, streaks
- **Identity** — users, roles, authentication
- **Curriculum** — subjects, topics, GCSE/Matric syllabus
- **Reporting** — progress, analytics, parent dashboards
- **Safeguarding** — content moderation, age-appropriate controls

## Getting Started (local)

### Prerequisites

- Docker Desktop
- .NET 8 SDK
- Node.js 20+
- Python 3.11+

### Run the full stack

```bash
docker compose up
```

| Service | URL |
|---|---|
| Web (Next.js) | http://localhost:3000 |
| API (.NET) | http://localhost:5000 |
| API Health | http://localhost:5000/health |
| PostgreSQL | localhost:5432 |

### Run services individually

```bash
# Frontend
cd src/web && npm install && npm run dev

# Backend
cd src/api && dotnet run --project StudyMate.Api

# Telegram bot
cd src/bot && py -m bot.bot
```

## Bot Agent

The Telegram bot (`src/bot/`) is an EdTech expert agent that creates GitHub user stories from your phone. Message it a feature requirement, it asks clarifying questions, proposes a story breakdown, and raises GitHub issues when you confirm.

See [`src/bot/.env.example`](src/bot/.env.example) for required environment variables.
