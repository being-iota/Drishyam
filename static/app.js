// Get the user's location and display it
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        document.getElementById('location-status').innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Send latitude and longitude to the backend to get the location address
    fetch(`/get_location?lat=${latitude}&long=${longitude}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('location-status').innerHTML = `You are in ${data.location}`;
        });
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            document.getElementById('location-status').innerHTML = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            document.getElementById('location-status').innerHTML = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            document.getElementById('location-status').innerHTML = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            document.getElementById('location-status').innerHTML = "An unknown error occurred.";
            break;
    }
}

// Handle form submission and transaction
document.getElementById('payment-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const recipientName = document.getElementById('recipient-name').value;
    const amount = document.getElementById('amount').value;
    const cardType = document.getElementById('card-type').value;

    // Make sure values are valid
    if (!recipientName || !amount || !cardType) {
        document.getElementById('status').innerHTML = 'Please fill in all fields.';
        return;
    }

    fetch('/submit_transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `recipient_name=${recipientName}&amount=${amount}&card_type=${cardType}`,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerHTML = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('status').innerHTML = 'Transaction Failed.';
    });
});

// Start location fetch on page load
window.onload = getLocation;
