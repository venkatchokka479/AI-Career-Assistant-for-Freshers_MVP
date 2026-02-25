import numpy as np

from app.services.embeddings import EmbeddingService, cosine_similarity
from app.services.recommendations import (
    fairness_audit_notes,
    generate_improvement_recommendations,
    generate_interview_questions,
    generate_learning_roadmap,
)
from app.services.skills import detect_skill_gap, extract_skills


class ATSMatcher:
    @staticmethod
    def run_match(resume_text: str, job_title: str, job_description: str) -> dict:
        resume_embedding = EmbeddingService.embed_text(resume_text)
        job_embedding = EmbeddingService.embed_text(job_description)

        semantic_score = cosine_similarity(resume_embedding, job_embedding)
        normalized_score = float(np.clip((semantic_score + 1) / 2 * 100, 0, 100))

        candidate_skills = extract_skills(resume_text)
        required_skills = extract_skills(job_description)
        matched, missing, gap_percentage = detect_skill_gap(candidate_skills, required_skills)

        return {
            "semantic_similarity": round(semantic_score, 4),
            "normalized_score": round(normalized_score, 2),
            "matched_skills": matched,
            "missing_skills": missing,
            "skill_gap_percentage": gap_percentage,
            "improvement_recommendations": generate_improvement_recommendations(missing),
            "interview_questions": generate_interview_questions(job_title, missing),
            "learning_roadmap": generate_learning_roadmap(missing),
            "fairness_notes": fairness_audit_notes(),
            "embeddings": {
                "resume": resume_embedding.tolist(),
                "job": job_embedding.tolist(),
            },
        }
