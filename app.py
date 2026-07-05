import os

from flask import Flask
from flask import render_template
from flask import request

from modules.pdf_reader import PDFReader
from modules.ocr import OCRReader
from modules.parser import MedicalParser

from database.store_report_data import (
    store_report_data
)
from database.history import (
    get_all_reports,
    get_report_results
)

from modules.chat_engine import ChatEngine
from modules.ai_indexer import AIIndexer

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
"index.html"
)


@app.route("/upload", methods=["POST"])
def upload():

    if "report" not in request.files:
        return "No File Selected"

    file = request.files["report"]

    if file.filename == "":
        return "Empty File"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Read PDF
    reader = PDFReader()
    document = reader.extract_document(filepath)

    # OCR only for scanned PDFs
    if document["is_scanned"]:

        print("Scanned PDF Detected")

        ocr = OCRReader()

        document["text"] = ocr.extract_text(
            filepath
        )

    # -------------------------
    # Parser (runs for BOTH scanned and normal PDFs)
    # -------------------------

    parser = MedicalParser()

    parsed_data = parser.parse_report(
        document["text"]
    )

    print(parsed_data)

    # -------------------------
    # Save in MySQL
    # -------------------------

    report_id = store_report_data(
        file.filename,
        parsed_data
    )

    print(f"Report ID : {report_id}")

    # -------------------------
    # Build AI Index
    # -------------------------

    # Uncomment these only if AIIndexer is imported and working
    #
    indexer = AIIndexer()
    indexer.create_index(
            report_id,
            document["text"]
        )

        # -------------------------
        # Return Dashboard
        # -------------------------

    return render_template(
"dashboard.html",
document=document,
report_id=report_id,
parsed_data=parsed_data
)
    
chat = ChatEngine()


@app.route("/chat/<int:report_id>")
def chat_page(report_id):

    return render_template(

"chat.html",

report_id=report_id

)


@app.route("/ask", methods=["POST"])
def ask():

    report_id = int(

        request.form["report_id"]

    )

    question = request.form["question"]

    answer = chat.ask(

        report_id,

        question

    )

    return {

"answer": answer

}

@app.route("/history")
def history():

    reports = get_all_reports()

    return render_template("history.html",reports=reports)


@app.route("/report/<int:report_id>")
def report(report_id):

    results = get_report_results(
        report_id
    )

    return render_template("report.html",results=results,report_id=report_id)

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )