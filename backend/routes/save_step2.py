from flask import Blueprint, request, jsonify
import os, json

save_step2 = Blueprint("save_step2", __name__)

@save_step2.route("/save-step2", methods=["POST"])  # ✅ Remove extra '/api'
def handle_step2():
    email = request.form.get("email")
    brand = request.form.get("brand")
    styleNotes = request.form.get("styleNotes")
    files = request.files.getlist("images")

    user_path = f"static/user_data/{email}"
    os.makedirs(user_path, exist_ok=True)

    with open(os.path.join(user_path, "step2.json"), "w") as f:
        json.dump({"brand": brand, "styleNotes": styleNotes}, f)

    image_path = os.path.join(user_path, "images")
    os.makedirs(image_path, exist_ok=True)

    for i, file in enumerate(files[:3]):
        file.save(os.path.join(image_path, f"inspiration_{i + 1}.jpg"))

    return jsonify({"status": "saved"})
