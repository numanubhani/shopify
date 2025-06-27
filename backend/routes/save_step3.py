from flask import Blueprint, request, jsonify
import os, json

save_step3 = Blueprint("save_step3", __name__)

@save_step3.route("/save-step3", methods=["POST"])  # ✅ DO NOT include /api here
def handle_step3():
    email = request.form.get("email")
    productType = request.form.get("productType")
    feeling = request.form.get("feeling")
    file = request.files.get("image")

    if not email:
        return jsonify({"error": "Missing email"}), 400

    user_path = f"static/user_data/{email}"
    os.makedirs(user_path, exist_ok=True)

    # Save text data
    with open(os.path.join(user_path, "step3.json"), "w") as f:
        json.dump({"productType": productType, "feeling": feeling}, f)

    # Save image (ensure 'images' folder exists)
    if file:
        image_dir = os.path.join(user_path, "images")
        os.makedirs(image_dir, exist_ok=True)
        file.save(os.path.join(image_dir, "product_focus.jpg"))

    return jsonify({"status": "step 3 saved"})
