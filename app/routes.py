from flask import Blueprint, request, jsonify, send_file, render_template
import os
from datetime import datetime
from .report_generator import ReportGenerator

# Define the blueprint (already imported in __init__.py)
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/api')
def api_info():
    return {
        "endpoints": {
            "/analyze": "POST - Process business queries",
            "/download-report": "POST - Generate PDF reports"
        },
        "message": "Business Insights Assistant API",
        "status": "running"
    }

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        query = request.json.get('query', '').strip()
        if not query:
            return jsonify({"error": "Empty query"}), 400
            
        from .core import BusinessInsightsEngine
        engine = BusinessInsightsEngine()
        response = engine.process_query(query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        filename = f"business_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(reports_dir, filename)
        
        ReportGenerator.generate_pdf(content, filepath)
        
        if not os.path.exists(filepath):
            raise Exception("PDF file was not created")
            
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({"error": f"Failed to generate report: {str(e)}"}), 500