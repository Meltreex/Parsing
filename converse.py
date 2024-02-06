import json
import pandas as pd
#Создаем датасет с названиями столбцов
df = pd.DataFrame(columns=['Название', 'Город', 'Описание', 'Ссылки'])
#Открываем фалй на чтение
with open('brands_list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#Переносим все данные в датасет с помощью метода loc
for key, value in data.items():

    df.loc[len(df.index)] = value
#Преобразуем в csv и xlsx
df.to_csv('output.csv')
df.to_excel('output.xlsx')





