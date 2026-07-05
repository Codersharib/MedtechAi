from database.save_report import save_report
from database.save_results import save_result


def store_report_data(
    filename,
    parsed_data):

        report_id = save_report(
            filename
        )

        for parameter, data in parsed_data.items():

            save_result(

                report_id,

                parameter,

                data["value"],

                data["unit"],

                data["status"]

            )

        return report_id