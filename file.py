from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
import csv
import time
import sqlite3

# Инициализируем пустой список для хранения словарей
data = []

# Чтение CSV и добавление каждой строки как словаря
with open('chrononyms.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(dict(row))

print(data[2])

# Инициализируем геокодер с пользовательским именем приложения
geolocator = Nominatim(user_agent="geo_example")

# Координаты костромской области для ограничения поиска
KOSTROMA_BOUNDING_BOX = [("57.0", "40.0"), ("58.5", "45.5")]

# Функция для получения координат
def get_coordinates(toponym, bounding_box, retries=3):
    for attempt in range(retries):
        try:
            location = geolocator.geocode(
                toponym,
                timeout=10,
                bounded=True,
                viewbox=bounding_box
            )
            if location:
                return (location.latitude, location.longitude)
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Попытка {attempt+1}: ошибка для {toponym} - {e}")
        # except Exception as e:
        #     print(f"Ошибка получения координат для {toponym}: {e}")
    return None

# Заполняем ключ coord координатами для каждого элемента
for item in data:
    item["Coord"] = get_coordinates(item["Toponym"], KOSTROMA_BOUNDING_BOX)
    a = item["Toponym"]
    print(f"Пытаемся найти {a}")
    print(item["Coord"])
    time.sleep(1)  # Пауза, чтобы избежать ограничений по частоте запросов

connection = sqlite3.connect("Locations.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Chrononym TEXT NOT NULL,
        Definition TEXT NOT NULL,
        Context TEXT NOT NULL,
        Toponym TEXT NOT NULL,
        Latitude REAL,
        Longitude REAL
    )
    """
)
connection.commit()


for item in data:
    chron = item["Name"]
    defi = item["Definition"]
    conx = item["Context"]
    top = item["Toponym"]
    if item["Coord"]:
        lat, lon = item["Coord"]
        cursor.execute("INSERT INTO locations (Chrononym, Definition, Context, Toponym, Latitude, Longitude) VALUES (?, ?, ?, ?, ?, ?)", (chron, defi, conx, top, lat, lon))
    else:
        cursor.execute("INSERT INTO locations (Chrononym, Definition, Context, Toponym, Latitude, Longitude) VALUES (?, ?, ?, ?, NULL, NULL)", (chron, defi, conx, top,))

connection.commit()


cursor.execute("SELECT * FROM locations")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close
