import asyncio
import os

from scraper import scrape
from neo4j_loader import insert_scheme

from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

schemes = asyncio.run(
    scrape()
)

docs = []

for scheme in schemes:

    docs.append(
        Document(
            page_content=
            f"""
            Scheme:
            {scheme['name']}

            URL:
            {scheme['url']}
            """
        )
    )

    insert_scheme(
        scheme
    )

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

db = FAISS.from_documents(
    docs,
    embeddings
)

db.save_local(
    "faiss_index"
)

print("Completed")