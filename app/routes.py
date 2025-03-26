from flask import Blueprint, request, jsonify, send_file
import os
from datetime import datetime
from.report_generator import ReportGenerator  # Assuming you have this module

# Create the blueprint FIRST
main_bp = Blueprint('main', __name__)

# Then define routes
@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        # Ensure reports directory exists
        os.makedirs('reports', exist_ok=True)
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"business_report_{timestamp}.pdf"
        filepath = os.path.join('reports', filename)
        
        # Generate PDF
        ReportGenerator.generate_pdf(content, filepath)
        
        # Verify file was created
        if not os.path.exists(filepath):
            raise Exception("PDF file was not created")
            
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"PDF Generation Error: {str(e)}")  # Log to console
        return jsonify({"error": f"Failed to generate report: {str(e)}"}), 500