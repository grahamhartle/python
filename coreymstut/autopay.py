from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options
from pathlib import Path

options = webdriver.SafariOptions()
driver = webdriver.Safari(options=options)
service = Service(driver)

driver.get("https://www.apple.com")

driver.quit()
