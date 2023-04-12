from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
from bs4 import BeautifulSoup
import numpy as np
import time
import pandas as pd



def main():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    service = Service('./assets/chromedriver')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) ,  options=options)
    # driver = webdriver.Chrome(service=service,  options=options)
    driver.get("https://prism.warehouseservices.com/Identity/Account/Login")
    time.sleep(2)
    driver.maximize_window()


    driver.find_element(By.ID, value='Input_Email').send_keys(Keys.COMMAND + "a")
    driver.find_element(By.ID, value='Input_Email').send_keys(Keys.DELETE)
    driver.find_element(By.ID, value='Input_Email').send_keys('Brad.Salyers@michelin.com')

    driver.find_element(By.ID, value='Input_Password').send_keys(Keys.COMMAND + "a")
    driver.find_element(By.ID, value='Input_Password').send_keys(Keys.DELETE)
    driver.find_element(By.ID, value='Input_Password').send_keys('Wr@nglers1984')

    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(1)

    print('log in successful ....')

    home = driver.current_url
    print('Current URL: ', home)

    # inventory 
    driver.get('https://prism.warehouseservices.com/api/inventory')
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup.prettify())
    content = soup.find('body').text
    json_content = json.loads(content)
    print('JSON content: ', json_content)
    df = pd.DataFrame(json_content)
    df.to_csv('inventory.csv')



if __name__ == '__main__':
    main()