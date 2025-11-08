import psycopg2

conn = psycopg2.connect(database='netology_db', user='postgres', password='2146')
with conn.cursor() as cur:
    def create_db(cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS person(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(80) NOT NULL
            );
            ''')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phone_number(
            id SERIAL PRIMARY KEY,
            number VARCHAR(20),
            person_id INT NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id)
            );
            """)
        conn.commit()

    def add_person (cursor, first_name, last_name, email):
        cursor.execute("""
            INSERT INTO person(first_name, last_name, email) VALUES(%s, %s, %s);
            """, (first_name, last_name, email))
        conn.commit()

    def add_phone_number (cursor, person_id, number=None):
        cursor.execute("""
            INSERT INTO phone_number(number, person_id) VALUES(%s, %s);
            """, (number, person_id))
        conn.commit()

    def change_person(cursor, person_id, first_name=None, last_name=None, email=None, number=None):
        if first_name:
            cursor.execute("""
                UPDATE person SET first_name=%s WHERE id=%s;""",
                (first_name, person_id))
            conn.commit()
        elif last_name:
            cursor.execute("""
                UPDATE person SET last_name=%s WHERE id=%s""",
                (last_name,person_id))
            conn.commit()
        elif email:
            cursor.execute("""
                UPDATE person SET email=%s WHERE id=%s""",
                (email,person_id))
            conn.commit()
        elif number:
            cursor.execute("""
                UPDATE person SET number=%s WHERE id=%s""",
                (number,person_id))
            conn.commit()

    def delete_ph_number(cursor, person_id, number):
        cursor.execute("""
            DELETE FROM phone_number WHERE person_id=%s AND number=%s;""",
            (person_id, number))
        conn.commit()

    def delete_person(cursor, person_id):
        cursor.execute("""
            DELETE FROM person WHERE id=%s;""",
            (person_id,))
        conn.commit()
    def find_person(cursor, first_name=None, last_name=None, email=None, number=None):
         if first_name:
            cursor.execute("""
                SELECT * FROM person WHERE first_name=%s;""",
                (first_name,))
            print(cur.fetchall())
         elif last_name:
             cursor.execute("""
                 SELECT * FROM person WHERE last_name=%s""",
                (last_name,))
             print(cur.fetchall())
         elif email:
             cursor.execute("""
                SELECT * FROM person WHERE email=%s""",
                (email,))
             print(cur.fetchall())
         elif number:
             cursor.execute("""
                SELECT * FROM person WHERE id =(SELECT person_id FROM phone_number WHERE number=%s)""",
                (number,))
             print(cur.fetchall())
         else:
             cursor.execute("""
                SELECT * FROM person""",
                (number,))
             print(cur.fetchall())


