# backend/routes/save_step1.py
from flask import Blueprint, request, jsonify
import os, json

save_step1 = Blueprint("save_step1", __name__)

@save_step1.route("/save-step1", methods=["POST"])
def save_step1_data():
    data = request.get_json()
    email = data.get("email")
    
    if not email:
        return jsonify({"error": "Email is required"}), 400

    user_path = f"static/user_data/{email}"
    os.makedirs(user_path, exist_ok=True)

    with open(os.path.join(user_path, "step1.json"), "w") as f:
        json.dump(data, f)

    return jsonify({"message": "Step 1 saved successfully."})
