#2) Navegacióny verificacíón de catalogo

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.login import login
from utils.helpers import esperar, driver_create #waiters y login importados como helpers

def test_catalogo():

    driver = driver_create()

    try:

        login(driver) # Login automatizado

        #Espera explicita del catalogo
        esperar(driver, EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        # Validamos nuevamente el titulo
        titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text

        assert titulo == 'Products'

        #Verifica la existencia de productos

        productos = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item')
        print(f'Se encontraron {len(productos)} productos.')
        assert len(productos) > 0

        #Impresion de nombre y valor del producto

        producto0 = productos[0].find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text
        precio0 = productos[0].find_element(By.CSS_SELECTOR, 'div.inventory_item_price').text
        print(f'Nombre: {producto0}, Precio: {precio0}')

        #Localizacíón de la funcionalidad de filtros
        filtro = driver.find_element(By.CLASS_NAME,'product_sort_container')
        assert filtro.is_displayed()

        #Localización de Hamburguer menu 
        menu = driver.find_element(By.ID, 'react-burger-menu-btn')
        assert menu.is_displayed()

    finally:
        driver.quit() #Cierre limpio.