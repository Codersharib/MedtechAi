from database.database import get_connection


def save_report(filename):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO reports (filename)
    VALUES (%s)
    """

    cursor.execute(
        query,
        (filename,)
    )

    connection.commit()

    report_id = cursor.lastrowid

    cursor.close()

    connection.close()

    return report_id