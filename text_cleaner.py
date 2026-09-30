import re


def clean_text(text):
    text = text.lower()                                # 1. all lowercase

    # 2. remove weird symbols, but KEEP letters, numbers, + # . - /
    text = re.sub(r"[^a-z0-9+#.\-/\s]", " ", text)

    # 3. remove dots at the END of words ("python." -> "python")
    #    but keep dots inside words (".net", "node.js")
    text = re.sub(r"\.+(?=\s|$)", " ", text)

    # 4. squash many spaces into one
    text = re.sub(r"\s+", " ", text).strip()
    return text