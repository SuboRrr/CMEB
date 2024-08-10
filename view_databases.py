import sqlite3

def view_databases():
    conn1 = sqlite3.connect('people_vehicles.db')
    c1 = conn1.cursor()
    c1.execute('SELECT * FROM people_vehicles')
    rows1 = c1.fetchall()
    print("Содержимое people_vehicles.db:")
    for row in rows1:
        print(row)
    conn1.close()

    conn2 = sqlite3.connect('people_addresses.db')
    c2 = conn2.cursor()
    c2.execute('SELECT * FROM people_addresses')
    rows2 = c2.fetchall()
    print("Содержимое people_addresses.db:")
    for row in rows2:
        print(row)
    conn2.close()

if __name__ == '__main__':
    view_databases()
