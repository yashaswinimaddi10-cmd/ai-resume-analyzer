import pandas as pd

roles = pd.read_csv("data/job_roles.csv")
skills = pd.read_csv("data/skill_dictionary.csv")

print(roles)
print(len(skills), "skills loaded")