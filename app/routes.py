from flask import Blueprint, jsonify, request, send_file
from app.core import BusinessInsightsEngine
from app.utils.report_generator import ReportGenerator
import os

main_bp = Blueprint('main', __name__)
engine = BusinessInsightsEngine()

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        query = request.json.get('query', '').strip()
        if not query or len(query) < 5:
            return jsonify({"error": "Query must be at least 5 characters"}), 400
            
        response = engine.process_query(query)
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content', '')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        filepath = ReportGenerator.generate_pdf(content)
        return send_file(filepath, as_attachment=True)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500