from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB upload limit
    
    # Ensure reports directory exists
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Register blueprints (if any)
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app