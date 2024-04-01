# cookies before login and after login
#saucedemo.com

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print("cookies before login")
for cookies in driver.get_cookies():
   print(cookies)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


print(" cookies after login")
for cookies in driver.get_cookies():
   print(cookies)
  
driver.quit()



# Pagesource

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

title = driver.title
print ("Tittle: title")

current_url = driver.current_url
print("current_url: current_url")

source = driver.page_source

with open("Webpage_task.txt", "w", encoding="utf-8") as file:
   file.write(source)
  
driver.quit()







