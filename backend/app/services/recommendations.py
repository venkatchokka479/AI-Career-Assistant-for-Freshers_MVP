def generate_improvement_recommendations(missing_skills: list[str]) -> list[str]:
    if not missing_skills:
        return ["Profile is well aligned. Focus on project depth and measurable impact."]
    return [
        f"Add at least one project demonstrating {skill}."
        for skill in missing_skills[:5]
    ] + ["Quantify outcomes with metrics (latency, accuracy, cost, users)."]


def generate_interview_questions(job_title: str, missing_skills: list[str]) -> list[str]:
    questions = [
        f"Walk me through your most relevant project for this {job_title} role.",
        "How do you debug a production issue end-to-end?",
    ]
    questions.extend(
        f"How would you learn and apply {skill} in your first 30 days?" for skill in missing_skills[:3]
    )
    return questions


def generate_learning_roadmap(missing_skills: list[str]) -> list[str]:
    if not missing_skills:
        return ["Advance with system design, mock interviews, and open-source contributions."]

    roadmap = []
    for skill in missing_skills[:5]:
        roadmap.append(f"Week plan: Learn fundamentals and build a mini-project in {skill}.")
    roadmap.append("Finalize with a capstone project and STAR-format resume bullets.")
    return roadmap


def fairness_audit_notes() -> dict:
    return {
        "excluded_features": ["name", "gender", "age", "college_tier", "photo"],
        "scoring_focus": "semantic relevance + demonstrated skills",
        "next_steps": "Add cohort-level fairness monitoring and drift alerts.",
    }
