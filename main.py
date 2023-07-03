from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from fastapi.encoders import jsonable_encoder

import db


if __name__ == "__main__":
    db_con = db.db_conn()
    db_flood = db_con[db.db_name]
    db_waterlvl = db_flood[db.db_collection]
    brave_path = '/usr/bin/brave-browser'  # Path to the Brave browser executable
    chromedriver_path = 'chromedriver'  # Path to the ChromeDriver executable

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument('--headless')  # Run Brave in headless mode, no GUI

    service = Service(chromedriver_path)


    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://bipadportal.gov.np/realtime/')

    time.sleep(5)

    rain_click = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > aside.styles_right_Gs3gKM3HFooUsd8CN5dtV > div.styles_right-content-container_1iVqdlST5-qcbQ0ln7tgGV > form > div.styles_real-time-sources-input_WXT1Dn0Af17zV1pLCgm4a.styles_list-selection_2alYshyZHzILhBxplw-Pmv.list-selection.single-segment > div.styles_options_1hBg1mRW-swCWsYh4K61S-.list-selection-options.styles_list-view_UYFRAKwTT4EXYh81gYQY2.list-view > label:nth-child(1) > div").click()
    table = driver.find_element(By.TAG_NAME, "table")
    body = table.find_element(By.TAG_NAME, "tbody")
    tr = body.find_elements(By.TAG_NAME, "tr")

    for h in tr:
        document = {
            "Basin"         : h.find_elements(By.TAG_NAME, 'td')[0].text,
            "Station-name"  : h.find_elements(By.TAG_NAME, 'td')[1].text,
            "Date"          : h.find_elements(By.TAG_NAME, 'td')[2].text,
            "Time"          : h.find_elements(By.TAG_NAME, 'td')[3].text,
            "Water-level"   : h.find_elements(By.TAG_NAME, 'td')[4].text,
            "Status"        : h.find_elements(By.TAG_NAME, 'td')[5].text,
        }
        print(document)
        document = jsonable_encoder(document)
        db_con.flood["waterlvl"].insert_one(document)
    driver.quit()