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
    job_vectors = vectorizer.fit_transform(job_docs)      # learn weights from the jobs
    resume_vector = vectorizer.transform([resume_doc])    # turn the resume into numbers

    scores = cosine_similarity(resume_vector, job_vectors)[0]
    ranked = sorted(zip(role_names, scores * 100), key=lambda x: x[1], reverse=True)
    return [(role, round(score, 1)) for role, score in ranked]