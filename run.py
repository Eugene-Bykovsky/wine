import pandas
from pprint import pprint
from collections import defaultdict

excel_data_df = pandas.read_excel('wine2.xlsx', sheet_name='wine')
grouped_data = defaultdict(list)
for _, row in excel_data_df.iterrows():
    grouped_data[row['Категория']].append({
        'Картинка': row['Картинка'],
        'Категория': row['Категория'],
        'Название': row['Название'],
        'Сорт': row['Сорт'] if pandas.notna(row['Сорт']) else '',
        'Цена': row['Цена'],
    })
grouped_data = dict(grouped_data)

pprint(grouped_data)
