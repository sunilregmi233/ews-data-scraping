from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

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
# print(html_content)
# text = driver.find_element(By.ID, "root")
# # text.click()
# print(text)



soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)

# table = soup.find_all('t')
table = soup.find('table')
# button = driver.find_element(By.CLASS_NAME, "ion-android-checkbox")
print(table.text)
# button.click()
# rows = table.find_all('tr')
# for row in rows:
#     cells = row.find_all('td')
#     for cell in cells:
#         print(cell.text.strip())  # Do whatever you want with the extracted data
#     print('---')  # Print a separator between rows

# # print(table)

driver.quit()