from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

y = 21

for index, row in df.iterrows():
    pdf.add_page()

    #Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # lines
    for y in range(20,298,10):
        pdf.line(10, y ,200, y)

    #Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    y1 = 0
    for j in range(row["Pages"] - 1):
        pdf.add_page()

        for i in range(29):
            y1 = y1 + 10
            pdf.line(10, y1, 200, y1)

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)


pdf.output("output_ruled.pdf")

