# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderServiceError, GeocoderTimedOut
import csv
import time
import sqlite3

# Инициализируем пустой список для хранения словарей
data = []

# Чтение CSV и добавление каждой строки как словаря
with open('chrononyms_fin.csv', mode='r', encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(dict(row))

print(data[2])

#  Инициализируем геокодер с пользовательским именем приложения
# geolocator = Nominatim(user_agent="geo_example")
#
# # Координаты костромской области для ограничения поиска
# KOSTROMA_BOUNDING_BOX = [("57.0", "40.0"), ("58.5", "45.5")]
#
# # Функция для получения координат
# def get_coordinates(toponym, bounding_box, retries=3):
#     for attempt in range(retries):
#         try:
#             location = geolocator.geocode(
#                 toponym,
#                 timeout=10,
#                 bounded=True,
#                 viewbox=bounding_box
#             )
#             if location:
#                 return (location.latitude, location.longitude)
#         except (GeocoderTimedOut, GeocoderServiceError) as e:
#             print(f"Попытка {attempt+1}: ошибка для {toponym} - {e}")
#         # except Exception as e:
#         #     print(f"Ошибка получения координат для {toponym}: {e}")
#     return None

# Заполняем ключ coord координатами для каждого элемента
coords = []
with open('districts_coords.csv', mode='r', encoding="utf-8-sig") as f:
    reader_coord = csv.DictReader(f)
    for row in reader_coord:
        coords.append(dict(row))
print(coords[2])

for item in data:
    for item2 in coords:
        if item["SS"] == item2["SS"] and item["District"] == item2["Short_dis"]:
            item["Latitude"] = item2["Lat"]
            item["Longitude"] = item2["Long"]
        else:
            print(item2)
print(data[2])

# for item in data:
#     item["Coord"] = get_coordinates(item["Toponym"], KOSTROMA_BOUNDING_BOX)
#     a = item["Toponym"]
#     print(f"Пытаемся найти {a}")
#     print(item["Coord"])
#     time.sleep(1)  # Пауза, чтобы избежать ограничений по частоте запросов
#
connection = sqlite3.connect("Locations_fin.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Chrononym TEXT NOT NULL,
        Definition TEXT NOT NULL,
        Context TEXT NOT NULL,
        District TEXT NOT NULL,
        Selsovet TEXT NOT NULL,
        Latitude REAL,
        Longitude REAL,
        Comment TEXT,
        Year TEXT NOT NULL,
        District_ss TEXT NOT NULL
    )
    """
)
connection.commit()

count = 0
for item in data:
    count += 1
    chron = item["Chrononym"]
    defi = item["Def"]
    conx = item["Context"]
    dis = item["District"]
    ss = item["SS"]
    year = item["Year"]
    comm = item["Comment"]
    diss = dis + ", " + ss
    lt = 57.707405 
    ln = 39.898133
    if item["Latitude"]:
        lat = item["Latitude"]
        lon = item["Longitude"]
        cursor.execute("INSERT INTO locations (Chrononym, Definition, Context, District, Selsovet, Latitude, Longitude, Comment, Year, District_ss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (chron, defi, conx, dis, ss, lat, lon, year, comm, diss))
    else:
        cursor.execute("INSERT INTO locations (Chrononym, Definition, Context, District, Selsovet, Latitude, Longitude, Comment, Year, District_ss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (chron, defi, conx, dis, ss, lt, ln, comm, year, diss))

connection.commit()


cursor.execute("SELECT * FROM locations")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close
