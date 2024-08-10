@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    conn1 = sqlite3.connect('people_vehicles.db')
    c1 = conn1.cursor()
    c1.execute('SELECT DISTINCT name FROM people_vehicles WHERE name LIKE ?', (f'%{search}%',))
    results = c1.fetchall()
    conn1.close()
    return jsonify([{'name': result[0]} for result in results])

@app.route('/department1', methods=['GET', 'POST'])
def department1():
    if request.method == 'POST':
        name = request.form['name']
        conn1 = sqlite3.connect('people_vehicles.db')
        c1 = conn1.cursor()
        c1.execute('SELECT name, birthdate FROM people_vehicles WHERE name LIKE ?', (f'%{name}%',))
        people = c1.fetchall()
        conn1.close()

        if len(people) == 1:
            person_name = people[0][0]
            birthdate = people[0][1]
            conn1 = sqlite3.connect('people_vehicles.db')
            c1 = conn1.cursor()
            c1.execute('SELECT vehicle, source FROM people_vehicles WHERE name = ? AND birthdate = ?', (person_name, birthdate))
            vehicles = c1.fetchall()
            conn1.close()

            conn2 = sqlite3.connect('people_addresses.db')
            c2 = conn2.cursor()
            c2.execute('SELECT address, source FROM people_addresses WHERE name = ? AND birthdate = ?', (person_name, birthdate))
            addresses = c2.fetchall()
            conn2.close()

            return render_template('person_info.html', name=person_name, birthdate=birthdate, vehicles=vehicles, addresses=addresses)
        else:
            return render_template('select_person.html', people=people)
    return render_template('department1.html')

