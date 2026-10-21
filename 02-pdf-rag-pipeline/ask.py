
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import ChatPromptTemplate

DB_DIR = "chroma_db"


def main():
    # Load the same embedding model used during ingestion.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Connect to the existing ChromaDB database.
    vector_store = Chroma(
        collection_name="pdf_knowledge_base",
        persist_directory=DB_DIR,
        embedding_function=embeddings,
    )

    # Configure the language model.
  

    
    llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
)


    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a document question-answering assistant.

Answer using ONLY the supplied context.
If the answer is not supported by the context, say:
"I couldn't find sufficient information in the provided documents."

Do not invent facts or source citations.
Cite every factual answer using the source filename and page
when available. TXT documents may not have page numbers.

Context:
{context}"""
        ),
        ("human", "{question}"),
    ])

    print("PDF RAG Assistant started!")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nAsk a question: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        # Retrieve the four most relevant chunks.
        results = vector_store.similarity_search_with_score(question, k=4)

       # Reject results that are not sufficiently relevant
        DISTANCE_THRESHOLD = 1.0

        relevant_results = [
            (doc, score)
             for doc, score in results
             if score <= DISTANCE_THRESHOLD
       ]

        if not relevant_results:
              print("\nAnswer:")
              print("I couldn't find sufficient information in the provided documents.")
              continue
        print("\nRelevant document text:")
        for doc, score in results:
                  print(doc.page_content)

        if not results:
            print("No relevant document passages found.")
            continue

        # Display retrieved sources for transparency.
        context_parts = []

        print("\nRetrieved sources:")

        for doc, distance in results:
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page")

            if page is not None:
                source_label = f"{source}, page {page + 1}"
            else:
                source_label = source

            print(f"- {source_label} (distance: {distance:.4f})")

            context_parts.append(
                f"[Source: {source_label}]\n{doc.page_content}"
            )

        context = "\n\n".join(context_parts)

        # Generate an answer grounded in the retrieved text.
        chain = prompt | llm

        

       

        
        try:
            print("\nSending question to Gemini...")

            response = chain.invoke({
                 "context": context,
                 "question": question,
            })

            print("\nGemini response received.")
            print("\nAnswer:")
            content = response.content

            if isinstance(content, list):
                 answer = "\n".join(
                      item["text"]
                      for item in content
                      if isinstance(item, dict) and item.get("type") == "text"
    )
            else:
                answer = content

            print(answer)

        
        except Exception as error:
            error_message = str(error)

            if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:
                print("\nGemini API quota exceeded.")
                print("Your document retrieval is still working.")
                print("Wait for the quota to reset, then try again.")
            else:
                print(f"\nAnswer generation failed: {error}")



if __name__ == "__main__":
    main()
