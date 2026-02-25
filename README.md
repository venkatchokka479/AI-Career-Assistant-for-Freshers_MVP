# AI-Powered ATS for Students & Freshers

Production-ready starter architecture for a semantic ATS that focuses on fresher profiles.

## Stack
- **Backend:** FastAPI, PostgreSQL, SQLAlchemy, sentence-transformers, FAISS/Chroma-ready vector abstraction
- **Frontend:** Next.js + TailwindCSS dashboard scaffold
- **AI Layer:** all-MiniLM-L6-v2 embeddings, cosine similarity, skill-gap detection, recommendations

## Quick Start
```bash
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local

docker compose -f infra/docker-compose.yml up --build
```

Backend: `http://localhost:8000/docs`  
Frontend: `http://localhost:3000`

## Core APIs
- `POST /api/v1/match/resume-file`
- `POST /api/v1/match/resume-text`
- `GET /api/v1/health`

## Repository Layout
- `backend/` FastAPI service
- `frontend/` Next.js dashboard scaffold
- `infra/` Docker and deployment material
- `docs/` architecture and scaling notes
