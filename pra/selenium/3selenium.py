from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

print(driver.title)
print(driver.current_url)

wait = WebDriverWait(driver, 10)

# The form lives inside an iframe — switch into it first
iframe = wait.until(EC.presence_of_element_located((By.ID, "iframeResult")))
driver.switch_to.frame(iframe)

# Now find and fill the form fields
fn = driver.find_element(By.NAME, "fname")
fn.clear()
fn.send_keys("Jon")

ln = driver.find_element(By.NAME, "lname")
ln.clear()
ln.send_keys("Doe")

# Click submit
submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_btn.click()

# Switch back to the main page if needed
driver.switch_to.default_content()
