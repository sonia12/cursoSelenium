
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")


driver.get("https://demoqa.com/text-box") # no encontramos el elemento emergente para probar
driver.maximize_window()

t= 3

btn= WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.XPATH,""))
btn.click()

time.sleep(t)

driver.close()

