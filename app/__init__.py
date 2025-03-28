from flask import Flask, Blueprint
from flask_cors import CORS

# Initialize the blueprint
main_bp = Blueprint('main', __name__)

def create_app():
    app = Flask(__name__, template_folder='templates')
    CORS(app)
    
    # Import routes after app creation to avoid circular imports
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app