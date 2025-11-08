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
                    SELECT * FROM phone_number WHERE person_id=%s AND number=%s;""",
                       (person_id, number))
        if len(cursor.fetchall()) == 0:
            print('Такого номер нет')
            return

        cursor.execute("""
            DELETE FROM phone_number as pn WHERE person_id=%s AND number=%s;""",
            (person_id, number))
        conn.commit()

    def delete_person(cursor, person_id):
        cursor.execute("""
            SELECT * FROM person WHERE id=%s;""",
            (person_id,))
        if len(cursor.fetchall()) == 0:
            print('Такого клиента нет')
            return

        cursor.execute("""
            DELETE FROM person as p WHERE id=%s;""",
            (person_id,))
        conn.commit()
        print(f'Удалена записаь о клиенте с ID {person_id}')
    def find_person(cursor, first_name=None, last_name=None, email=None, number=None):
         cursor.execute("""
            SELECT p.*, pn.number FROM person as p
            JOIN phone_number as pn ON p.id=pn.person_id
            WHERE (first_name = %(first_name)s OR first_name = %(first_name)s is NULL)
            AND (last_name = %(last_name)s OR last_name = %(last_name)s is NULL)
            AND (email = %(email)s OR email = %(email)s is NULL)
            AND (number = %(number)s OR number = %(number)s is NULL)
            """,
            {'first_name' : first_name, 'last_name' : last_name, 'email' : email, 'number' : number})
         print('Найдена запись о клиенте: ', cursor.fetchall())




