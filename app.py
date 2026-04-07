#setting up interface

import gradio as gr
from error_logger import setup_logger
from text_extraction import load_pdf_text
from langchain_text_splitter import clean_text, create_chunks
from vector_store import build_vectorstore
from summarizer import load_summarizer
from chatbot import chat_answer
from config import PDF_PATH

setup_logger() #handle errors if any and then log them

corpus = load_pdf_text(PDF_PATH)
cleaned = clean_text(corpus)
chunks = create_chunks(cleaned)

embedding_model, index = build_vectorstore(chunks)
summarizer = load_summarizer()

def respond(message, history):
    answer, metrics, g1, g2, g3 = chat_answer(
        message,
        history,
        embedding_model,
        index,
        chunks,
        summarizer
    )

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})

    return history, metrics, g1, g2, g3

with gr.Blocks() as demo:
    gr.Markdown("## Deep Learning Chat with Metrics & Graphs")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask a question")

    metrics_box = gr.Textbox(label="Metrics")
    g1 = gr.Image(label="Graph 1")
    g2 = gr.Image(label="Graph 2")
    g3 = gr.Image(label="Graph 3")

    msg.submit(respond, [msg, chatbot], [chatbot, metrics_box, g1, g2, g3])

    gr.Markdown("RAG Project by Murk Asad")

demo.launch()