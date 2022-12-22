from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



print("Please type in your username")
username = input()
print("Please type in your password")
password = input()


driver = webdriver.Chrome("chromedriver")

driver.get("https://watch.freecast.com/login/?next=/channels/free")

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/input"))
                                              
finally:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/form/div[2]/div[2]/div[1]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[2]/form/button[1]").click()   








