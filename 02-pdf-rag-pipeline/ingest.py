
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DOCUMENTS_DIR = Path("documents")
DB_DIR = "chroma_db"


def load_documents():
    documents = []

    for path in DOCUMENTS_DIR.iterdir():
        if path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(path))
        elif path.suffix.lower() == ".txt":
            loader = TextLoader(str(path), encoding="utf-8")
        else:
            continue

        pages = loader.load()

        for page in pages:
            page.metadata["source"] = path.name

        documents.extend(pages)

    if not documents:
        raise ValueError("No PDF or TXT documents found!")

    return documents


def main():
    documents = load_documents()

    print(f"Loaded {len(documents)} pages/documents.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} text chunks.")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        collection_name="pdf_knowledge_base",
        persist_directory=DB_DIR,
        embedding_function=embeddings,
    )

    # Replace existing records for these chunk IDs on reruns.
    import hashlib

    ids = []
    for chunk in chunks:
        identity = (
            f"{chunk.metadata['source']}|"
            f"{chunk.metadata.get('page', -1)}|"
            f"{chunk.page_content}"
        )
        ids.append(hashlib.sha256(identity.encode()).hexdigest())

    vector_store.add_documents(documents=chunks, ids=ids)

    print("Ingestion complete!")
    print(f"Stored {len(chunks)} chunks in {DB_DIR}.")


if __name__ == "__main__":
    main()
