import re


class MedicalParser:

    def __init__(self):

        self.parameter_map = {

            "hb": "Hemoglobin",
            "hemoglobin": "Hemoglobin",
            "hgb": "Hemoglobin",

            "wbc": "WBC",
            "white blood cells": "WBC",
            "white blood cell count": "WBC",

            "rbc": "RBC",
            "red blood cells": "RBC",

            "platelets": "Platelets",
            "platelet count": "Platelets",

            "blood sugar": "Blood Sugar",
            "glucose": "Blood Sugar",

            "creatinine": "Creatinine"
        }

        self.reference_ranges = {

            "Hemoglobin": (13.0, 17.0),
            "WBC": (4000, 11000),
            "Platelets": (150000, 450000),
            "Blood Sugar": (70, 100),
            "Creatinine": (0.7, 1.3)
        }

    def standardize_parameter(self, parameter):

        parameter = parameter.strip().lower()

        return self.parameter_map.get(
    parameter,
    parameter.title()
)

    def normalize_value(self, value, line):

        line = line.lower()

        if "lakh" in line:
            return value * 100000

        if "million" in line:
            return value * 1000000

        return value

    def get_status(self, parameter, value):

        if parameter not in self.reference_ranges:
            return "Unknown"

        low, high = self.reference_ranges[parameter]

        if value < low:
            return "Low"

        if value > high:
            return "High"

        return "Normal"

    def parse_report(self, text):

        report_data = {}

        lines = text.splitlines()

        for line in lines:

            line = line.strip()

            if line == "":
                continue

            for key in self.parameter_map:

                if key.lower() in line.lower():

                    parameter_name = self.parameter_map[key]

                    number_match = re.search(
                        r"(\d+\.?\d*)",
                        line
                    )

                    # Skip lines that don't contain numbers
                    if number_match is None:
                        continue

                    value = float(
                        number_match.group(1)
                    )

                    normalized_value = self.normalize_value(
                        value,
                        line
                    )

                    unit = ""

                    parts = line.split(
                        number_match.group(1),
                        1
                    )

                    if len(parts) > 1:
                        unit = parts[1].strip()

                        report_data[parameter_name] = {

                            "value": normalized_value,

                            "unit": unit,

                            "status": self.get_status(
                                parameter_name,
                                normalized_value
                            ),

                            "raw_line": line

                        }

                        break

        return report_data