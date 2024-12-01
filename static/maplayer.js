        // Функция для добавления слоев по районам
        function addGeoJsonLayer(url, style) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    L.geoJSON(data, { style }).addTo(map);
                })
                .catch(error => console.error(`Error loading GeoJSON from ${url}:`, error));
        }

        // Определение URL-адресов и стилей
        const geojsonLayers = [
            {
                url: 'https://raw.githubusercontent.com/simp37/Russia_geoJSON/refs/heads/master/Kostromskaya.geojson',
                style: {
                    color: 'black',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'blue',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Antropovskij.geojson',
                style: {
                    color: 'red',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'red',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/buyy.geojson',
                style: {
                    color: 'yellow',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'yellow',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Chuhlomskoj.geojson',
                style: {
                    color: 'gray',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'gray',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Galichskij.geojson',
                style: {
                    color: 'purple',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'purple',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Kadyjskij.geojson',
                style: {
                    color: 'brown',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'brown',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Kologrivskij.geojson',
                style: {
                    color: 'white',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'white',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Kologrivskij.geojson',
                style: {
                    color: 'white',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'white',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Kostromskoj.geojson',
                style: {
                    color: 'pink',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'pink',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Krasnoselskij.geojson',
                style: {
                    color: 'orange',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'orange',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Makarevskij.geojson',
                style: {
                    color: 'violet',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'violet',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Manturovskij.geojson',
                style: {
                    color: 'violet',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'violet',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Mezhevskoj.geojson',
                style: {
                    color: 'red',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'red',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Nejskij.geojson',
                style: {
                    color: 'black',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'black',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Nerehtskij.geojson',
                style: {
                    color: 'green',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'green',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Oktjabrskij.geojson',
                style: {
                    color: 'yellow',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'yellow',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Ostrovskij.geojson',
                style: {
                    color: 'white',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'white',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Parfenevskij.geojson',
                style: {
                    color: 'green',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'green',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Ponazyrevskij.geojson',
                style: {
                    color: 'blue',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'blue',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Pyschugskij.geojson',
                style: {
                    color: 'green',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'green',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Sharinskij.geojson',
                style: {
                    color: 'orange',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'orange',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Soligalich.geojson',
                style: {
                    color: 'orange',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'orange',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Sudislavskij.geojson',
                style: {
                    color: 'black',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'black',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Susaninskij.geojson',
                style: {
                    color: 'red',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'red',
                    fillOpacity: 0.1
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Vohomskij.geojson',
                style: {
                    color: 'violet',
                    weight: 1,
                    opacity: 0.5,
                    fill: true,
                    fillColor: 'violet',
                    fillOpacity: 0.1
                }
            }
      ];

        // Добавление всех слоев на карту
        geojsonLayers.forEach(layer => addGeoJsonLayer(layer.url, layer.style));
