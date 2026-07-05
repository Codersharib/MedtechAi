from modules.text_processor import TextProcessor
from modules.retriever import Retriever

sample_text = """

Hemoglobin : 12.4 g/dL

Platelets : 250000 /uL

Blood Sugar : 96 mg/dL

Creatinine : 1.1 mg/dL

WBC : 7500 /uL

"""

processor = TextProcessor()

chunks = processor.create_chunks(
    sample_text
)

retriever = Retriever()

retriever.build_report_index(

    report_id=1,

    chunks=chunks

)

results = retriever.retrieve(

    report_id=1,

    question="What is the hemoglobin level?"

)

print()

print("Retrieved Chunks")

print()

for chunk in results:

    print(chunk)

    print("-" * 50)
