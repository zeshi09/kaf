//import { fetchLocations } from './fetch_locations_old.js';
//import { generatePopupContent } from './fetch_locations_old.js';
const map = L.map('map', {
        attributionControl: false,
        center: [58.0, 43.5],
        zoom: 7.5,
        maxZoom: 15,
        minZoom: 1
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '',
          attributionControl: false,
          noWrap: true
      }).addTo(map);

      let markers = [];
      
      
      function fetchLocations(chrononym = "", toponym = "", district = "") {
          console.log("Fetching locations with filters:", { chrononym, toponym, district });

          // Удаляем старые маркеры
          markers.forEach(marker => map.removeLayer(marker));
          markers = [];

          // Запрос на сервер для получения данных
          fetch(`/api/locations?chrononym=${encodeURIComponent(chrononym)}&toponym=${encodeURIComponent(toponym)}&district=${encodeURIComponent(district)}`)
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
                          <i>${location.comment}</i><br>
                          <small>${location.distr}</small>
                          <small>${location.toponym}</small>
                          <small>${location.year}</small>
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
          group.forEach((location, index) => {
              content += `
                  <div class="popup-item" data-index="${index}">
                      <b>${location.chrononym}</b><br>
                      <i>${location.definition}</i><br>
                      ${location.context}<br>
                      <b><i>${location.comment}</i></b><br>
                      <small>${location.distr}</small><br>
                      <small>${location.toponym}</small><br>
                      <small>${location.year}</small><br>
                  </div>
              `;
          });
          return content;
      }

      // Функция для загрузки уникальных Chrononym
      function loadChrononyms() {
          fetch('/api/chrononyms')
              .then(response => response.json())
              .then(data => {
                  const select = document.getElementById('chrononym');
                  data.forEach(chrononym => {
                      const option = document.createElement('option');
                      option.value = chrononym;
                      option.textContent = chrononym;
                      select.appendChild(option);
                  });
              })
              .catch(error => console.error('Error loading chrononyms:', error));
      }

      // Функция для загрузки уникальных Toponym
      function loadToponyms() {
          fetch('/api/toponyms') // Предполагается, что ваш API возвращает список топонимов
              .then(response => response.json())
              .then(data => {
                  const select = document.getElementById('toponym');
                  data.forEach(toponym => {
                      const option = document.createElement('option');
                      option.value = toponym;
                      option.textContent = toponym;
                      select.appendChild(option);
                  });
              })
              .catch(error => console.error('Error loading toponyms:', error));
      }

      // Функция для загрузки уникальных District
      function loadDistricts() {
          fetch('/api/districts') // Предполагается, что ваш API возвращает список топонимов
              .then(response => response.json())
              .then(data => {
                  const select = document.getElementById('district');
                  data.forEach(district => {
                      const option = document.createElement('option');
                      option.value = district;
                      option.textContent = district;
                      select.appendChild(option);
                  });
              })
              .catch(error => console.error('Error loading districts:', error));
      }


      // Обработчик кнопки фильтрации
      document.getElementById("filter-btn").addEventListener("click", () => {
          // Получаем значения полей ввода
          const chrononym = document.getElementById("chrononym").value;
          const toponym = document.getElementById("toponym").value;
          const district = document.getElementById("district").value;

          // Логи для отладки
          console.log("Filter button clicked");
          console.log("Chrononym value:", chrononym);
          console.log("Toponym value:", toponym);
          console.log("District value:", district);

          // Проверка значений перед вызовом функции
          if (!chrononym && !toponym && !district) {
              console.warn("No filter values provided. Both fields are empty.");
          }

          // Вызов функции с логами
          console.log("Calling fetchLocations with:", { chrononym, toponym, district });
          fetchLocations(chrononym, toponym, district)
              .then(() => console.log("fetchLocations completed successfully"))
              .catch(err => console.error("Error in fetchLocations:", err));
      });


      // Показать кнопку, если прокрутили вниз
      const sidebar = document.getElementById('locations-list');
      const scrollToTopBtn = document.getElementById('scroll-to-top');
      sidebar.addEventListener('scroll', () => {
          if (sidebar.scrollTop > 100) {
              scrollToTopBtn.style.display = 'block';
          } else {
              scrollToTopBtn.style.display = 'none';
          }
      });

      // Обработчик нажатия на кнопку
      scrollToTopBtn.addEventListener('click', () => {
          sidebar.scrollTo({
              top: 0,
              behavior: 'smooth' // Плавная прокрутка
          });
      });

      // Загрузка всех точек при загрузке страницы
      fetchLocations();

      // Загрузка уникальных Chrononym при загрузке страницы
      loadChrononyms();
      loadToponyms();
      loadDistricts();

