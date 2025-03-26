@main_bp.route('/download-report', methods=['POST'])
def download_report():
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400
            
        # Use absolute path for Render deployment
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