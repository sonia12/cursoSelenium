from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\driver actualizados\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
print(driver.title)
print("bienvenidos a selenium")
driver.close()

