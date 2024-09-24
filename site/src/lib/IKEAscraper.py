from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = 'https://www.ikea.com/se/en/cat/beds-bm003/'

all_beds = []

driver.get(url)

print("Sleeping")
sleep(2)
cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
cookies.click()

button = driver.find_element(By.XPATH, '//span[@class="plp-btn__label"]/../..')

for i in range(75):
  sleep(0.2)
  button.click()
  print(f"clicked {i+1} times")

def scrape_products():

  products = driver.find_elements(By.CLASS_NAME, 'plp-fragment-wrapper')

  i = 1
  
  for product in products:
    try:
      name = product.find_element(By.XPATH, './/span[@class="notranslate plp-price-module__product-name"]').text
      description = product.find_element(By.XPATH, './/span[@class="plp-price-module__description"]').text
      image = product.find_element(By.XPATH, './/img[@class="plp-image plp-product__image"]').get_attribute('src')
      price = product.find_element(By.XPATH, './/span[@class="plp-price__integer"]').text
      springs = product.find_elements(By.XPATH, './/span[@class="plp-text plp-text--body-m plp-icon-text__text"]')[0].text
      firmness = product.find_elements(By.XPATH, './/span[@class="plp-text plp-text--body-m plp-icon-text__text"]')[1].text
      
      all_beds.append({
        'name': name,
        'description': description,
        'image': image,
        'price': price,
        'springs': springs,
        'firmness': firmness,
      })

    except:
      continue
      
    print(f"found {i} beds so far")
    i += 1

scrape_products()

for bed in all_beds:
  print(bed)

driver.quit()