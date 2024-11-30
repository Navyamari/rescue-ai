from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to allow cross-origin requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()  # Get JSON data from the request body
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        text = data.get("text")
        if text:
            # Dummy response for sentiment analysis
            return jsonify({"label": "NEGATIVE", "score": 0.995}), 200
        else:
            return jsonify({"error": "Missing text parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use the PORT environment variable for the port number in production (Heroku)
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    app.run(host="0.0.0.0", port=port, debug=False)  # Disable debug mode in production
