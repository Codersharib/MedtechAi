from database.database import get_connection


def save_result(
    report_id,
    parameter,
    value,
    unit,
    status):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO medical_results
        (
            report_id,
            parameter,
            value,
            unit,
            status
        )
        VALUES
        (%s,%s,%s,%s,%s)
        """

        cursor.execute(

            query,

            (
                report_id,
                parameter,
                value,
                unit,
                status
            )
        )

        connection.commit()

        cursor.close()

        connection.close()