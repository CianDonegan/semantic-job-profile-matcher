import gradio as gr
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load data
jobs_df = pd.read_csv("data/jobs.csv")
profiles_df = profiles_df = pd.read_csv("data/profiles.csv", delimiter="\t", encoding="latin1")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute profile embeddings (for speed)
profile_embeddings = model.encode(profiles_df['summary'].tolist(), convert_to_tensor=True)

def match_job_to_profiles(job_description, top_k=5):
    # Encode job description
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    
    # Compute cosine similarity
    cos_scores = util.cos_sim(job_embedding, profile_embeddings)[0].cpu().numpy()
    top_indices = np.argsort(-cos_scores)[:top_k]  # Sort and get top K indices
    
    # Build results
    results = []
    for idx in top_indices:
        score = cos_scores[idx]
        profile = profiles_df.iloc[idx]
        results.append({
            "Name": profile['name'],
            "Summary": profile['summary'],
            "Similarity Score": f"{score:.3f}"
        })
    
    # Return as DataFrame for Gradio
    return pd.DataFrame(results)

# Gradio Interface
with gr.Blocks(title="Semantic Job ↔ Profile Matcher") as demo:
    gr.Markdown("# 🔍 Semantic Job ↔ Profile Matcher")
    gr.Markdown("Enter a job description — get semantically matched candidate profiles (no keyword matching!)")
    
    job_input = gr.Textbox(label="Job Description", placeholder="e.g., Looking for a senior Java engineer with Spring Boot...")
    top_k_slider = gr.Slider(minimum=1, maximum=8, value=5, step=1, label="Number of Matches")
    output_table = gr.Dataframe(label="Top Matches")
    
    btn = gr.Button("Find Matches")
    btn.click(fn=match_job_to_profiles, inputs=[job_input, top_k_slider], outputs=output_table)

    gr.Markdown("💡 Built with Sentence-BERT + Gradio | No keyword matching — understands meaning!")

demo.launch()