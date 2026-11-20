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
    if get_page_with_retries(driver, "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"):
        items = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
        print(f"Found {len(items)} results")
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, 'div.cp-deprecated-bib-brief h3.cp-title').text
            except NoSuchElementException:
                title = ""

        # Authors: find_elements returns an empty list if none exist,
        # so no try block is needed here
            author_elements = item.find_elements(By.CSS_SELECTOR, 'div.cp-deprecated-bib-brief span.cp-author-link')
            authors = "; ".join([a.text for a in author_elements])

            # Format and year
            try:
                format_year = item.find_element(
                    By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary').text
            except NoSuchElementException:
                format_year = ""

            results.append({
                "Title": title,
                "Author": authors,
                "Format-Year": format_year,
            })

        df = pd.DataFrame(results)
        print(df)

# Task 4: Write out the Data
        df.to_csv("assignment8/get_books.csv", index=False)
        with open("assignment8/get_books.json", "w") as file:
            json.dump(results, file)

finally:
    driver.quit()



