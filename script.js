document.addEventListener("DOMContentLoaded", () => {
    console.log("Website loaded!");

    // Button event listeners
    document.getElementById('congestion-button').addEventListener('click', showCongestion);
    document.getElementById('reroute-button').addEventListener('click', rerouteFlight);
    document.getElementById('updates-button').addEventListener('click', getRealTimeUpdates);
    document.getElementById("contactForm").addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = {
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone_number: document.getElementById("phone_number").value,
            contact_message: document.getElementById("contact_message").value
        };

        fetch("/api/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => alert("Error: " + error));
    });
});

const locationMap = {
    "New York": { lat: 40.7128, lon: -74.0060 },
    "London": { lat: 51.5074, lon: -0.1276 },
    "Beijing": { lat: 39.9042, lon: 116.4074 }
};

function getLatitude(location) {
    return locationMap[location]?.lat || 0;
}

function getLongitude(location) {
    return locationMap[location]?.lon || 0;
}

let map = L.map('map').setView([51.505, -0.09], 5);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let isUpdating = false;

function updateMap() {
    if (isUpdating) return;
    isUpdating = true;

    fetch('/api/flight-data')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (!Array.isArray(data)) {
                throw new Error("Invalid data format received.");
            }
            data.forEach(flight => {
                let latitude = getLatitude(flight.location);
                let longitude = getLongitude(flight.location);

                L.marker([latitude, longitude]).addTo(map)
                    .bindPopup(`Flight: ${flight.flight_id} - Status: ${flight.status}`)
                    .openPopup();
            });
        })
        .catch(error => console.error('Error fetching flight data:', error))
        .finally(() => isUpdating = false);
}

setInterval(updateMap, 5000);
updateMap();

function showCongestion() {
    const output = document.getElementById("output-content");
    output.innerHTML = `
        <h3>Congestion Predictions</h3>
        <p>Predicted congestion zones:</p>
        <ul>
            <li>Zone 1: High congestion (80%)</li>
            <li>Zone 2: Moderate congestion (60%)</li>
            <li>Zone 3: Low congestion (30%)</li>
        </ul>
        <p>Take necessary action to prevent delays.</p>
    `;
}

function rerouteFlight() {
    const output = document.getElementById("output-content");
    output.innerHTML = `
        <h3>Flight Rerouting</h3>
        <p>Flights have been dynamically rerouted:</p>
        <ul>
            <li>Flight A123 redirected to Route B</li>
            <li>Flight B456 redirected to Route C</li>
            <li>Flight C789 rerouted to Route D</li>
        </ul>
    `;
}

function getRealTimeUpdates() {
    const output = document.getElementById("output-content");
    output.innerHTML = `
        <h3>Real-Time Updates</h3>
        <p>Live updates of flights and air traffic conditions:</p>
        <ul>
            <li>Flight A123: On time</li>
            <li>Flight B456: Delayed by 15 minutes</li>
            <li>Flight C789: Departed</li>
        </ul>
    `;
}
