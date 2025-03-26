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
            "generate_report": "/download-report (POST)"
        }
    }

@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        os.makedirs('reports', exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"business_report_{timestamp}.pdf"
        filepath = os.path.join('reports', filename)
        
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
        print(f"PDF Generation Error: {str(e)}")
        return jsonify({"error": f"Failed to generate report: {str(e)}"}), 500