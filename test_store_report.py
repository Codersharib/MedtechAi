from database.store_report_data import (
    store_report_data
)

sample_data = {

    "Hemoglobin": {

        "value": 12.4,

        "unit": "g/dL",

        "status": "Low"

    },

    "WBC": {

        "value": 7500,

        "unit": "/uL",

        "status": "Normal"

    },

    "Platelets": {

        "value": 250000,

        "unit": "/uL",

        "status": "Normal"

    }
}

report_id = store_report_data(

    "cbc_report.pdf",

    sample_data

)

print(
    f"Stored Report ID = {report_id}"
)