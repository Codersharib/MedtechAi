from database.database import get_connection


def get_all_reports():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""

    SELECT *

    FROM reports

    ORDER BY upload_date DESC

    """)

    reports = cursor.fetchall()

    cursor.close()

    connection.close()

    return reports


def get_report_results(report_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(

        """

        SELECT *

        FROM medical_results

        WHERE report_id=%s

        """,

        (report_id,)

    )

    results = cursor.fetchall()

    cursor.close()

    connection.close()

    return results