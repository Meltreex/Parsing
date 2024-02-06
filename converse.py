import json


import pandas as pd

df = pd.DataFrame(columns=['Название', 'Город', 'Описание', 'Ссылки'])

with open('brands_list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for key, value in data.items():

    df.loc[len(df.index)] = value

df.to_csv('output.csv')
df.to_excel('output.xlsx')





