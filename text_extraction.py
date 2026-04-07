#extracting from the pdf book
import pdfplumber
import logging

logger = logging.getLogger(__name__)

def load_pdf_text(pdf_path: str) -> str:
    try:
        corpus = ""

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):  #books usually start at later pages, page1 is only the book title
                text = page.extract_text()

                if text:
                    corpus += text + " "
                else:
                    logger.warning(f"No text found on page {page_num}")

        if not corpus.strip():
            raise ValueError("Empty PDF content")

        logger.info("PDF loaded successfully")
        return corpus

    except FileNotFoundError:
        logger.error("PDF file not found")
        raise

    except Exception as e:
        logger.exception(f"Error loading PDF: {e}")
        raise