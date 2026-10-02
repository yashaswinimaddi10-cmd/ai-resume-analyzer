import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(path="data/job_roles.csv"):
    """Returns {role: [list of required skills]}"""
    df = pd.read_csv(path)
    roles = {}
    for _, row in df.iterrows():
        roles[row["role"]] = [s.strip() for s in row["required_skills"].split(";")]
    return roles


def _split_skills(text):
    # each "word" for TF-IDF is one whole skill, e.g. "machine learning"
    return [s for s in text.split(";") if s]


def rank_roles(found_skills, roles):
    role_names = list(roles.keys())
    job_docs = [";".join(roles[r]) for r in role_names]
    resume_doc = ";".join(found_skills)

    vectorizer = TfidfVectorizer(tokenizer=_split_skills, lowercase=False,
                                 token_pattern=None)
    job_vectors = vectorizer.fit_transform(job_docs)
    resume_vector = vectorizer.transform([resume_doc])

    scores = cosine_similarity(resume_vector, job_vectors)[0]
    ranked = sorted(zip(role_names, scores * 100), key=lambda x: x[1], reverse=True)
    return [(role, round(score, 1)) for role, score in ranked]


def skill_gap(found_skills, required_skills):
    """Compare what the resume has with what the role needs."""
    found_set = set(found_skills)
    have = [s for s in required_skills if s in found_set]
    missing = [s for s in required_skills if s not in found_set]
    coverage = round(100 * len(have) / len(required_skills), 1) if required_skills else 0.0
    return {"coverage": coverage, "have": have, "missing": missing}