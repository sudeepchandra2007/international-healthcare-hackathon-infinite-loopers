import os
import json
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from api.gemini_api import analyze_with_gemini

app = Flask(__name__)
UPLOAD_FOLDER = "webapp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

STATS_FILE = "webapp/stats.json"

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return []

def save_stats(new_entry):
    stats = load_stats()
    stats.insert(0, new_entry)  
    with open(STATS_FILE, "w") as f:
        json.dump(stats[:10], f, indent=4)  

@app.route("/")
def index():
    return render_template("index.html", statistics=load_stats())

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image_file = request.files["file"]

    if image_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    print(f"🔹 DEBUG: File received: {image_file.filename}")

    analysis_result = analyze_with_gemini(image_file)
    print(f"🔹 DEBUG: AI Analysis Result: {analysis_result}")

    if analysis_result:
        result_data = {
            "findings": analysis_result.get("findings", "Not available"),
            "concerns": analysis_result.get("concerns", "Not specified"),
            "probability": f"{analysis_result.get('probability', '0%')}",
            "cancer_type": analysis_result.get("cancer_type", "Not specified"),
        }
        save_stats(result_data) 
        return jsonify(result_data)

    return jsonify({"error": "Analysis failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
