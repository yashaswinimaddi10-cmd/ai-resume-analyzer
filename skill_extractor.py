import re
import pandas as pd


def load_skill_dictionary(path="data/skill_dictionary.csv"):
    """Returns {skill: {"category": ..., "names": [skill + its aliases]}}"""
    df = pd.read_csv(path).fillna("")
    skills = {}
    for _, row in df.iterrows():
        names = [row["skill"]]
        if row["aliases"]:
            names += [a.strip() for a in row["aliases"].split(";") if a.strip()]
        skills[row["skill"]] = {"category": row["category"], "names": names}
    return skills


def _found(name, text):
    # \b breaks on c++ and c#, so we build our own "word edges":
    # the name must NOT be glued to another letter, digit, + or #
    pattern = r"(?<![a-z0-9+#])" + re.escape(name) + r"(?![a-z0-9+#])"
    return re.search(pattern, text) is not None


def extract_skills(cleaned_text, skill_dict):
    """Returns {skill: category} for every skill found in the text."""
    found = {}
    for skill, info in skill_dict.items():
        if any(_found(name, cleaned_text) for name in info["names"]):
            found[skill] = info["category"]
    return found


def group_by_category(found):
    groups = {}
    for skill, category in found.items():
        groups.setdefault(category, []).append(skill)
    return groups