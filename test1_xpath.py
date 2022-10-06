#  -------------------- elementos seleccionado por Xpath--------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

#nom = driver.find_element_by_xpath("//input[contains(@id,'userName')]")
nom =driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")

nom.send_keys("Sonia")
time.sleep(2)

driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("sonia@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("direccion actual Tiquipaya")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]").send_keys("bolivia tiquipaya")
time.sleep(2)

driver.execute_script("window.scrollTo(0,300)")  #para bajar con el scroll bar
time.sleep(2)

driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").click()
time.sleep(3)

driver.close()

