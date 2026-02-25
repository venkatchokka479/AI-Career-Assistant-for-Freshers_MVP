# Backend (FastAPI ATS Service)

## Folder Structure
```text
backend/
├── app/
│   ├── api/
│   │   └── match.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── session.py
│   ├── models/
│   │   └── entities.py
│   ├── schemas/
│   │   └── match.py
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── matcher.py
│   │   ├── recommendations.py
│   │   ├── skills.py
│   │   ├── text_extraction.py
│   │   └── vector_store.py
│   └── main.py
├── db_schema.sql
├── requirements.txt
└── Dockerfile
```

## API Examples

### `POST /api/v1/match/resume-text`
```json
{
  "resume_text": "Built FastAPI + React projects with PostgreSQL and Docker",
  "job_title": "Junior Backend Engineer",
  "job_description": "Need Python, FastAPI, SQL, Docker, Redis"
}
```

Response:
```json
{
  "semantic_similarity": 0.74,
  "normalized_score": 87.1,
  "matched_skills": ["docker", "fastapi", "python", "sql"],
  "missing_skills": ["redis"],
  "skill_gap_percentage": 20.0,
  "improvement_recommendations": ["Add at least one project demonstrating redis."],
  "interview_questions": ["Walk me through your most relevant project..."],
  "learning_roadmap": ["Week plan: Learn fundamentals and build a mini-project in redis."],
  "fairness_notes": {
    "excluded_features": ["name", "gender", "age", "college_tier", "photo"],
    "scoring_focus": "semantic relevance + demonstrated skills",
    "next_steps": "Add cohort-level fairness monitoring and drift alerts."
  }
}
```
