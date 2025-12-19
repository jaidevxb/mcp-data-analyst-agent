from fpdf import FPDF
import tempfile

def build_markdown(result):
    return f"""
# MCP Data Analyst Agent Report

## Agent Plan
{result.get("plan", "")}

## Dataset Overview
{result.get("inspection", "")}

## Key Insights
{result.get("explanation", "")}
"""

def export_pdf(markdown_text: str):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)

    for line in markdown_text.split("\n"):
        pdf.multi_cell(0, 6, line)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp.name)
    return tmp.name
