import requests
from bs4 import BeautifulSoup
from time import sleep

urls = []
beds = []

urls.append('https://www.ikea.com/se/en/cat/beds-bm003/')

for i in range(2, 77):
  url = 'https://www.ikea.com/se/en/cat/beds-bm003/?page=' + str(i)
  urls.append(url)

i = 1
for url in urls: 
  response = requests.get(url)

  if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='plp-fragment-wrapper')

    for product in products:
      try:

        name = product.find('span', class_='notranslate plp-price-module__product-name').get_text()
        description = product.find('span', class_='plp-price-module__description').get_text()
        image = product.find('img').get('src', '')
        price = product.find('span', class_='plp-price__integer').get_text()
        springs = product.find_all('span', class_='plp-text plp-text--body-m plp-icon-text__text')[0].get_text()
        firmness = product.find_all('span', class_='plp-text plp-text--body-m plp-icon-text__text')[1].get_text()
        

        beds.append({
          'name': name,
          'description': description,
          'image': image,
          'price': price,
          'springs': springs,
          'firmness': firmness,
          })


      except:
        continue
  print(str(i) + "/76 completed")
  i += 1

for bed in beds:
  print(bed)
