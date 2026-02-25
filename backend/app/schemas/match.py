from typing import Any

from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    candidate_id: int | None = None
    candidate_name: str | None = None
    resume_text: str = Field(..., min_length=20)
    job_title: str
    job_description: str


class MatchResponse(BaseModel):
    semantic_similarity: float
    normalized_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    skill_gap_percentage: float
    improvement_recommendations: list[str]
    interview_questions: list[str]
    learning_roadmap: list[str]
    fairness_notes: dict[str, Any]
