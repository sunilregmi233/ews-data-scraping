from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime


brave_path = '/usr/bin/brave-browser'  # Path to the Brave browser executable
chromedriver_path = 'chromedriver'  # Path to the ChromeDriver executable

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument('--headless')  # Run Brave in headless mode, no GUI

service = Service(chromedriver_path)


driver = webdriver.Chrome(service=service, options=options)

driver.get('https://bipadportal.gov.np/realtime/')

time.sleep(10)


html_content = driver.page_source




soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table')
print(table.text)


driver.quit()