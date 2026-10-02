from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, rank_roles

path = "sample_resumes/fake_resume_aarav.pdf"
with open(path, "rb") as f:
    cleaned = clean_text(extract_text(f, path))

found = extract_skills(cleaned, load_skill_dictionary())
roles = load_job_roles()

print("Skills found:", list(found))
print("\nRole ranking:")
for i, (role, score) in enumerate(rank_roles(list(found), roles), start=1):
    print(f"{i}. {role}: {score}%")