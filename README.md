# Tamil Nadu Government Schemes GraphRAG Chatbot

A Hybrid GraphRAG application that combines:

- Playwright Web Scraping
- FAISS Vector Database
- Neo4j Aura Knowledge Graph
- Hugging Face Embeddings (BGE)
- Azure OpenAI GPT-4.1 Mini
- LangChain
- Streamlit

The chatbot helps users discover and understand Tamil Nadu Government schemes through semantic search and graph-based relationship retrieval.

---

# Architecture

```text
                     Tamil Nadu Government Website
                                      |
                                      v
                           Playwright Scraper
                                      |
                                      v
                          Scheme Content Extraction
                                      |
                     +----------------+----------------+
                     |                                 |
                     v                                 v
               FAISS Vector DB                 Neo4j Aura Graph
             (Semantic Search)             (Relationship Search)
                     |                                 |
                     +----------------+----------------+
                                      |
                                      v
                              LangChain Pipeline
                                      |
                                      v
                           Azure OpenAI GPT-4.1 Mini
                                      |
                                      v
                              Streamlit Chat UI
```

---

# Features

✅ Government scheme extraction from TN Government website

✅ Semantic similarity search using FAISS

✅ Knowledge graph storage using Neo4j Aura

✅ Hugging Face Embeddings

✅ Natural language question answering

✅ Source-aware retrieval

✅ Fast and lightweight architecture

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Scraper | Playwright |
| LLM | Azure OpenAI GPT-4.1 Mini |
| Vector DB | FAISS |
| Knowledge Graph | Neo4j Aura |
| Embeddings | BAAI/bge-base-en-v1.5 |
| Framework | LangChain |

---

# Project Structure

```text
knowlege-graph/

├── app.py
├── ingest.py
├── scraper.py
├── neo4j_loader.py
├── requirements.txt
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
└── README.md
```

---

# Installation

## Step 1 - Create Virtual Environment

Mac/Linux

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```cmd
python -m venv venv

venv\Scripts\activate
```

---

## Step 2 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 - Install Playwright Browser

```bash
playwright install chromium
```

---

# Configuration

Update Azure OpenAI values inside code.

```python
AZURE_OPENAI_API_KEY = "YOUR_API_KEY"

AZURE_OPENAI_ENDPOINT = "YOUR_ENDPOINT"

AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
```

Update Neo4j Aura values.

```python
NEO4J_URI = "neo4j+s://xxxx.databases.neo4j.io"

NEO4J_USERNAME = "neo4j"

NEO4J_PASSWORD = "your-password"
```

---

# Neo4j Aura Setup

1. Create a free Neo4j Aura instance
2. Open Aura Console
3. Copy:

```text
URI
USERNAME
PASSWORD
```

4. Update values in project

---

# Data Ingestion

This step:

- Scrapes scheme information
- Generates embeddings
- Creates FAISS index
- Loads data into Neo4j Aura

Run:

```bash
python ingest.py
```

Expected Output:

```text
Scraping schemes...

Creating embeddings...

Creating FAISS index...

Loading Neo4j Aura...

Completed
```

---

# Verify Neo4j Data

Open Neo4j Query Console

Run:

```cypher
MATCH (s:Scheme)
RETURN s
LIMIT 10
```

You should see scheme nodes.

---

# Start Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# Example Questions

General

```text
What government schemes are available in Tamil Nadu?
```

Farmer

```text
What schemes are available for farmers?
```

Women

```text
What welfare schemes are available for women?
```

Students

```text
What educational assistance schemes are available?
```

Senior Citizen

```text
What schemes are available for senior citizens?
```

Recommendations

```text
I am a small farmer from Tamil Nadu. Suggest suitable government schemes.
```

```text
I am a woman entrepreneur. What schemes can I apply for?
```

```text
I am a college student. Which government schemes can support my education?
```

---

# Knowledge Graph Example

```text
Department
    |
  OFFERS
    |
  Scheme
   /   \
HAS     PROVIDES
 |         |
Eligibility Benefit
```

Example:

```text
Agriculture Department
            |
            v
 Farmer Welfare Scheme
      /            \
Eligibility      Benefit

Small Farmer     Subsidy
```

---

# FAISS Retrieval Flow

```text
User Question
      |
      v
Convert to Embedding
      |
      v
FAISS Similarity Search
      |
      v
Top Relevant Schemes
      |
      v
LLM Response Generation
```

---

# Troubleshooting

## Playwright Error

```text
BrowserType.launch
```

Run:

```bash
playwright install chromium
```

---

## Module Not Found

Install dependencies again

```bash
pip install -r requirements.txt
```

---

## FAISS Not Found

```bash
pip install faiss-cpu
```

---

## Neo4j Connection Error

Verify:

```text
NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD
```

---

## LangChain Import Error

Replace:

```python
from langchain.schema import Document
```

with

```python
from langchain_core.documents import Document
```

---

# Future Enhancements

- Scheme eligibility extraction
- Department relationship mapping
- GraphRAG retrieval
- Multi-language support
- Chat history memory
- Source citations
- BM25 + FAISS Hybrid Search
- Recommendation Engine
- Azure Content Safety Guardrails
- LangSmith Monitoring

---

# Buildathon Highlights

- Hybrid RAG Architecture
- Knowledge Graph Powered Search
- Real-Time Government Scheme Discovery
- Playwright Web Scraping
- Neo4j Aura Integration
- FAISS Semantic Retrieval
- GPT-4.1 Mini Powered Question Answering

---

# Author

Built as part of a GraphRAG-based Government Scheme Discovery Assistant leveraging FAISS, Neo4j Aura, LangChain, Hugging Face Embeddings, Streamlit, and Azure OpenAI.