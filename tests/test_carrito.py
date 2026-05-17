#3) Interacción con productos

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import driver_create, esperar
from utils.login import login


def test_carrito():

    driver = driver_create()

    try:

        # Login automatizado
        login(driver)

        # Espera catálogo
        esperar(driver,EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        productos = driver.find_elements(By.CSS_SELECTOR,'div.inventory_item')

        # Agregar primer producto
        productos[0].find_element(By.TAG_NAME, 'button').click()

        # Guardar nombre y precio
        producto0 = productos[0].find_element(By.CSS_SELECTOR,'div.inventory_item_name').text

        precio0 = productos[0].find_element(By.CSS_SELECTOR,'div.inventory_item_price').text

        print(f'Nombre: {producto0}, Precio: {precio0}')

        # Verificar badge carrito
        badge = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text

        assert badge == '1'

        # Ir al carrito
        driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()

        # Espera carrito
        esperar(driver,EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

        # Validar URL carrito
        assert '/cart.html' in driver.current_url

        # Validar producto agregado
        item_carrito = driver.find_element(By.CSS_SELECTOR,'.inventory_item_name').text

        assert item_carrito == producto0

        print('Producto en carrito OK ->', item_carrito)

    finally:

        driver.quit()