from modules.parser import MedicalParser

sample_report = """
Hemoglobin : 12.4 g/dL
WBC : 7500 /uL
Platelets : 2.5 lakh/uL
Blood Sugar : 96 mg/dL
Creatinine : 1.1 mg/dL
"""

parser = MedicalParser()

result = parser.parse_report(
    sample_report
)

print(result)