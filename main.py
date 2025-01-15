from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas

from format_tools import get_year_word

excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='wine')


wines = excel_data_df.to_dict(orient='records')

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

timedelta_years = datetime.datetime.now().year - 1920
year_word = get_year_word(timedelta_years)
rendered_page = template.render(
    wines=wines,
    timedelta_years=timedelta_years,
    year_word=year_word
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
