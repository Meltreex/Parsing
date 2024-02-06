from bs4 import BeautifulSoup
import json
import requests

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}


url = 'https://russianstreetwear.club'

with open('links_for_brands.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

dict_brands = {}

for item in data:

    response = requests.get(url=url+item, headers=headers)
    src = response.text
    soup = BeautifulSoup(src, 'html.parser')

    name = soup.find(class_='brand-title').text
    city = soup.find(class_='city').text if soup.find(class_='city') else 'None'
    description = soup.find(class_='blockContent').text if soup.find(class_='blockContent') else 'None'
    links = soup.find(class_='links').find_all('a')

    links_list = []
    for i in links:
        href = i['href']
        links_list.append(href)
    dict_brands[name] = [name, city, description, links_list]

with open('brands_list.json', 'w', encoding='utf-8') as file:
    json.dump(dict_brands, file, indent=4, ensure_ascii=False)
