from flask import send_file
from app.utils.report_generator import ReportGenerator
import os

@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content', '')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        # Generate PDF
        filepath = ReportGenerator.generate_pdf(content)
        
        # Send the file directly
        return send_file(
            filepath,
            as_attachment=True,
            download_name='business_report.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500