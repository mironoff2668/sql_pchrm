import psycopg2

def create_db(cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS personal_info(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(60) NOT NULL,
        last_name VARCHAR(60) NOT NULL,
        email VARCHAR(60) NOT NULL UNIQUE);
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        phone VARCHAR(60),
        pers_id INTEGER REFERENCES personal_info(personal_id));
        """
    )
    conn.commit()
    pass

def add_new_personal(cur, first_name, last_name, email, phone=None):
    cur.execute(
        """
        INSERT INTO personal_info(first_name, last_name, email)
        VALUES(%s, %s, %s);
        """,
        (first_name, last_name, email)
    )

    cur.execute(
        """
        INSERT INTO phones(phone, personal_id)
        VALUES (%s, (SELECT id FROM personal_info WHERE name = %s));
        """,
        (phone, first_name, )
        )
    conn.commit
    pass

def add_phone(cur, phone, personal_id):
    cur.execute(
        """
        INSERT INTO phones(phone)
        VALUES (%s, %s);
        """,
        (phone, personal_id, )
    )
    conn.commit
    pass

def change_person(cur, personal_id, first_name=None, last_name=None, email=None, phone=None):
    if first_name is not None:
        cur.execute(
            """
            UPDATE personal_info
            SET name = %s
            WHERE personal_id = %s AND name <> %s;
            """,
            (first_name, personal_id, first_name)
        )
    elif last_name is not None:
        cur.execute(
            """
            UPDATE personal_info
            SET name = %s
            WHERE personal_id = %s AND first_name <> %s;
            """,
            (last_name, personal_id, last_name)
        )
    elif email is not None:
        cur.execute(
            """
            UPDATE personal_info
            SET email = %s
            WHERE personal_id = %s AND email <> %s;
            """,
            (email, personal_id, email)
        )
    elif phone is not None:
        cur.execute(
            """
            UPDATE phones
            SET phone = %s
            WHERE personal_id = %s AND phone <> %s;
            """,
            (phone, personal_id, phone)
        )
        conn.commit
        pass

def delete_phone(cur, phone):
    cur.execute(
        """
        DELETE FROM phones
        WHERE personal_id = %s;
        """,
        (personal_id)
    )
    cur.execute(
        """
        DELETE FROM personal_info
        WHERE personal_id = %s;
        """,
        (personal_id)
    )
    conn.commit
    pass

def find_personal(cur, first_name=None, last_name=None, email=None, phone=None):
    if phone is not None:
        cur.execute(
            """
            SELECT pi.first_name, pi.last_name, pi.email, p.phone FROM personal_info pi
            JOIN phones p ON pi.personal_id = p.personal_id
            WHERE pi.first_name LIKE %s OR pi.last_name LIKE %s
            OR pi.email LIKE %s or p.phone LIKE %s;
            """,
            (first_name, last_name, email, phone)
        )
    else:
        cur.execute(
            """
            SELECT pi.first_name, pi.last_name, pi.email, p.phone FROM personal_id pi
            JOIN phones p ON pi.personal_id = p.personal_id
            WHERE pi.first_name LIKE %s or pi.last_name LIKE %s
            OR pi.email LIKE %s;
            """,
            (first_name, last_name, email)
        )
        print(cur.fetchall())
        pass



if __name__ == '__main__':
    with psycopg2.connect(database='hw_def_sql', user='postgres', password='polo1gavonon') as conn:
        with conn.cursor() as cur:
            create_db(cur)
            add_new_personal(cur, 'Oleg', 'Smirnov', 'o.smirnov@gmail.com', '+79214457855')
            add_new_personal(cur, 'Olga', 'Ivanova', 'o.ivanova@gmail.com', '+79995546658')
            add_new_personal(cur, 'Andrey', 'Petrov', 'a.petrov@gmail.com', '+79112585236')
            find_personal(cur, 'Andrey')
            find_personal(cur, '79112585236')
            change_person(cur)