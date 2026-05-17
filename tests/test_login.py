#1) Automatización de login

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import esperar, driver_create #helpers de expected_conditions

def test_login():
    
    driver = driver_create()

    try:

        driver.get("https://saucedemo.com") #Ingreso a la pagina

        #Espera explicita
        username = esperar(
            driver,
            EC.presence_of_element_located((By.ID, "user-name"))
        )

        username.send_keys("standard_user")

        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]' ).click()

        #Validación de inventario

        assert '/inventory.html' in driver.current_url

        #Asercion de titulos
        
        titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
        assert titulo == 'Products'

        logo = driver.find_element(By.CLASS_NAME, "app_logo").text
        assert logo == "Swag Labs"

    finally:
        driver.quit()   #Cierre limpio.