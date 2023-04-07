var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// adding marker
var marker = L.marker([51.5, -0.09]).addTo(map);

// fetching hotels
let hotels = JSON.parse(document.getElementById('hotels_json').textContent);

// add marker for each hotel
hotels.forEach((hotel) => {
    L.marker([hotel.latitude, hotel.longitude]).addTo(map)
        .bindPopup(`<b>${hotel.hotel_name}`)
        .openPopup();
});