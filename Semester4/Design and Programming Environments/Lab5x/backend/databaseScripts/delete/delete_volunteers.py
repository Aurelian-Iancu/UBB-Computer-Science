#from databaseScripts.constants import HOST, PORT, DATABASE, USER, PASSWORD, SPECIAL_CHARS, TLDS, EMAIL_DOMAINS
import mysql.connector


def delete_volunteers():
    conn = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                database="animalshelter",
                user="debian-sys-maint",
                password="1ZKDyeEnwjHkFTIH"
            )

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM volunteer;")
            conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()