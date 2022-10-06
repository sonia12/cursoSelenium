#  --------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)



driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("sonia" + Keys.TAB + "sonia@gmail.com" + Keys.TAB + "direccion actual tiquipaya" + Keys.TAB + "bolivia Tiquipaya" + Keys.TAB + Keys.ENTER)

time.sleep(2)
driver.find_element(By.XPATH, "//li[@class='btn btn-light '][contains(.,'Check Box')]").click()
time.sleep(3)


driver.close()

