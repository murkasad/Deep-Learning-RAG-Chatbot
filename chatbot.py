#getting replies

import time
import logging
from config import TOP_K, MAX_RETRIEVED_WORDS
from graphs import create_graphs
from vector_store import retrieve_chunks
from summarizer import summarize_text

logger = logging.getLogger(__name__)

def chat_answer(message, history, embedding_model, index, chunks, summarizer):

    try:
        context = " ".join(
            str(h["content"])
            for h in history[-3:]
            if h["role"] == "user"
        )

        # for h in history[-3:]  means loop through each message (h)
        # if h["role"] == "user" means keep only user messages (ignore assistant replies)
        # h["content"] will extract the actual text of the user question
        # then create a list of those questions and joins them

        full_query = context + " " + message

        t1 = time.time()
        retrieved_chunks = retrieve_chunks(
            full_query,
            embedding_model,
            index,
            chunks,
            TOP_K
        )
        t2 = time.time()

        answer = " ".join(retrieved_chunks)
        answer = " ".join(answer.split()[:MAX_RETRIEVED_WORDS])

        summary = summarize_text(answer, summarizer)
        t3 = time.time()

        retrieved_len = len(answer.split())
        summary_len = len(summary.split())

        #to fetch time it takes for evry step in the pipleine
        stage_times = {
            "Retrieve": t2 - t1,
            "Summarize": t3 - t2
        }

        chunk_lengths = [len(c.split()) for c in chunks] #create a list of word counts in each sentence

        g1, g2, g3 = create_graphs(
            chunk_lengths,
            retrieved_len,
            summary_len,
            stage_times
        )

        metrics = f"""
                        Retrieved words: {retrieved_len}
                        Summary words: {summary_len}
                        Compression ratio: {round(summary_len / max(retrieved_len,1), 3)}

                        Retrieval time: {round(stage_times['Retrieve'],3)}s
                        Summarization time: {round(stage_times['Summarize'],3)}s
                        """

        return summary, metrics, g1, g2, g3

    except Exception as e:
        logger.exception("Chatbot error")
        return "Error occurred. Please try again.", "", None, None, None #get the 5 things (summary, metrics, g1, g2, g3) from return statement or give None for properly handling error 