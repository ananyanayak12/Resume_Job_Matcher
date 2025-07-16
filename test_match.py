from extract_resume import extract_text_from_pdf
from matcher import match_resume_to_jobs

resume_text = extract_text_from_pdf("sample_resume.pdf")
results = match_resume_to_jobs(resume_text)

for r in results:
    print(f"{r['title']} → Match Score: {r['score']}%")
