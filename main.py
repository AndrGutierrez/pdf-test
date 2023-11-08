from urllib import request
from weasyprint import HTML, CSS

html = HTML(filename="./test.html", base_url="./")
css= CSS(filename="./styles.css")
html.write_pdf('output.pdf', css=css)
