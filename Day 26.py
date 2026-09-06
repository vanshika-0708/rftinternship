"""
Day 26 - AI Resume Screening Tool (simple keyword-matching version)

Folder structure expected:
    resumes/
        candidate1.txt
        candidate2.txt
        ...

Each resume .txt file should have lines like:
    Name: John Doe
    Skills: Python, SQL, Machine Learning
    Experience: 3 years
    Education: B.Tech Computer Science

Usage:
    python resume_screening.py
"""

import os
import glob
import pandas as pd

# ---------- SETTINGS ----------
RESUME_FOLDER = "resumes"          # folder containing .txt resumes
SHORTLIST_THRESHOLD = 50           # % match score needed to shortlist
OUTPUT_FILE = "shortlisted_candidates.csv"

JOB_DESCRIPTION = """
We are looking for a Python Developer with experience in
SQL, Machine Learning, Data Analysis, Pandas, and Streamlit.
Minimum 2 years of experience required.
"""


def extract_field(text, field_name):
    """Pulls out the value after 'FieldName:' in the resume text."""
    for line in text.splitlines():
        if line.lower().startswith(field_name.lower() + ":"):
            return line.split(":", 1)[1].strip()
    return ""


def parse_resume(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    name = extract_field(text, "Name")
    skills = extract_field(text, "Skills")
    experience = extract_field(text, "Experience")
    education = extract_field(text, "Education")

    return {
        "File": os.path.basename(filepath),
        "Name": name,
        "Skills": skills,
        "Experience": experience,
        "Education": education,
        "RawText": text
    }


def get_job_keywords(job_description):
    # Simple keyword extraction: lowercase words, remove common stopwords
    stopwords = {"we", "are", "looking", "for", "a", "with", "in", "and", "of", "required", "minimum", "years"}
    words = job_description.lower().replace(",", " ").replace(".", " ").split()
    keywords = set(w for w in words if w not in stopwords and len(w) > 2)
    return keywords


def calculate_match_score(candidate, job_keywords):
    candidate_text = (candidate["Skills"] + " " + candidate["RawText"]).lower()
    candidate_words = set(candidate_text.replace(",", " ").split())

    matched = job_keywords.intersection(candidate_words)
    missing = job_keywords - candidate_words

    score = round((len(matched) / len(job_keywords)) * 100, 2) if job_keywords else 0
    return score, matched, missing


def main():
    resume_files = glob.glob(os.path.join(RESUME_FOLDER, "*.txt"))
    if not resume_files:
        print(f"No resume files found in '{RESUME_FOLDER}' folder.")
        return

    job_keywords = get_job_keywords(JOB_DESCRIPTION)

    results = []
    for filepath in resume_files:
        candidate = parse_resume(filepath)
        score, matched, missing = calculate_match_score(candidate, job_keywords)

        results.append({
            "Name": candidate["Name"] or candidate["File"],
            "Skills": candidate["Skills"],
            "Experience": candidate["Experience"],
            "Education": candidate["Education"],
            "MatchScore": score,
            "MatchedKeywords": ", ".join(sorted(matched)),
            "MissingSkills": ", ".join(sorted(missing))
        })

    df = pd.DataFrame(results)
    df = df.sort_values("MatchScore", ascending=False).reset_index(drop=True)
    df.insert(0, "Rank", df.index + 1)

    print("\n📋 Candidate Ranking:")
    print(df[["Rank", "Name", "MatchScore"]])

    shortlisted = df[df["MatchScore"] >= SHORTLIST_THRESHOLD]
    shortlisted.to_csv(OUTPUT_FILE, index=False)

    print(f"\n✅ Shortlisted {len(shortlisted)} candidates (score >= {SHORTLIST_THRESHOLD}%)")
    print(f"📁 Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()