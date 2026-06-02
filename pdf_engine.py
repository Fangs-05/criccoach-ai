import textwrap
from fpdf import FPDF
from datetime import datetime

def write_safe_multiline(pdf, text, max_chars=80):
    """
    Bypasses FPDF's buggy multi_cell wrapper by manually wrapping text into safe lines.
    This makes the Not enough horizontal space error physically impossible.
    """
    if not text:
        return
    
    # 1. Strip weird characters that confuse the PDF engine
    text = str(text).encode('ascii', 'ignore').decode('ascii')
    
    # 2. Split by any natural paragraphs the AI created
    paragraphs = text.split('\n')
    
    for para in paragraphs:
        # 3. Use standard Python to wrap lines safely
        lines = textwrap.wrap(para, width=max_chars, break_long_words=True)
        
        # 4. Print line-by-line using standard cells instead of multi_cell
        for line in lines:
            pdf.cell(0, 6, line, ln=True)

def generate_pdf_report(player_name, overall_score, shot_type, report_data):
    pdf = FPDF()
    pdf.add_page()
    
    # Header styling (SRH Orange accent)
    pdf.set_fill_color(242, 101, 34)
    pdf.rect(0, 0, 210, 25, 'F')
    
    pdf.set_font("Helvetica", 'B', 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(6)
    pdf.cell(0, 10, "CricCoach AI - Session Report", ln=True, align='C')
    
    # Player Meta Data
    pdf.ln(15)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 8, f"Player: {player_name}", ln=True)
    
    pdf.set_font("Helvetica", '', 11)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%B %d, %Y - %I:%M %p')}", ln=True)
    pdf.cell(0, 8, f"Shot Analyzed: {shot_type}", ln=True)
    
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 8, f"Overall Efficiency Score: {overall_score}/100", ln=True)
    
    # Coach's Assessment
    pdf.ln(8)
    pdf.set_font("Helvetica", 'B', 14)
    pdf.set_text_color(242, 101, 34)
    pdf.cell(0, 10, "Coach's Assessment", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", '', 11)
    
    # Using our custom safe text writer instead of multi_cell
    write_safe_multiline(pdf, report_data['opening'])
    pdf.ln(2)
    write_safe_multiline(pdf, report_data['closing'])
    
    # Priority Corrections & Drills
    if report_data['corrections']:
        pdf.ln(8)
        pdf.set_font("Helvetica", 'B', 14)
        pdf.set_text_color(242, 101, 34)
        pdf.cell(0, 10, "Priority Corrections & Drills", ln=True)
        pdf.set_text_color(0, 0, 0)
        
        for c in report_data['corrections']:
            pdf.set_font("Helvetica", 'B', 11)
            # Standard cell for headers
            pdf.cell(0, 8, f"{c['area']} (Measured: {c['your_angle']}  | Ideal: {c['ideal']})", ln=True)
            
            pdf.set_font("Helvetica", '', 11)
            # --- THE FIX: Using the safe writer for the dynamic AI feedback ---
            write_safe_multiline(pdf, f"Focus: {c['problem']}")
            write_safe_multiline(pdf, f"Drill: {c['drill']}")
            pdf.ln(4)
            
    return pdf.output()