import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import os

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing or invalid input"}), 400

        text = data["text"].lower()
        category = ""
        response = {}

        if "accident" in text or "crash" in text:
            category = "Road Accident"
            response = {"action": "Call 911", "resource": "Nearest tow service: ABC Towing"}
        elif "fire" in text or "smoke" in text:
            category = "Fire Incident"
            response = {"action": "Contact firefighters", "resource": "Nearest fire station: XYZ"}
        elif "injury" in text or "hurt" in text:
            category = "Medical Emergency"
            response = {"action": "Call an ambulance", "resource": "Nearest hospital: General Hospital"}
        elif "flood" in text or "storm" in text:
            category = "Natural Disaster"
            response = {"action": "Evacuate", "resource": "Shelter at DEF location"}
        else:
            category = "Uncategorized"
            response = {"action": "Please provide more details", "resource": "None available"}

        return jsonify({"category": category, "response": response}), 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
