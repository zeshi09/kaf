function fetchLocations(chrononym = "", toponym = "") {
    console.log("Fetching locations with filters:", { chrononym, toponym });

    // Удаляем старые маркеры
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];

    // Запрос на сервер для получения данных
    fetch(`/api/locations?chrononym=${encodeURIComponent(chrononym)}&toponym=${encodeURIComponent(toponym)}`)
        .then(response => {
            console.log("Server response status:", response.status);
            if (!response.ok) {
                throw new Error(`Failed to fetch locations. Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Fetched data:", data);

            const locationsList = document.getElementById('locations-list');
            locationsList.innerHTML = ""; // Очищаем список перед обновлением

            document.getElementById('selected-count').textContent = `Выбрано: ${data.length}`;

            if (data.length === 0) {
                console.warn("No locations found for the given filters.");
                return;
            }

            // Группируем маркеры по координатам для отображения на карте
            let groupedMarkers = {};
            data.forEach(location => {
                // Проверяем корректность координат
                if (isNaN(location.latitude) || isNaN(location.longitude)) {
                    console.error("Invalid location coordinates:", location);
                    return; // Пропускаем некорректные данные
                }

                const key = `${location.latitude}, ${location.longitude}`;
                if (!groupedMarkers[key]) {
                    groupedMarkers[key] = [];
                }
                groupedMarkers[key].push(location);

                // Создаем список для каждого элемента (не группируем)
                const listItem = document.createElement('div');
                listItem.innerHTML = `
                    <b>${location.chrononym}</b><br>
                    <i>${location.definition}</i><br>
                    ${location.context}<br>
                    <small>${location.toponym}</small>
                `;
                listItem.style.cursor = 'pointer';
                listItem.style.padding = '10px';
                listItem.style.marginBottom = '10px';

                listItem.addEventListener('click', () => {
                    const lat = location.latitude;
                    const lng = location.longitude;
                    console.log("List item clicked. Moving to:", { lat, lng });
                    map.setView([lat, lng], 10);
                    markers.forEach(marker => {
                        if (marker.getLatLng().lat === lat && marker.getLatLng().lng === lng) {
                            marker.openPopup();
                        }
                    });
                });

                locationsList.appendChild(listItem);
            });

            // Создаем маркеры на карте для каждой группы по координатам
            Object.keys(groupedMarkers).forEach(key => {
                const group = groupedMarkers[key];
                const [lat, lng] = key.split(',').map(Number);

                console.log("Creating marker for group at:", { lat, lng });

                const marker = L.marker([lat, lng])
                    .addTo(map)
                    .bindPopup(generatePopupContent(group));
                markers.push(marker);
            });
        })
        .catch(error => console.error("Error fetching locations:", error));
}

function generatePopupContent(group) {
    let content = '<b>Элементы в этой точке:</b><br>';
    group.forEach(location => {
        content += `
            <b>${location.chrononym}</b><br>
            <i>${location.definition}</i><br>
            ${location.context}<br>
            <small>${location.toponym}</small><br><br>
        `;
    });
    return content;
}

