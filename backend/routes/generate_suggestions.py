from flask import Blueprint, request, jsonify
import os
import json

generate_suggestions = Blueprint("generate_suggestions", __name__)

@generate_suggestions.route("/generate-suggestions", methods=["GET"])
def generate():
    email = request.args.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Sanitize email for folder safety
    safe_email = email.replace("@", "_at_").replace(".", "_dot_")
    user_path = os.path.join("static", "user_data", safe_email)

    step1 = {}
    step2 = {}

    try:
        step1_path = os.path.join(user_path, "step1.json")
        step2_path = os.path.join(user_path, "step2.json")

        if os.path.exists(step1_path) and os.path.exists(step2_path):
            with open(step1_path, "r") as f1, open(step2_path, "r") as f2:
                step1 = json.load(f1)
                step2 = json.load(f2)
        else:
            # Fallback dummy data for smoother testing
            step1 = {
                "pieces": "6 pieces",
                "types": ["Dresses", "Tops"]
            }
            step2 = {
                "styleNotes": "elegant and minimal"
            }

        return jsonify({
            "summary": f"{step1.get('pieces', '?')}, including {', '.join(step1.get('types', []))}",
            "fabrics": "Try modal or TENCEL for a sustainable, soft feel.",
            "colors": "Earth tones like olive, beige, and rust.",
            "tips": f"For your vision, emphasize {step2.get('styleNotes', '').lower()} in the design."
        })

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in user files"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
