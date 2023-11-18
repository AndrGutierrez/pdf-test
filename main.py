from weasyprint import HTML

html = HTML(filename="./index.html", base_url="./")
html.write_pdf('output.pdf')
