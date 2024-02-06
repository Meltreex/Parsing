from bs4 import BeautifulSoup
import lxml
import requests
import json

#Здесь требуется указать Accept и User-Agent вашего браузера
headers = {
    'Accept': '',
    'User-Agent': ''
}


url = 'https://russianstreetwear.club'
#создаем запрос к сайту
response = requests.get(url=url, headers=headers)

src = response.text

soup = BeautifulSoup(src, 'html.parser')
#Получаем html страницу с ссылками 
letter = soup.find_all('a', class_='Card_link__37XsF')
#Пустой список для дальнейшего сохранения в json файл
list_brands = []
#Забираем все ссылки и добавляем в список
for item in letter:
    href = item['href']
    list_brands.append(href)
#Корректируем список(на сайте появляются новые бренды, они заносятся в основной список, а также появляются в начале, 
#4 - означает 4 новых бренда. Данная цифра учитывается по мере обновления сайта)
list_brands = list_brands[4:]
#Преобразуем в json формат
with open('links_for_brands.json', 'w', encoding='utf-8') as file:
    json.dump(list_brands, file, indent=4, ensure_ascii=False)


