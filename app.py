import os
import streamlit as st

from neo4j import GraphDatabase

from langchain_openai import AzureChatOpenAI

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

st.set_page_config(
    page_title="TN Scheme Assistant"
)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD")
    )
)

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    ),
    api_key=os.getenv(
        "AZURE_OPENAI_API_KEY"
    ),
    azure_deployment=os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    ),
    api_version="2024-02-01"
)

st.title(
    "Tamil Nadu Scheme Assistant"
)

question = st.chat_input(
    "Ask your question"
)

if question:

    with st.chat_message("user"):
        st.write(question)

    docs = db.similarity_search(
        question,
        k=5
    )

    vector_context = "\n".join(
        [
            d.page_content
            for d in docs
        ]
    )

    with driver.session() as session:

        result = session.run(
            """
            MATCH (s:Scheme)
            RETURN s.name AS name
            LIMIT 20
            """
        )

        graph_context = "\n".join(
            [
                row["name"]
                for row in result
            ]
        )

    prompt = f"""
You are Tamil Nadu Scheme Assistant.

Vector Context:
{vector_context}

Graph Context:
{graph_context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    with st.chat_message(
        "assistant"
    ):
        st.write(
            response.content
        )