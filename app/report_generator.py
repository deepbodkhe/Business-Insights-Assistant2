from fpdf import FPDF
from datetime import datetime
import os

class ReportGenerator:
    @staticmethod
    def generate_pdf(content: str, output_path: str):
        # Create reports directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        pdf = FPDF()
        pdf.add_page()
        
        # Configure PDF settings
        pdf.set_margins(15, 15, 15)  # Left, Top, Right margins
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=10)
        
        # Add title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Business Insights Report", 0, 1, 'C')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 5, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, 1, 'C')
        pdf.ln(10)
        
        # Process content with smart wrapping
        effective_page_width = pdf.w - 2*pdf.l_margin
        
        for line in content.split('\n'):
            line = line.strip()
            if not line:
                pdf.ln(5)
                continue
                
            # Handle markdown headers
            if line.startswith('## '):
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(0, 10, line[3:].strip(), 0, 1)
                pdf.set_font("Arial", size=10)
                continue
            elif line.startswith('### '):
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 8, line[4:].strip(), 0, 1)
                pdf.set_font("Arial", size=10)
                continue
                
            # Smart text wrapping
            words = line.split(' ')
            current_line = ""
            
            for word in words:
                if pdf.get_string_width(current_line + ' ' + word) < effective_page_width:
                    current_line += ' ' + word if current_line else word
                else:
                    if current_line:
                        pdf.cell(0, 5, current_line, 0, 1)
                    current_line = word
                    
                    if pdf.get_string_width(word) > effective_page_width:
                        for i in range(0, len(word), 20):
                            pdf.cell(0, 5, word[i:i+20], 0, 1)
                        current_line = ""
            
            if current_line:
                pdf.cell(0, 5, current_line, 0, 1)
            
            pdf.ln(2)
        
        pdf.output(output_path)