# semantic-job-profile-matcher
 Match job descriptions to candidate profiles using semantic similarity (Sentence-BERT) not keywords.

# 🔍 Semantic Job ↔ Profile Matcher

> Match job descriptions to candidate profiles using **semantic similarity** (Sentence-BERT) — not keyword matching.

Perfect for recruiters, HR tech, or NLP portfolios. Built for laptops — no GPU needed.

![Demo](demo.gif) <!-- Optional: add later -->

---

## 🚀 Features

- ✅ Uses `all-MiniLM-L6-v2` for semantic understanding
- ✅ Compares against TF-IDF baseline (coming soon)
- ✅ Interactive Gradio UI
- ✅ Lightweight — runs on any laptop
- ✅ Easy to extend (add explainability, export, fine-tuning)

---

## ⚙️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/semantic-job-profile-matcher.git
cd semantic-job-profile-matcher
pip install -r requirements.txt
python app.py
```

Open `http://localhost:7860` in your browser.

---

## 📂 Structure

```
semantic-job-profile-matcher/
├── data/               # Sample jobs + profiles
├── notebooks/          # TF-IDF + Semantic notebooks (coming)
├── app.py              # Gradio UI
├── requirements.txt
└── README.md
```

---

## 📈 Next Steps

- [ ] Add TF-IDF baseline notebook
- [ ] Add evaluation metrics (Precision@K)
- [ ] Record demo GIF
- [ ] Deploy to Hugging Face Spaces

---

💡 **Why this matters**: Most “resume matchers” use keywords. This understands *meaning* — e.g., “led team” ≈ “managed engineers” even if words don’t match.