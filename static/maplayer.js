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
                    color: 'blue',
                    weight: 3,
                    opacity: 0.1,
                    fill: true,
                    fillColor: 'blue',
                    fillOpacity: 0.2
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/Krasnosel.geojson',
                style: {
                    color: 'red',
                    weight: 3,
                    opacity: 0.1,
                    fill: true,
                    fillColor: 'red',
                    fillOpacity: 0.5
                }
            },
            {
                url: 'https://raw.githubusercontent.com/zeshi09/kaf/refs/heads/main/templates/geos/buyy.geojson',
                style: {
                    color: 'yellow',
                    weight: 3,
                    opacity: 0.1,
                    fill: true,
                    fillColor: 'yellow',
                    fillOpacity: 0.5
                }
            }
        ];

        // Добавление всех слоев на карту
        geojsonLayers.forEach(layer => addGeoJsonLayer(layer.url, layer.style));
