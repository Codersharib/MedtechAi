from modules.ai_indexer import AIIndexer

text = """

Hemoglobin : 12.4 g/dL

Platelets : 250000 /uL

Blood Sugar : 96 mg/dL

Creatinine : 1.1 mg/dL

WBC : 7500 /uL

RBC : 4.6 million/uL

"""

indexer = AIIndexer()

indexer.create_index(

    report_id=1,

    text=text

)

results = indexer.search(

    report_id=1,

    question="What is the hemoglobin level?"

)

print()

print("Retrieved Chunks")

print()

for result in results:

    print(result)

    print("-" * 60)