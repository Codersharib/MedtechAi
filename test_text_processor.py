from modules.text_processor import TextProcessor


sample_text = """

Hemoglobin : 12.4 g/dL

Platelets : 2.5 lakh/uL

Blood Sugar : 96 mg/dL

Creatinine : 1.1 mg/dL

WBC : 7500 /uL

RBC : 4.7 million/uL

"""

processor = TextProcessor(
    chunk_size=50,
    overlap=10
)

chunks = processor.create_chunks(
    sample_text
)

for chunk in chunks:

    print("=" * 40)

    print(chunk["chunk_id"])

    print(chunk["text"])

    print(chunk["start_char"])

    print(chunk["end_char"])
