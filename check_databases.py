import sqlite3


def check_table(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    try:
        c.execute(f"SELECT * FROM {table_name}")
        rows = c.fetchall()
        print(f"\nСодержимое таблицы {table_name} в {db_name}:")
        for row in rows:
            print(row)
    except sqlite3.OperationalError as e:
        print(f"Ошибка: {e}")

    conn.close()


if __name__ == "__main__":
    print("Проверка базы данных people_vehicles.db:")
    check_table('people_vehicles.db', 'people_vehicles')

    print("Проверка базы данных people_addresses.db:")
    check_table('people_addresses.db', 'people_addresses')
