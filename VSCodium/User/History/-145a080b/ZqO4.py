from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("https://seoschmiede.at/en/aitools/chatgpt-tool/")
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/p[4]/a').click()
time.sleep(1)
text_area = driver.find_element(By.XPATH, '/html/body/article/div[2]/div/div[1]/div/div[5]/div/div/div/div[2]/div/main/form/div/div/textarea')
# driver.execute_script("arguments[0].scrollIntoView(true);", text_area)
text_area.click()

text_area.send_keys("Merhaba")
text_area.send_keys(Keys.ENTER)


time.sleep(2)
response = driver.find_elements(By.CSS_SELECTOR, '#chat-history > div:nth-child(3)')
print(response[-1].text)