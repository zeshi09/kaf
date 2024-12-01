import os
import json

directory = "."

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory,filename)
        print(filepath)

        input_file = filepath
        output_file = filepath[2:].split(".")[0] + ".geojson"

        with open(input_file, "r") as f:
            coords = json.load(f)

        geojson = {
              "type": "FeatureCollection",
              "features": [
                {
                  "type": "Feature",
                  "properties": {},
                  "geometry": {
                  "coordinates": coords,
                  "type": "LineString"

                  }
                }
              ],
        }

        with open(output_file, "w") as f:
            json.dump(geojson, f, indent=4)

print("U r awesome")
