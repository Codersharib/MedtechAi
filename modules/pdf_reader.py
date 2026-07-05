import fitz
class PDFReader:
    def extract_document(self, pdf_path):
        document = fitz.open(pdf_path)
        extracted_text = ""
        for page in document:
            extracted_text += page.get_text()
            metadata = document.metadata
            document_info = { "filename": pdf_path.split("/")[-1], "total_pages": len(document), "text": extracted_text.strip(), "metadata": metadata, "is_scanned": False }
            if len(document_info["text"]) < 50:
                document_info["is_scanned"] = True
            document.close()
            return document_info