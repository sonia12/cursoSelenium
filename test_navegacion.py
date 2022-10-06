import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")

t=2

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://stackoverflow.com/questions/34747341/python-send-keyskeys-tab-types-a-symbol-e004-selenium-firefox")
time.sleep(t)

driver.get("https://www.ingles.com/traductor/buscando")
time.sleep(t)

#driver.back() --> en vez de back usar esta funcion de javacript
driver.execute_script("window.history.go(-1)")

time.sleep(t)

driver.execute_script("window.history.go(-1)") # para volver una pagina
time.sleep(t)
driver.execute_script("window.history.go(2)") # para ir a la pagina 2
time.sleep(t)


driver.close()