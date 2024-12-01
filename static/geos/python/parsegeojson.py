import requests
from transliterate import translit
import json
import time
from fake_useragent import UserAgent

ua = UserAgent()
randomua = ua.random
headers = {
        'User-Agent': randomua
        }

def area_coords_parser(search, max_retries=10, retry_delay=2):
    base_url = "http://nominatim.openstreetmap.org/search"
    params = {
        "format": "json",
        "q": search,
        "polygon_geojson": 1
    }

    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(base_url, params=params, headers=headers)
            
            if response.status_code == 403:
                print(f"403 Forbidden for '{search}'. Retrying... ({retries + 1}/{max_retries})")
                retries += 1
                time.sleep(retry_delay)  # Ожидаем перед повторной попыткой
                continue
            
            response.raise_for_status()  # Вызывает исключение для других ошибок HTTP
            data = response.json()

            if not data:
                return f"No data found for '{search}'"

            result = []

            # Извлекаем координаты из geojson
            geojson = data[0].get("geojson", {})
            geojson_type = geojson.get("type")
            coordinates = geojson.get("coordinates", [])

            if geojson_type == "MultiPolygon":
                for polygon in coordinates:
                    temp = []
                    for coord in polygon[0]:  # Берем внешний контур
                        temp.append(coord)  # Не меняем местами широту и долготу
                    result.append(temp)
            elif geojson_type == "Polygon":
                for coord in coordinates[0]:  # Берем внешний контур
                    result.append(coord)  # Не меняем местами широту и долготу

            return result

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(retry_delay)  # Ожидаем перед повторной попыткой

    return f"Failed to fetch data for '{search}' after {max_retries} retries."

with open('districts.txt', "r", encoding="utf-8") as districts:
    for line in districts:
        region = line
        coords = area_coords_parser(region)

        # Сохраняем результат в JSON-файл
        if isinstance(coords, list):  # Успешный результат
            with open(f"{translit(region.split(' ')[0], language_code='ru', reversed=True)}.json", "w", encoding="utf-8") as file:
                json.dump(coords, file, ensure_ascii=False, indent=4)
            print(f"Coordinates for '{region}' saved to {translit(region.split(' ')[0], language_code='ru', reversed=True)}.json")
        else:  # Ошибка
            print(coords)
