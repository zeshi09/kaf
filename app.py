from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных и извлечения данных
def get_data_from_db(chrononym=None):
    conn = sqlite3.connect("database.db")
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

# API для автозаполнения (поиск по Chrononym)
@app.route("/api/autocomplete")
def autocomplete():
    term = request.args.get("term", "").lower()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = """
        SELECT DISTINCT Chrononym
        FROM locations
        WHERE LOWER(Chrononym) LIKE ?
        LIMIT 10
    """
    cursor.execute(query, (f"%{term}%",))
    data = cursor.fetchall()
    conn.close()

    results = [row[0] for row in data]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

