# model/scorer.py
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    return round(score * 100, 2)  # Scale to 0–100

def generate_report(name, resume_text, job_description):
    score = compute_similarity(resume_text, job_description)
    return {
        "name": name,
        "score": score,
        "recommendation": "Shortlist" if score > 75 else "Review" if score > 50 else "Reject"
    }
