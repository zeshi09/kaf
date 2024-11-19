from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных и извлечения данных
def get_data_from_db(chrononym=None, toponym=None):
    conn = sqlite3.connect("Locations.db")
    cursor = conn.cursor()

    # if chrononym:
    #     query = """
    #         SELECT Chrononym, Definition, Context, Toponym, Latitude, Longitude
    #         FROM locations
    #         WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL AND Chrononym=?
    #     """
    #     cursor.execute(query, (chrononym,))
    # else:
    #     query = """
    #         SELECT Chrononym, Definition, Context, Toponym, Latitude, Longitude
    #         FROM locations
    #         WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL
    #     """
    #     cursor.execute(query)

    query = """
        SELECT Chrononym, Definition, Context, Toponym, Latitude, Longitude
        FROM locations
        WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL
    """
    params = []

    if chrononym:
        query += " AND Chrononym = ?"
        params.append(chrononym)
    if toponym:
        query += " AND Toponym = ?"
        params.append(toponym)

    cursor.execute(query, tuple(params))
    data = cursor.fetchall()
    conn.close()
    return data

# Главная страница с картой
@app.route("/")
def index():
    return render_template("map.html")

# API для получения всех точек (с возможностью фильтрации)
@app.route("/api/locations")
def locations():
    chrononym = request.args.get("chrononym")
    toponym = request.args.get("toponym")
    data = get_data_from_db(chrononym, toponym)

    response = [
        {
            "chrononym": row[0],
            "definition": row[1],
            "context": row[2],
            "toponym": row[3],
            "latitude": row[4],
            "longitude": row[5],
        }
        for row in data
    ]
    return jsonify(response)

# API для получения уникальных значений Chrononym
@app.route("/api/chrononyms")
def get_chrononyms():
    conn = sqlite3.connect("Locations.db")
    cursor = conn.cursor()

    query = "SELECT DISTINCT Chrononym FROM locations WHERE Chrononym IS NOT NULL"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    chrononyms = [row[0] for row in data]
    return jsonify(chrononyms)
# API для получения уникальных значений Toponym
@app.route("/api/toponyms")
def get_toponyms():
    conn = sqlite3.connect("Locations.db")
    cursor = conn.cursor()

    query = "SELECT DISTINCT Toponym FROM locations WHERE Toponym IS NOT NULL"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    toponyms = [row[0] for row in data]
    return jsonify(toponyms)
if __name__ == "__main__":
    app.run(debug=True)

