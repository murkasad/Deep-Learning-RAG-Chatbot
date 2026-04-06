# Deep-Learning-RAG-Chatbot
A Deep Learning Chat System with Retrieval-Augmented Generation and Performance Metrics


This Project presents a Retrieval-Augmented Generation (RAG)-based conversational system designed to answer deep learning-related queries using a structured knowledge source. The system utilizes the textbook Deep Learning by Ian Goodfellow et al. as its primary corpus. The document is processed, chunked, and embedded into a vector space using sentence transformers, enabling semantic retrieval through FAISS indexing. Retrieved content is then summarized using a transformer-based Large Language Model (LLM) to generate concise responses. The system also integrates runtime performance metrics and visualization, including execution time, chunk distribution, and compression ratio. A Gradio-based interface enables interactive querying while exposing internal system behavior.
