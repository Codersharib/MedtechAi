import fitz
import pytesseract 
from PIL import Image
class OCRReader:
    def extract_text(self, pdf_path):
        document = fitz.open(pdf_path)
        final_text = ""
        for page_number in range(len(document)):
            page = document.load_page(page_number)
            pix = page.get_pixmap(dpi=300)
            image = Image.frombytes( "RGB", [pix.width, pix.height], pix.samples )
            page_text = pytesseract.image_to_string(image)
            final_text += page_text + "\n"
        document.close()
        return final_text.strip()