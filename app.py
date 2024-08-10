from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Функции для получения данных из баз данных
def get_people_from_department1(query=None):
    conn = sqlite3.connect('people_vehicles.db')
    c = conn.cursor()
    if query:
        c.execute("SELECT name, dob, vehicle FROM people_vehicles WHERE LOWER(name) LIKE LOWER(?)", (query + '%',))
    else:
        c.execute("SELECT name, dob, vehicle FROM people_vehicles")
    results = c.fetchall()
    conn.close()
    return [{'name': row[0], 'dob': row[1], 'vehicle': row[2]} for row in results]

def get_people_from_department2(query=None):
    conn = sqlite3.connect('people_addresses.db')
    c = conn.cursor()
    if query:
        c.execute("SELECT name, dob, address FROM people_addresses WHERE LOWER(name) LIKE LOWER(?)", (query + '%',))
    else:
        c.execute("SELECT name, dob, address FROM people_addresses")
    results = c.fetchall()
    conn.close()
    return [{'name': row[0], 'dob': row[1], 'address': row[2]} for row in results]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/department1')
def department1():
    return render_template('department1.html')

@app.route('/department2')
def department2():
    return render_template('department2.html')

@app.route('/list_department1')
def list_department1():
    people = get_people_from_department1()
    return jsonify(people)

@app.route('/list_department2')
def list_department2():
    people = get_people_from_department2()
    return jsonify(people)

@app.route('/autocomplete_department1')
def autocomplete_department1():
    query = request.args.get('q', '').strip()
    results = get_people_from_department1(query)
    return jsonify(results)

@app.route('/autocomplete_department2')
def autocomplete_department2():
    query = request.args.get('q', '').strip()
    results = get_people_from_department2(query)
    return jsonify(results)

@app.route('/person_details')
def person_details():
    name = request.args.get('name')
    dob = request.args.get('dob')
    department = int(request.args.get('department'))

    if department == 1:
        results1 = get_people_from_department1(name)
        results2 = get_people_from_department2(name)
    else:
        results1 = get_people_from_department2(name)
        results2 = get_people_from_department1(name)

    return render_template('person_details.html', name=name, dob=dob, results1=results1, results2=results2, department=department)

if __name__ == '__main__':
    app.run(debug=True)
