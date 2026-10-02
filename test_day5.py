from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, rank_roles, skill_gap
from roadmap_generator import generate_roadmap

path = "sample_resumes/fake_resume_aarav.pdf"
with open(path, "rb") as f:
    cleaned = clean_text(extract_text(f, path))

found = list(extract_skills(cleaned, load_skill_dictionary()))
roles = load_job_roles()

target = "Machine Learning Engineer"
gap = skill_gap(found, roles[target])

print("Target role:", target)
print("Match score (skill coverage):", gap["coverage"], "%")
print("Skills you have:", gap["have"])
print("Missing skills:", gap["missing"])

print("\nTop 3 recommended roles:")
for i, (role, score) in enumerate(rank_roles(found, roles)[:3], start=1):
    print(f"{i}. {role} - {score}%")

print("\nRoadmap:")
for week, topic in generate_roadmap(gap["missing"]):
    print(f"{week}: {topic}")

print("\nCoverage for every role:")
for role, skills in roles.items():
    print(f"  {role}: {skill_gap(found, skills)['coverage']}%")