#! Getting Data for Web Scraping

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

driver_class = webdriver.Chrome(options=options)
driver_class.get(
    "https://www.amazon.in/s?k=top+10+fiction+books&adgrpid=58530962626&gad_source=1&hvadid=294150948629&hvdev=c&hvexpln=0&hvlocphy=9061733&hvnetw=g&hvocijid=7811825893588660929--&hvqmt=e&hvrand=7811825893588660929&hvtargid=kwd-310093776697&hydadcr=2402_1727570&mcid=d30db86574da33239acd8611303785b0&tag=googinhydr1-21&ref=pd_sl_1ljz73dtqw_e"
)
print(driver_class.title)
print(driver_class.current_url)
# s-spacing-small
class_ = driver_class.find_elements(By.CLASS_NAME, "s-spacing-small")
# * By.ID        -> Get data by id
# * By.TAG_NAME  -> Get data by Tag
# * By.CSS_SELECTOR -> Get data by css

# print(Book_class)
for classes_ in class_:
    print("\n\n", classes_.text)
    """
    classes_.get_attribute("href")         # any HTML attribute
    classes_.get_attribute("innerHTML")    # raw inner HTML
    classes_.get_attribute("class")
    classes_.is_displayed()
    """
