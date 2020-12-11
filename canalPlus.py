from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time

DRIVER_PATH = '/Users/jasonbeedle/Desktop/snaviescraper/chromedriver'

options = Options()
options.page_load_strategy = 'normal'

# Navigate to url
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.canalplus.com/programme-tv/")

time.sleep(8)

# ###################
# Scrolling the page
# ###################
elements = driver.find_elements_by_css_selector(
    "#landing_layers_1 > div > div.guide__body___1xh-z > div.channels___3ppaC > div > div > button")
time.sleep(10)
for elem in elements:
    elem.click()
print("pressing button again now")

time.sleep(10)

print("Need to press it two more times")
elements = driver.find_elements_by_css_selector(
    "#landing_layers_1 > div > div.guide__body___1xh-z > div.channels___3ppaC > div > div > button")
time.sleep(10)
for elem in elements:
    elem.click()
print("This should be the last time")

elements = driver.find_elements_by_css_selector(
    "horizontalScrollerNav___33Spw horizontalScrollerNav--nextButton___JlDng horizontalScrollerNav--active___3aC1p horizontalScrollerNav--displayOnMobile___2ZcX7")
time.sleep(10)
for elem in elements:
    elem.click()

print("Here is your data. Right I am off to sleep then!")
time.sleep(8)

# This is the programme column selector
results = driver.find_element_by_class_name('guide___1Ogg9')

print(results.text)
# Create csv
outfile = open("canalplus.csv", 'a', newline='')
writer = csv.writer(outfile)

driver.quit
