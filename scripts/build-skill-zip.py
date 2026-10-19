"""Builds dist/siteflock-website-builder.zip for uploading the skill to claude.ai
(Customize -> Skills). claude.ai needs the skill folder itself at the top of the
ZIP, so entries are siteflock-website-builder/SKILL.md and so on.

Usage: python scripts/build-skill-zip.py
"""

import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "siteflock", "skills")
NAME = "siteflock-website-builder"
OUT = os.path.join(ROOT, "dist", NAME + ".zip")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as archive:
    for folder, dirs, files in os.walk(os.path.join(SKILLS, NAME)):
        dirs.sort()
        for file in sorted(files):
            path = os.path.join(folder, file)
            archive.write(path, os.path.relpath(path, SKILLS).replace(os.sep, "/"))

with zipfile.ZipFile(OUT) as archive:
    names = archive.namelist()
assert NAME + "/SKILL.md" in names, "SKILL.md missing"
assert all(n.startswith(NAME + "/") for n in names), "skill folder must be the ZIP's top level"
print(OUT)
for n in names:
    print("  " + n)
