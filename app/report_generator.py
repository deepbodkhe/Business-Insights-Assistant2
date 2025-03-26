from fpdf import FPDF
from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_pdf(content: str, output_path: str):
        pdf = FPDF()
        pdf.add_page()
        
        # Set better margins (left, top, right)
        pdf.set_margins(10, 10, 10)  
        
        # Use a fixed-width font that handles wrapping better
        pdf.set_font("Courier", size=10)
        
        # Enable automatic page breaks
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add title with proper spacing
        pdf.set_font("Courier", 'B', 14)
        pdf.cell(200, 10, txt="Business Insights Report", ln=1, align='C')
        pdf.set_font("Courier", size=10)
        pdf.cell(200, 5, txt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ln=1, align='C')
        pdf.ln(10)  # Add some vertical space
        
        # Process content with proper line breaks
        for line in content.split('\n'):
            # Handle markdown headers
            if line.startswith('## '):
                pdf.set_font("Courier", 'B', 12)
                pdf.cell(200, 5, txt=line[3:].strip(), ln=1)
                pdf.set_font("Courier", size=10)
            elif line.startswith('### '):
                pdf.set_font("Courier", 'B', 10)
                pdf.cell(200, 5, txt=line[4:].strip(), ln=1)
                pdf.set_font("Courier", size=10)
            else:
                # Handle long lines by splitting them
                max_width = 180  # Adjust based on your page width
                if pdf.get_string_width(line) > max_width:
                    words = line.split(' ')
                    temp_line = ""
                    for word in words:
                        if pdf.get_string_width(temp_line + word) < max_width:
                            temp_line += word + " "
                        else:
                            pdf.multi_cell(0, 5, txt=temp_line)
                            temp_line = word + " "
                    if temp_line:
                        pdf.multi_cell(0, 5, txt=temp_line)
                else:
                    pdf.multi_cell(0, 5, txt=line)
            pdf.ln(2)  # Small vertical spacing between lines
        
        pdf.output(output_path)