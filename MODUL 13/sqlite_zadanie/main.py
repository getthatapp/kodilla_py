import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database_user.db')
        print(sqlite3.version)
    except Error as e:
        print(e)

    if conn:
        return conn


def create_table(conn):
    try:
        sql_create_table_query = """ CREATE TABLE IF NOT EXISTS users (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            email text NOT NULL UNIQUE
                                            ); """
        conn.execute(sql_create_table_query)
    except Error as e:
        print(e)


def create_user(conn, user):
    sql = ''' INSERT INTO users (name, email) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid


def get_user(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def update_user(conn, user):
    sql = ''' UPDATE users SET name = ?, email = ? WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()


def delete_user(conn, id):
    sql = ' DELETE FROM users WHERE id=? '
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def main():
    database = create_connection()
    create_table(database)

    user1 = ('Jan', 'jan@kowalski.com')
    user1_id = create_user(database, user1)
    print("Utworzono użytkownika: ")
    get_user(database, user1_id)

    user1 = ('Janusz', 'janusz@kowalski.pl', user1_id)
    update_user(database, user1)
    print("Zaktualizowano użytkownika: ")
    get_user(database, user_id)

    user2 = ('Adam', 'adam@nowak.com')
    user2_id = create_user(database, user2)
    print("Utworzono drugiego użytkownika: ")
    get_user(database, user2_id)

    delete_user(database, user1_id)
    print("Usunięto pierwszego użytkownika, brak wyników: ")
    get_user(database, user1_id)
    print("Drugi użytkownik jest nadal dostępny: ")
    get_user(database, user2_id)


if __name__ == '__main__':
    main()
