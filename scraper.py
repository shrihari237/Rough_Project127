import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(2)

scrape_data = []

def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        soup = BeautifulSoup(browser.page_source,"html.parser")

        bright_star_table = soup.find("table" , attrs ={"class" , "wikitable"} )

        table_body = bright_star_table.find("tbody")

        table_rows = table_body.find_all('tr')

        for row in table_rows:
            table_cols = row.find_all('td')
            print(table_cols)

     
