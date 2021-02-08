
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images": 2}
#chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_extension("Block-image_v1.1.crx")

option = webdriver.ChromeOptions()
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
chrome_options.experimental_options["prefs"] = chrome_prefs

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

start_time=time.time()
driver=webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.google.com")


print(f"The time taken is  {time.time()-start_time}")

driver.quit()
