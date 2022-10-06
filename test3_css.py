#  -------------------- elementos seleccionado por css--------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)


#driver.find_element(By.XPATH, "//input[@type='text'and @id='userName']").send_keys("soniac") #-->con selectores multiples
driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("sonia" )
time.sleep(2)


driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("sonia@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("direccion actual Tiquipaya")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#permanentAddress").send_keys("bolivia tiquipaya")
time.sleep(2)

driver.execute_script("window.scrollTo(0,300)")  #para bajar con el scroll bar
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#submit").click()
time.sleep(3)

driver.close()

