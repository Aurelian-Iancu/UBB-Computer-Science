import random

import mysql.connector
from faker import Faker


def insert_data_volunteer_ings():
    conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="animalshelters",
                user="root",
                password="Aurelian2002"
            )

    SPECIAL_CHARS = [".", " ", ",", "'"]
    TLDS = [".com", ".net", ".ro"]
    EMAIL_DOMAINS = ["@gmail.com", "@yahoo.com"]
    ROLES = ["Marketing & Public Relations", "Volunteer Management", "Customer Experience", "Animal Care & Medical",
             "Retail", "Events & Fundraising", "Accounting & Database Management", "Operations & Administration"]

    try:
        with open("./queries/insert_volunteer_ings.py", "w", encoding="utf-8") as f:
            fake = Faker()
            with conn.cursor() as cursor:
                cursor.execute("SELECT shelter_id from shelter")
                shelters_id = [el[0] for el in cursor.fetchall()]
                cursor.execute("SELECT volunteer_id from volunteer")
                volunteers_id = [el[0] for el in cursor.fetchall()]
                pairs = set()

                insert_query = "INSERT INTO volunteers_in (shelter_id, volunteer_id, hours_per_week, role) VALUES "
                values = []
                for i in range(10000000):
                    shelter_id = random.choice(shelters_id)
                    volunteer_id = random.choice(volunteers_id)
                    while(shelter_id, volunteer_id) in pairs:
                        shelter_id = random.choice(shelters_id)
                        volunteer_id = random.choice(volunteers_id)
                    pairs.add((shelter_id, volunteer_id))
                    hours_per_week = random.randint(0, 168)
                    role = random.choice(ROLES)
                    values.append(f"({shelter_id}, {volunteer_id}, '{hours_per_week}', '{role}')")
                    if len(values) == 1000:
                        f.write(insert_query + ", ".join(values) + ";\n")
                        cursor.execute(insert_query + ", ".join(values))
                        values = []
                conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()