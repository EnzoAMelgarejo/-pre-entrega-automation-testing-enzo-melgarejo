from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

#Helper de WebDriverWait
def esperar(driver, condicion, tiempo = 10):
    return WebDriverWait(driver, tiempo).until(condicion)


#Helper  de configuración y creación del driver
def driver_create():

    options = Options()
    options.add_argument('--start-maximized')

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)

    return driver