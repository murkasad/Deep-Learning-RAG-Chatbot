#transforming sentence chunks from langchain into vectors usin faiss

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

def load_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)  #all-MiniLM-L6-v2 from config file, we can change it 

def build_vectorstore(chunks):
    if not chunks:
        raise ValueError("Chunks list is empty.")

    model = load_embedding_model()
    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]  #384size vector

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    return model, index

def retrieve_chunks(query, model, index, chunks, k):  #k is number of chunks we want to extract, the more k, better the answer but slower the process
    if index is None:
        raise ValueError("FAISS index has not been built.")

    query_embedding = model.encode([query])
    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    return [chunks[i] for i in indices[0]] #since we have only 1 query, get 0th item from list of indices [[chunk1, chunk2]]