from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(options=options)
driver.get("https://www.geeksforgeeks.org/")
print(driver.title)
print(driver.current_url)


# print("\n\n\n\n", driver.page_source)

driver.back()
driver.forward()
driver.refresh()

driver.quit()
