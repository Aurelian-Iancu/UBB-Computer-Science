import mysql.connector


def delete_shelters():
    conn = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                database="animalshelter",
                user="debian-sys-maint",
                password="1ZKDyeEnwjHkFTIH"
            )

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM shelter;")
            conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()