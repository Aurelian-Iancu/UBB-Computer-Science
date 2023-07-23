#from databaseScripts.constants import HOST, PORT, DATABASE, USER, PASSWORD, SPECIAL_CHARS, TLDS, EMAIL_DOMAINS
import mysql.connector


def delete_volunteer_ins():
    conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="animalshelters",
                user="root",
                password="Aurelian2002"
            )

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM volunteers_in;")
            conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()