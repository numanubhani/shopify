from flask import Flask
from flask_cors import CORS
import os

# Import route blueprints
from routes.save_step1 import save_step1
from routes.save_step2 import save_step2
from routes.save_step3 import save_step3
from routes.generate_suggestions import generate_suggestions
from routes.download_pdf import download_pdf

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all origins during development

# Ensure base user data directory exists
os.makedirs("static/user_data", exist_ok=True)

# Register all blueprints with /api prefix
app.register_blueprint(save_step1, url_prefix="/api")
app.register_blueprint(save_step2, url_prefix="/api")
app.register_blueprint(save_step3, url_prefix="/api")
app.register_blueprint(generate_suggestions, url_prefix="/api")
app.register_blueprint(download_pdf, url_prefix="/api")

# Start the Flask development server
if __name__ == "__main__":
    print("✅ Flask backend is running at http://localhost:5000")
    app.run(debug=True)
