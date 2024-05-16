document.addEventListener('DOMContentLoaded', function() {
    populateSelectOptions();
    fetchData();
    populateLegend();
});

mapboxgl.accessToken = 'pk.eyJ1IjoiYWFmMzYiLCJhIjoiY2x3Nmo1Z2dtMXJwbTJpcHllaXNta3YyeSJ9.ZaeHe7SF26RZavgh9AgHrA';

const initialViewState = {
    longitude: 35.5,
    latitude: 33.8,
    zoom: 5,  // Adjusted zoom level
    pitch: 0,
    bearing: 0
};

// Initialize the Mapbox GL JS map
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v10',
    center: [initialViewState.longitude, initialViewState.latitude],
    zoom: 5,  // Adjusted zoom level
    minZoom: 4,  // Allow more zoom out
    maxBounds: [
        [34.5, 32.5], // Southwest coordinates (loosened bottom-left corner)
        [37.0, 35.0]  // Northeast coordinates (loosened top-right corner)
    ]
});

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());

// Define shades of red for each corruption type
const corruptionColors = {
    'فساد سياسي': [255, 0, 0],
    'تأثيرات سلبية على استقلالية القضاء': [255, 69, 0],
    'فساد قانوني': [255, 99, 71],
    'احتكار': [255, 140, 105],
    'تقصير أو اهمال في توفير السلامة': [255, 160, 122],
    'فساد بيئي.': [255, 182, 193],
    'فساد مالي': [255, 0, 0],
    'تجاوز السلطة': [204, 0, 0],
    'فساد اداري': [153, 0, 0],
    'فساد عقاري': [255, 69, 0],
    'انتهاكات حقوق انسان': [255, 99, 71],
    'تغطية': [255, 140, 105],
    'فساد تعييني': [255, 160, 122],
    'فساد في العقود': [255, 182, 193],
    'تقييد حرية التعبير': [204, 0, 0],
    'اهمال': [153, 0, 0],
    'اختلاس الأموال العامة': [255, 0, 0],
    'جريمة': [255, 69, 0],
    'سوء ادارة': [255, 99, 71],
    'عدم الشفافية': [255, 140, 105],
    'فساد سلوكي / فساد أخلاقي': [255, 160, 122],
    'تلاعب بالصفقات': [255, 182, 193],
    'تهديدات عنيفة': [204, 0, 0],
    'بيروقراطية': [153, 0, 0],
    'انحياز واستغلال الموقف': [255, 0, 0],
    'تزوير واستعمال مزور': [255, 69, 0],
    'اتهامات بالاختلاس وغسيل الأموال': [255, 99, 71],
    'قمع': [255, 140, 105],
    'زيادة الأسعار بصورة غير مبررة': [255, 160, 122],
    'سرقة': [255, 182, 193],
    'التهريب': [204, 0, 0],
    'الفساد المرتبط بالأحزاب السياسية والمسؤولين': [153, 0, 0],
    'تقصير': [255, 0, 0],
    'تشويه الحقائق': [255, 69, 0]
};

// Create the Deck.gl scatterplot layer with glow effect
const deckLayer = new deck.MapboxLayer({
    id: 'deck-layer',
    type: deck.ScatterplotLayer,
    data: [],
    getPosition: d => [d.longitude, d.latitude],
    getFillColor: d => corruptionColors[d.corruption_type] || [255, 0, 0],
    getRadius: d => 200, // Adjust the radius as needed
    radiusScale: 10,
    radiusMinPixels: 5,
    radiusMaxPixels: 200,
    opacity: 0.8,
    stroked: true,
    getLineWidth: 5,
    lineWidthMinPixels: 2,
    getLineColor: [255, 255, 255, 255]  // White outline for glow effect
});


// Add the Deck.gl layer to the Mapbox map
map.on('load', function() {
    map.addLayer(deckLayer);
});

document.getElementById('filter-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const corruptionType = document.getElementById('corruption_type').value;
    const sectorType = document.getElementById('public_sector_type').value;
    fetchData(corruptionType, sectorType);
});

function fetchData(corruptionType = '', sectorType = '') {
    const url = new URL('/corruption-heatmap/', window.location.origin);
    if (corruptionType) {
        url.searchParams.append('corruption_type', corruptionType);
    }
    if (sectorType) {
        url.searchParams.append('public_sector_type', sectorType);
    }
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            renderHeatmap(data);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function renderHeatmap(data) {
    deckLayer.setProps({
        data: data
    });
}

function populateSelectOptions() {
    fetch('/choices/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const corruptionTypeSelect = document.getElementById('corruption_type');
            data.corruption_types.forEach(type => {
                const option = document.createElement('option');
                option.value = type[0];
                option.textContent = type[1];
                corruptionTypeSelect.appendChild(option);
            });

            const sectorTypeSelect = document.getElementById('public_sector_type');
            data.sector_types.forEach(type => {
                const option = document.createElement('option');
                option.value = type[0];
                option.textContent = type[1];
                sectorTypeSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching choices:', error));
}

function populateLegend() {
    const legendContainer = document.getElementById('legend-container');
    legendContainer.innerHTML = ''; // Clear existing legend items

    Object.keys(corruptionColors).forEach(type => {
        const legendItem = document.createElement('div');
        legendItem.className = 'legend-item';

        const legendColor = document.createElement('div');
        legendColor.className = 'legend-color';
        legendColor.style.backgroundColor = `rgb(${corruptionColors[type].join(',')})`;

        const legendText = document.createElement('span');
        legendText.textContent = type;

        legendItem.appendChild(legendColor);
        legendItem.appendChild(legendText);
        legendContainer.appendChild(legendItem);
    });
}

document.getElementById('toggle-legend-button').addEventListener('click', function() {
    const legendContainer = document.getElementById('legend-container');
    if (legendContainer.style.display === 'none') {
        legendContainer.style.display = 'block';
    } else {
        legendContainer.style.display = 'none';
    }
});


