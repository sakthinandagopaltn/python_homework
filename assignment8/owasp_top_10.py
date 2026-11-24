import csv

import pandas as pd
import json 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Task 3: Write a Program to Extract this Data
    
results=[]
def get_page_with_retries(driver, url, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            driver.get(url)
            return True  # the page loaded, so stop retrying
        except (TimeoutException, WebDriverException) as e:
            print(f"Attempt {attempt} failed: {type(e).__name__}")
            if attempt < max_attempts:
                wait = 2 * attempt  # wait longer after each failure: 2 seconds, then 4 seconds
                print(f"Waiting {wait} seconds before the next attempt.")
                time.sleep(wait)
    print(f"Giving up on {url} after {max_attempts} attempts.")
    return False

try:
    if get_page_with_retries(driver, "https://owasp.org/www-project-top-ten/"):
        items = driver.find_elements(By.XPATH, '//article//ol/li/a')
        if len(items) != 10:
            print(f"Found {len(items)} links on the assigned page, trying 'https://top10.owasp.org/2025/'")
            driver.get('https://top10.owasp.org/2025/')
            items=driver.find_elements(By.XPATH, '//article//ol/li/a')
        for item in items:
            results.append({
            "Title": item.text.strip(),
            "Link": item.get_attribute("href"),
        })
        print(f"Found {len(results)} vulnerabilities")
        for r in results:
            print(r)
        with open("owasp_top_10.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Title", "Link"])
            writer.writeheader()
            writer.writerows(results)

except WebDriverException as e:
    print(f"Browser error: {type(e).__name__}")

finally:
    driver.quit()
