# PDF Question Answering Using Retrieval-Augmented Generation (RAG)

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to ask questions about the contents of PDF documents.

The application retrieves relevant text from a PDF and uses the retrieved information as context for a language model to generate an answer.

It combines document processing, text embeddings, similarity search, and Generative AI to support document-based question answering.

## Features
- Load and process PDF documents.
- Split document text into smaller chunks.
- Convert text chunks into vector embeddings.
- Retrieve relevant document chunks for a user's question.
- Generate answers using the retrieved context and Google Gemini.
- Display retrieved source information, including document names and page numbers where supported.
- Handle API quota errors and answer-generation failures.

## Technologies Used
- Python
- Retrieval-Augmented Generation (RAG)
- Google Gemini API
- Text embeddings
- Vector similarity search
- PDF processing
- LangChain, if used in the implementation

## Project Structure

```text
02-pdf-rag-pipeline/
├── main.py
├── requirements.txt
├── README.md
└── company_policy.pdf
```

*Note: Replace `main.py` with your actual script filename if different. Include any additional modules or vector database files your implementation requires.*

## Prerequisites
- Python version compatible with your installed dependencies.
- pip package manager.
- A Google Gemini API key.
- Internet access for API-based embedding or answer generation, if required by your implementation.

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure your Gemini API key using an environment variable or a local `.env` file, depending on your implementation.

   Never upload API keys or files containing secrets to GitHub.

## Run the Project

Run the main Python script. For example:

```bash
python main.py
```

Follow the prompt to enter a question about the configured PDF document.

## Example

**Question:**
How many public holidays are provided annually?

**Pipeline workflow:**

1. The application reads the PDF.
2. The document text is divided into chunks.
3. Embeddings represent the chunks in vector space.
4. The system retrieves the most relevant chunks for the question.
5. The retrieved text is passed to Gemini as context.
6. Gemini generates an answer based on the supplied context, subject to the model's availability and quota.

The answer depends on the actual contents of the PDF.

## Error Handling
If the Gemini API quota is exceeded, the application reports the quota limitation. Document retrieval can still work independently, but final answer generation may fail until API access is available again.

## Learning Outcomes
- Understanding the RAG architecture.
- Processing and chunking PDF documents.
- Using embeddings and similarity search.
- Connecting document retrieval with a Generative AI model.
- Understanding source-grounded question answering.
- Handling API errors and quota limitations.

## Author
Aswathy K.

## Internship
Datheon Python, Generative AI & LangChain Internship