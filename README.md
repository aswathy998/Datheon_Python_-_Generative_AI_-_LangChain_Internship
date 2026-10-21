# Datheon Python, Generative AI & LangChain Internship Projects

This repository contains two hands-on Python and Generative AI projects developed as part of my learning journey.

## Projects

### 1. AI Document Parser

**Folder:** `01-ai-document-parser/`

A Python application that extracts structured invoice information, validates the extracted fields, and saves the results as JSON.

**Key features**
- Invoice data extraction and validation
- PDF reading
- Structured JSON output
- Automated tests
- Python-based document processing

### 2. PDF RAG Pipeline

**Folder:** `02-pdf-rag-pipeline/`

A Retrieval-Augmented Generation (RAG) application that retrieves relevant information from PDF documents and uses a Google Gemini model to generate answers based on the retrieved context.

**Key features**
- PDF ingestion and text splitting
- Hugging Face sentence embeddings
- Chroma vector database
- Similarity-based document retrieval
- Gemini-powered answer generation
- Environment-based configuration for API credentials

## Technologies

- Python
- LangChain
- Google Gemini
- Hugging Face
- ChromaDB
- PyPDF
- pytest

## Getting Started

1. Open the project folder you want to explore.
2. Follow its `README.md` for project-specific setup instructions.
3. Install dependencies using its `requirements.txt`.
4. Configure required API credentials in a local `.env` file when needed. Never commit API keys or secrets to GitHub.

## Repository Structure

```text
.
├── 01-ai-document-parser/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── requirements.txt
│   └── README.md
├── 02-pdf-rag-pipeline/
│   ├── ask.py
│   ├── ingest.py
│   ├── requirements.txt
│   ├── documents/
│   └── README.md
├── .gitignore
└── README.md
```

## Learning Objectives

These projects demonstrate practical experience with Python development, document processing, automated testing, vector search, and foundational Generative AI and RAG concepts.