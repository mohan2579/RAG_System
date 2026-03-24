from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

# 1. Load existing vector store (IMPORTANT: not from_documents)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# 2. Take user query
query = input("Ask your question: ")

# 3. Retrieve relevant chunks
retrieved_docs = vector_store.similarity_search(query, k=2)
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

# 4. Create LLM
llm = ChatOllama(model="phi3")

# 5. Strict prompt
prompt = ChatPromptTemplate.from_template(
    """
    You are a strict assistant.

    Use ONLY the information provided in the CONTEXT below.
    Do NOT add explanations, analogies, or examples that are not explicitly written in the context.
    If the answer is not present in the context, respond exactly with:
    I don't know.

    CONTEXT:
    --------------------
    {context}
    --------------------

    QUESTION:
    {question}

    FINAL ANSWER:
    """
)

final_prompt = prompt.format(context=context, question=query)
response = llm.invoke(final_prompt)

print("\nAnswer:\n")
print(response.content)