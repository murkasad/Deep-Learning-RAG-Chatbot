# Text Retrieval and Summarizer ChatBot Framework 

### RAG (Retrieval-Augmented Generation) System

**Project Summary**:

This project is a text retrieval and summarization system that allows users to input a question and receive a concise summary based on relevant content.

It works by first converting the user’s input into numerical embeddings using a sentence transformer model. These embeddings are then compared against a pre-built vector index (FAISS) to identify the most relevant text chunks from your dataset. The retrieved content is combined and passed to a transformer-based summarization model BART, which generates a concise summary as the final output.

The entire pipeline is integrated into an interactive user interface built using Gradio, allowing users to easily input queries and view summarized results in real time.

Steps:
1. Retrieves relevant text from a User's Document (FAISS)
2. Converts Corpus to Sentences (Sentence Transformer)
3. Generates a Summarized output (HuggingFace Text Summarizer)

**Use of SBERT**:

Sentence Transformers(SBERT), uses pretrained "Embedding" models, all we do is provide them our chunks from previous step and it creates vectors. (huggingface)
Embeddings are dense, lower-dimensional, numerical vector representations of data such as text, images, or audio that capture semantic meaning and relationships.(soucre: google)

Steps:
1. Load an embedding model
2. Feed text chunks into the model
3. Convert each chunk into a vector of numbers

Transformer Model (all-MiniLM-L6-v2):
This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.(huggingface)

**Use of FAISS**:

FAISS as a super-fast “vector search engine”, stands for Facebook AI Similarity Search. 
It is an open-source library developed by Meta's Fundamental AI Research group (formerly Facebook AI Research) designed for the efficient similarity search and clustering of dense vectors. (google)

Takes chunks of text from the document
As each chunk is previously converted to a 384-dimensional embedding by MiniLM
This store all embeddings in FAISS
so when a user asks a question, the question is converted to a vector and FAISS finds the nearest embeddings (most similar chunks of text from the document)
Then we pass those chunks to your LLM to generate the answer


**Final Pipeline**: 
Take PDF -> Get chunks -> Make embeddings -> Ask Question -> Retrieve Answer -> Summarize Result and Display Metrics

*--by Murk Asad*