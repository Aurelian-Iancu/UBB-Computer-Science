import random

import faker
import mysql.connector
from faker import Faker


def insert_data_animals():
    conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="animalshelters",
                user="root",
                password="Aurelian2002"
            )



    ANIMALS = ["Dog", "Cat", "Rabbit", "Hamster", "Guinea pig", "Bird", "Snake", "Turtle", "Lizard"]
    BREEDS = [
        "Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Beagle", "Poodle", "Rottweiler", "Boxer", "Siberian Husky", "Dachshund",
        "Siamese", "Persian", "Maine Coon", "Sphynx", "Bengal", "Scottish Fold", "Ragdoll", "Birman", "British Shorthair", "American Shorthair",
        "Lionhead", "Dutch", "Mini Lop", "Netherland Dwarf", "Flemish Giant", "Himalayan", "Californian", "Angora", "Polish", "Hotot",
        "Syrian", "Dwarf Campbell Russian", "Dwarf Winter White Russian", "Roborovski", "Chinese", "Mongolian Gerbil", "Teddy Bear", "Winter White Russian", "Campbell Russian", "Djungarian",
        "Abyssinian", "Peruvian", "Texel", "Silkie", "American", "Teddy", "Merino", "Baldwin", "Coronet", "Alpaca",
        "Parakeet", "Cockatiel", "Budgerigar", "African Grey Parrot", "Caique", "Conure", "Lovebird", "Eclectus", "Cockatoo", "Macaw",
        "Ball Python", "Corn Snake", "King Snake", "Milk Snake", "Boa Constrictor", "Rat Snake", "Garter Snake", "Green Tree Python", "Anaconda", "Copperhead",
        "Red-Eared Slider", "Painted Turtle", "Russian Tortoise", "Map Turtle", "Musk Turtle", "Box Turtle", "Diamondback Terrapin", "Snapping Turtle", "Softshell Turtle", "Sulcata Tortoise",
        "Bearded Dragon", "Gecko", "Iguana", "Chameleon", "Skink", "Monitor", "Anole", "Uromastyx", "Horned Lizard", "Frilled Lizard"
    ]

    try:
        with open("./queries/insert_animals.py", "w", encoding="utf-8") as f:
            fake = Faker("ro_Ro")
            with conn.cursor() as cursor:
                cursor.execute("SELECT shelter_id from shelter")
                shelter_ids = [el[0] for el in cursor.fetchall()]

                insert_query = "INSERT INTO animal (name, type, weight, breed, date_of_birth, shelter_animal_fk) VALUES "
                values = []
                for i in range(1000000):
                    name = fake.name()
                    type = random.choice(ANIMALS)
                    weight = round(random.uniform(10, 100), 2)
                    breed = random.choice(BREEDS)
                    year = random.randint(2008, 2023)
                    month = random.randint(1, 12)
                    day = random.randint(1, 28)
                    date_of_birth = f"{year}-{'{:02d}'.format(month)}-{'{:02d}'.format(day)}"

                    shelter_animal_fk = random.choice(shelter_ids)


                    values.append(
                        f"('{name}', '{type}', {weight}, '{breed}', '{date_of_birth}', {shelter_animal_fk})")

                    if len(values) == 1000:
                        #f.write(insert_query + ", ".join(values) + ";\n")
                        cursor.execute(insert_query + ", ".join(values))
                        values = []
                conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn:
            cursor.close()
            conn.close()