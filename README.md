<div align="center">

# 🚀 SkillGraph AI

### AI-Powered Career Intelligence Platform using Knowledge Graphs, RAG, and Large Language Models

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)]()
[![Neo4j](https://img.shields.io/badge/Neo4j-Knowledge_Graph-blue.svg)]()
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-orange.svg)]()
[![Gemini](https://img.shields.io/badge/Gemini-LLM-purple.svg)]()
[![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg)]()
[![License](https://img.shields.io/badge/License-MIT-success.svg)]()

**Transform resumes into personalized career roadmaps using Knowledge Graphs, Retrieval-Augmented Generation (RAG), and Generative AI.**

</div>

---

# 📌 Overview

SkillGraph AI is an intelligent career guidance platform that analyzes a candidate's resume, extracts technical skills using Large Language Models, compares them against a Neo4j-powered career knowledge graph, identifies missing competencies, and generates a personalized learning roadmap with curated learning resources, recommended projects, and AI-generated career advice.

Unlike traditional resume analyzers that rely solely on keyword matching, SkillGraph AI combines:

- 🧠 Knowledge Graphs (Neo4j)
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 Gemini LLM
- 🔎 Semantic Search (ChromaDB)
- 📈 Career Readiness Analytics
- 🌐 Interactive Learning Graphs

to create a personalized career intelligence system.

---

# ✨ Features

## 📄 Resume Analysis

- Upload PDF resumes
- Resume text extraction
- AI-powered skill extraction using Gemini
- Automatic skill normalization

---

## 🧠 Knowledge Graph

Neo4j stores relationships between:

- Skills
- Roles
- Learning prerequisites
- Career pathways

Example:

```
Python
   │
   ▼
NumPy
   │
   ▼
Machine Learning
   │
   ▼
Deep Learning
```

---

## 🎯 Career Twin

Creates a digital representation of the candidate by comparing:

Current Skills

VS

Required Skills

for any target role.

Supported roles include:

- AI Engineer
- Data Scientist
- Backend Engineer
- Frontend Engineer
- MLOps Engineer
- DevOps Engineer
- IoT Engineer

---

## 📊 Career Readiness Score

Calculates readiness percentage based on

```
Current Skills
──────────────
Required Skills
```

Example

```
AI Engineer

72%
```

---

## 🔮 Future Career Simulation

Predicts improvement after completing recommended learning paths.

Example

```
Current Readiness

42%

↓

Future Readiness

94%
```

---

## 🛣 Personalized Learning Paths

Automatically generates prerequisite-aware learning sequences.

Example

```
Programming Fundamentals

↓

Python

↓

NumPy

↓

Pandas

↓

Machine Learning

↓

Deep Learning

↓

Transformers

↓

RAG
```

---

## 🌐 Unified Roadmap Graph

Combines all missing skills into a single optimized roadmap.

Removes duplicate prerequisite chains automatically.

---

## 📚 Learning Resource Recommendation

Provides:

- Official Documentation
- Recommended Course
- Practical Project

Example

```
Docker

Docs:
https://docs.docker.com/

Course:
Docker for Beginners

Project:
Containerize a FastAPI Application
```

---

## 💻 Project Recommendation Engine

Suggests portfolio-quality projects based on missing skills.

Example

```
Multi-PDF RAG Chatbot

Skills

• RAG

• LangChain

• Embeddings

• Vector Databases
```

---

## 🏆 Multi-Role Ranking

Ranks multiple careers based on resume similarity.

Example

| Role | Match |
|------|--------|
| AI Engineer | 82% |
| Data Scientist | 76% |
| Backend Engineer | 58% |

---

## 🎯 Learning Milestones

Every roadmap node contains practical goals.

Example

```
Machine Learning

✓ Train Logistic Regression

✓ Train Random Forest

✓ Compare Evaluation Metrics
```

---

## 🤖 AI Career Coach

Uses Gemini to generate:

- Resume feedback
- Skill gap explanation
- Career roadmap
- Personalized learning advice

---

## 🌐 Interactive Roadmap

(Currently Backend Ready)

React Flow compatible graph format.

Nodes contain:

- Skill
- Status
- Milestones
- Learning Resources
- Suggested Projects

---

# 🏗 System Architecture

```
                    Resume PDF
                         │
                         ▼
              PDF Text Extraction
                         │
                         ▼
            Gemini Skill Extraction
                         │
                         ▼
                 Skill Normalization
                         │
                         ▼
              Neo4j Knowledge Graph
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
   Skill Gap      Learning Paths   Role Matching
          │              │              │
          └──────────────┼──────────────┘
                         ▼
              Unified Roadmap Generator
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Resources         Projects         Milestones
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                Gemini Career Coach
                         │
                         ▼
              Career Intelligence API
                         │
                         ▼
                React Dashboard (WIP)
```

---

# 📂 Project Structure

```
SkillGraph-AI/

backend/
│
├── app/
│   ├── api/
│   │      graph_api.py
│   │      resume_career.py
│   │      rag_api.py
│   │
│   ├── services/
│   │      resume_service.py
│   │      career_twin_service.py
│   │      role_service.py
│   │      learning_path_service.py
│   │      roadmap_service.py
│   │      graph_visualization_service.py
│   │      resource_service.py
│   │      project_service.py
│   │      milestone_service.py
│   │      future_simulator.py
│   │      career_simulator.py
│   │      multi_role_service.py
│   │      gemini_service.py
│   │      search_service.py
│   │
│   ├── graphrag/
│   │      neo4j_connection.py
│   │      ingest_graph.py
│   │
│   └── main.py
│
├── datasets/
│      career_roles.csv
│      resources.json
│      milestones.json
│      projects.json
│
├── vector_db/
│
├── frontend/
│
└── README.md
```

---

# 🔌 API Endpoints

## `POST /resume-career`

Main endpoint.

Performs complete career analysis.

Returns:

- Extracted Skills
- Missing Skills
- Career Readiness
- Future Simulation
- Multi-role Ranking
- Learning Paths
- Unified Roadmap
- Graph Data
- Milestones
- Resources
- Recommended Projects
- AI-generated Career Advice

---

## `POST /graph-roadmap`

Returns React Flow compatible roadmap graph.

---

## `POST /rag-search`

Semantic search using ChromaDB.

---

## `GET /`

Health check endpoint.

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python
- Neo4j
- ChromaDB
- Gemini API
- PyPDF
- NetworkX

## AI

- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Semantic Search
- Knowledge Graphs

## Frontend

- React
- Tailwind CSS
- React Flow
- Axios
- Recharts

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/<username>/SkillGraph-AI.git

cd SkillGraph-AI
```

## Install

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn backend.app.main:app --reload
```

Backend

```
localhost:8000
```

Swagger

```
localhost:8000/docs
```

## Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
localhost:5173
```

---

# 🎯 Current Status

### Backend

- ✅ Resume Analysis
- ✅ Knowledge Graph
- ✅ RAG Search
- ✅ Career Intelligence
- ✅ AI Career Coach
- ✅ Learning Roadmaps
- ✅ Project Recommendation
- ✅ Resources
- ✅ Career Simulation

### Frontend

- 🚧 React Dashboard (In Progress)
- 🚧 Interactive Graph
- 🚧 Analytics Dashboard

---

# 📈 Future Enhancements

- User Authentication
- Progress Tracking
- Daily Learning Planner
- Interview Preparation Module
- Resume Version Comparison
- Job Recommendation Engine
- ATS Resume Optimization
- AI Mock Interview
- Skill Trend Analytics

---

# 👨‍💻 Author

**Jayanth M**

Computer Science Undergraduate

Machine Learning | Knowledge Graphs | Generative AI | MLOps

GitHub:
https://github.com/JayanthM19

---

# ⭐ If you found this project interesting, consider giving it a star!
