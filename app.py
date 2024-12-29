from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
import random

app = Flask(__name__)

# Mockup of a user database (just for testing)
user_balance = 1000  # Mock user balance

# Initialize geolocator for location
geolocator = Nominatim(user_agent="drishyam_app")

# Route to serve the payment page (index.html)
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route to handle the location request from frontend
@app.route('/get_location')
def get_location():
    try:
        lat = float(request.args.get('lat'))
        long = float(request.args.get('long'))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid latitude or longitude"})

    location = geolocator.reverse((lat, long), language='en')
    if location:
        location_address = location.address
        # You can add logic to simulate specific locations for testing purposes
        if "Delhi" in location_address:
            return jsonify({"location": "You are in Delhi right now."})
        return jsonify({"location": location_address})
    else:
        return jsonify({"location": "Location not found"})

# Route to handle the form submission and transaction
@app.route('/submit_transaction', methods=['POST'])
def submit_transaction():
    global user_balance  # Declare user_balance as global to modify it

    # Extract data from the frontend form submission
    recipient_name = request.form.get('recipient_name')
    amount = float(request.form.get('amount'))
    card_type = request.form.get('card_type')

    # Simulate user confirmation of payment method
    if card_type not in ["credit", "debit"]:
        return jsonify({
            "message": "Invalid card type. Please choose 'credit' or 'debit'."
        })

    # Simulate transaction processing
    if user_balance >= amount:
        # Deduct amount from the user's balance
        user_balance -= amount
        return jsonify({
            "message": f"Transaction Completed! You paid {recipient_name} {amount}. Remaining balance: {user_balance}."
        })
    else:
        # Insufficient funds
        return jsonify({
            "message": "Insufficient funds. Transaction failed."
        })

# Route to handle the voice command for payment amount
@app.route('/voice_command', methods=['POST'])
def voice_command():
    try:
        # Assuming the voice input is sent as JSON (For example: { "command": "100" })
        command = request.json.get('command')
        if command:
            amount = float(command)
            return jsonify({"message": f"Amount received: {amount}. Please choose 'credit' or 'debit' to continue."})
        else:
            return jsonify({"message": "Voice command is empty."})
    except ValueError:
        return jsonify({"message": "Invalid amount in the voice command."})

if __name__ == '__main__':
    app.run(debug=True)
