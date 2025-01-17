import argparse
import os
import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

from format_tools import get_year_word


def main():
    parser = argparse.ArgumentParser(
        description="Скрипт для генерации HTML-страницы с информацией о винах."
    )
    parser.add_argument(
        "--file",
        default=os.getenv("WINE_FILE", "wine3.xlsx"),
        help="Путь к файлу с данными. "
             "По умолчанию используется 'wine3.xlsx' "
             "или значение переменной окружения WINE_FILE."
    )
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Ошибка: Файл '{args.file}' не найден.")
        return

    excel_data_df = pandas.read_excel(args.file, sheet_name='wine')
    excel_data_df = excel_data_df.sort_values(by=['Категория', 'Цена'])

    wines = defaultdict(list)
    for _, row in excel_data_df.iterrows():
        wines[row['Категория']].append({
            'Картинка': row['Картинка'],
            'Категория': row['Категория'],
            'Название': row['Название'],
            'Сорт': row['Сорт'] if pandas.notna(row['Сорт']) else '',
            'Цена': row['Цена'],
            'Акция': row['Акция'] if pandas.notna(row['Акция']) else ''
        })

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


if __name__ == '__main__':
    main()
