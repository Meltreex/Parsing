from bs4 import BeautifulSoup
import lxml
import requests
import json


headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}


url = 'https://russianstreetwear.club'

response = requests.get(url=url, headers=headers)

src = response.text

soup = BeautifulSoup(src, 'html.parser')
#Парсим все ссылки на магазины одежд
letter = soup.find_all('a', class_='Card_link__37XsF')

list_brands = []

for item in letter:
    href = item['href']
    list_brands.append(href)

list_brands = list_brands[4:]

with open('links_for_brands.json', 'w', encoding='utf-8') as file:
    json.dump(list_brands, file, indent=4, ensure_ascii=False)


