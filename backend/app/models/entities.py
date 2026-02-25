from sqlalchemy import JSON, Column, DateTime, Float, Integer, String, Text, func

from app.db.session import Base


class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=True)
    full_name = Column(String(255), nullable=True)
    resume_text = Column(Text, nullable=False)
    extracted_skills = Column(JSON, nullable=False, default=list)
    embedding = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class JobRole(Base):
    __tablename__ = "job_roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    required_skills = Column(JSON, nullable=False, default=list)
    embedding = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class MatchResult(Base):
    __tablename__ = "match_results"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, nullable=False, index=True)
    job_id = Column(Integer, nullable=False, index=True)
    semantic_score = Column(Float, nullable=False)
    skill_gap_percentage = Column(Float, nullable=False)
    matched_skills = Column(JSON, nullable=False, default=list)
    missing_skills = Column(JSON, nullable=False, default=list)
    recommendations = Column(JSON, nullable=False, default=list)
    interview_questions = Column(JSON, nullable=False, default=list)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
