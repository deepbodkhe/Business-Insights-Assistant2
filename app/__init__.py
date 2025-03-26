from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder='templates')
    CORS(app)
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app