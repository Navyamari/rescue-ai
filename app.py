import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import os

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Flask app and enable CORS (Cross-Origin Resource Sharing)
app = Flask(__name__)
CORS(app)

# Define the /analyze POST endpoint
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Get the data sent with the POST request (expects JSON)
        data = request.get_json()
        app.logger.debug(f"Received data: {data}")  # Log the received data

        # Check if data is present
        if not data:
            app.logger.error("Invalid JSON received")
            return jsonify({"error": "Invalid JSON"}), 400

        # Extract the 'text' field from the data
        text = data.get("text")
        
        if text:
            # Basic sentiment analysis logic
            if "love" in text.lower() or "happy" in text.lower():
                return jsonify({"label": "POSITIVE", "score": 0.99}), 200
            else:
                return jsonify({"label": "NEGATIVE", "score": 0.995}), 200
        else:
            app.logger.error("Missing 'text' parameter in the request")
            return jsonify({"error": "Missing 'text' parameter"}), 400

    except Exception as e:
        # Log any exceptions that occur
        app.logger.error(f"Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Run the app using Waitress for production environment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use environment variable for port or default to 5000
    app.logger.info(f"Starting server on port {port}")
    serve(app, host="0.0.0.0", port=port)
