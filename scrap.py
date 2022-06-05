from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep

path = "D:/Dwnld/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
browser.get("https://www.amazon.in")
browser.implicitly_wait(30)
browser.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("Samsung Phones")
browser.find_element(By.XPATH, "//span[text()='Samsung']").click()
phonenames = browser.find_elements(By.XPATH, "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
price = browser.find_elements(By.XPATH, "//span[contains(@class,'a-price-whole')]")


for ph in phonenames:
    print(ph.text)

print("*"*30)

for pri in price:
    print(pri.text)

browser.quit()