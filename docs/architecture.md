# System Architecture

## 1) End-to-end flow
1. Candidate uploads resume (`PDF/DOCX`) or submits raw text.
2. Backend extracts and cleans text.
3. Sentence-BERT (`all-MiniLM-L6-v2`) generates normalized embeddings.
4. Job description is embedded similarly.
5. Cosine similarity produces semantic match score.
6. Skill extractor finds skill coverage and missing skills.
7. Recommendation engine creates improvements, interview questions, and roadmap.
8. API returns structured JSON for UI/recruiter dashboard consumption.

## 2) Backend module responsibilities
- `app/api`: HTTP routers and contract boundaries.
- `app/services/text_extraction.py`: PDF/DOCX parsers + cleaning.
- `app/services/embeddings.py`: model lifecycle and vector generation.
- `app/services/vector_store.py`: FAISS indexing abstraction.
- `app/services/skills.py`: skill extraction and gap logic.
- `app/services/matcher.py`: orchestration of scoring + outputs.
- `app/services/recommendations.py`: recommendation and fairness notes.
- `app/db` + `app/models`: persistence and relational entities.

## 3) Bias reduction strategy
- Exclude sensitive features (name, gender, age, college tier) from model scoring.
- Score only semantic fit + demonstrable skill evidence.
- Keep fairness notes in payload for transparency.
- Future: demographic parity monitoring on recruiter dashboard.

## 4) Scale path to microservices
- Split into services when traffic grows:
  - `ingestion-service` (file parsing)
  - `embedding-service` (GPU workers)
  - `matching-service` (scoring + ranking)
  - `recommendation-service` (LLM-assisted suggestions)
- Add queue (Kafka/RabbitMQ) between ingestion and embedding.
- Move FAISS to dedicated vector store (Chroma/Pinecone/pgvector).
- Add Redis caching for repeated JD embeddings.
