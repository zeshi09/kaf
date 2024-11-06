from geopy.geocoders import Nominatim
import csv
import time

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

# Функция для получения координат
def get_coordinates(toponym, retries=3):
    try:
        location = geolocator.geocode(toponym, timeout=10)
        if location:
            return (location.latitude, location.longitude)
    except Exception as e:
        print(f"Ошибка получения координат для {toponym}: {e}")
    return None

# Заполняем ключ coord координатами для каждого элемента
for item in data:
    item["Coord"] = get_coordinates(item["Toponym"])
    a = item["Toponym"]
    print(f"Пытаемся найти {a}")
    print(item["Coord"])
    time.sleep(1)  # Пауза, чтобы избежать ограничений по частоте запросов

