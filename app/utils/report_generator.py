from fpdf import FPDF
from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_pdf(content: str, filename: str = "business_insights.pdf") -> str:
        """Generate PDF report from analysis content"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Add title
        pdf.cell(200, 10, txt="Business Insights Report", ln=1, align='C')
        pdf.cell(200, 10, txt=datetime.now().strftime("%Y-%m-%d"), ln=1, align='C')
        pdf.ln(10)
        
        # Add content
        for line in content.split('\n'):
            if line.startswith('## '):
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(200, 10, txt=line[3:].strip(), ln=1)
                pdf.set_font("Arial", size=12)
            elif line.startswith('### '):
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(200, 10, txt=line[4:].strip(), ln=1)
                pdf.set_font("Arial", size=12)
            else:
                pdf.multi_cell(0, 10, txt=line.strip())
        
        filepath = f"reports/{filename}"
        pdf.output(filepath)
        return filepath