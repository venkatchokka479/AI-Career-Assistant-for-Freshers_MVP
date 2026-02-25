from collections import OrderedDict

COMMON_SKILLS = {
    "python",
    "java",
    "c++",
    "sql",
    "postgresql",
    "mongodb",
    "fastapi",
    "django",
    "flask",
    "react",
    "next.js",
    "tailwindcss",
    "docker",
    "kubernetes",
    "aws",
    "gcp",
    "git",
    "redis",
    "machine learning",
    "nlp",
    "pandas",
    "numpy",
    "data structures",
    "algorithms",
    "rest api",
    "microservices",
}


def extract_skills(text: str, skill_lexicon: set[str] | None = None) -> list[str]:
    lexicon = skill_lexicon or COMMON_SKILLS
    lower_text = text.lower()
    found = OrderedDict()
    for skill in sorted(lexicon):
        if skill in lower_text:
            found[skill] = True
    return list(found.keys())


def detect_skill_gap(candidate_skills: list[str], required_skills: list[str]) -> tuple[list[str], list[str], float]:
    candidate_set = set(map(str.lower, candidate_skills))
    required_set = set(map(str.lower, required_skills))

    matched = sorted(candidate_set.intersection(required_set))
    missing = sorted(required_set.difference(candidate_set))

    if not required_set:
        gap = 0.0
    else:
        gap = (len(missing) / len(required_set)) * 100

    return matched, missing, round(gap, 2)
