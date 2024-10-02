import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

all_beds = []
url = 'https://www.ikea.com/se/en/cat/beds-bm003/'

driver = webdriver.Chrome()
driver.get(url)


# For page to load
sleep(2) 

# Remove cookies
cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
cookies.click()

show_more_button = driver.find_element(By.XPATH, '//span[@class="plp-btn__label"]/../..')
click_times = 70

# Load more beds to page
for i in range(click_times):
  sleep(0.2)
  show_more_button.click()
  print(f"clicked {i+1}/{click_times} times")

# Appends beds as dicts. If any field == null it is not included
def scrape_products():

  products = driver.find_elements(By.CLASS_NAME, 'plp-fragment-wrapper')

  i = 1
  
  for product in products:
    print("Trying to find a bed")
    try:
      # Slower with XPATH but didn't get .CLASS to work (????)
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
        'price': int(price.replace(' ', '')),
        'springs': springs,
        'firmness': firmness,
      })

    except Exception as e:
      continue
      
    print(f"found {i} beds so far")
    i += 1

scrape_products()
driver.quit()

# Find absolute path so file_path points to the same folder as scraper
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'output.txt')

# One bed per line, many beds are the same model with different dimensions
with open(file_path, 'w', encoding='utf-8') as file:
  for bed in all_beds:
    file.write(f'{bed}\n')