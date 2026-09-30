from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills, group_by_category

path = "sample_resumes/fake_resume_aarav.pdf"
with open(path, "rb") as f:
    cleaned = clean_text(extract_text(f, path))

skill_dict = load_skill_dictionary()
found = extract_skills(cleaned, skill_dict)

print("Skills found:", len(found))
for category, skills in group_by_category(found).items():
    print(f"  {category}: {', '.join(skills)}")

print("\nAlias test:", list(extract_skills("i use sklearn and cpp with apis", skill_dict)))
print("Glue test:", list(extract_skills("javascript and pythonic code", skill_dict)))