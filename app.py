from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных и извлечения данных
def get_data_from_db(chrononym=None):
    conn = sqlite3.connect("Locations.db")
    cursor = conn.cursor()

    if chrononym:
        query = """
            SELECT Chrononym, Definition, Context, Toponym, Latitude, Longitude
            FROM locations
            WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL AND Chrononym=?
        """
        cursor.execute(query, (chrononym,))
    else:
        query = """
            SELECT Chrononym, Definition, Context, Toponym, Latitude, Longitude
            FROM locations
            WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL
        """
        cursor.execute(query)

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
    data = get_data_from_db(chrononym)

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

if __name__ == "__main__":
    app.run(debug=True)

