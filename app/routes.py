from flask import Blueprint, jsonify, request, render_template
from app.core import BusinessInsightsEngine

main_bp = Blueprint('main', __name__)
engine = BusinessInsightsEngine()

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        query = request.json.get('query', '').strip()
        if not query:
            return jsonify({"error": "Empty query"}), 400
            
        response = engine.process_query(query)
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500