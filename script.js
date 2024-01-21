//set view
var map = L.map('map').setView([-32, 21], 6);

// layers
var streets = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap contributors'
});

var satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 20,    
    attribution: '© OpenStreetMap contributors'
});

// marker
var nthuMarker = L.marker([-32, 21]).bindPopup('NTHU'); //緯, 經
var markers = L.layerGroup([nthuMarker]);

// GeoJSON data
var geojson = new L.GeoJSON.AJAX('./data/bioscape_domain_20220201.geojson');

// objects for layer control
var baseLayers = {
    "Streets": streets,
    "Satellite": satellite,
};

var overlays = {
    "Markers": markers
};

// add to map
streets.addTo(map);
markers.addTo(map);
geojson.addTo(map);
L.control.layers(baseLayers, overlays).addTo(map); //layer control widget 

// window switch
function page1() {
    window.location.href = 'index.html';
    map.setView([-32, 21], 6); // reset view
}
function page2() {
    window.location.href = 'data.html'; 
}
