from flask import Blueprint, request, jsonify, send_file
import os
from datetime import datetime
from app.report_generator import ReportGenerator

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return {
        "status": "running",
        "message": "Business Insights Assistant API",
        "endpoints": {
            "/analyze": "POST - Process business queries",
            "/download-report": "POST - Generate PDF reports"
        }
    }

@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
            
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        os.makedirs('reports', exist_ok=True)
        filename = f"business_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join('reports', filename)
        
        ReportGenerator.generate_pdf(content, filepath)
        
        if not os.path.exists(filepath):
            return jsonify({"error": "PDF generation failed"}), 500
            
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({"error": f"Report generation failed: {str(e)}"}), 500