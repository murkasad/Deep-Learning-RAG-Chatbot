#splitting text to chunks from the extracted pdf file, and overlapping chunks to keep some previous context

import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP  #getting values from configuration file

def clean_text(corpus: str) -> str:
    corpus = re.sub(r'\s+', ' ', corpus)
    corpus = re.sub(r'([a-z])([A-Z])', r'\1 \2', corpus)
    return corpus.lower()

def create_chunks(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP 
    )
    return splitter.split_text(text)