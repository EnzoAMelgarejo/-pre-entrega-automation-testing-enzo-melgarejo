# conftest.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import InventoryPage, CartPage

@pytest.fixture(scope = "function")
def driver():
    """Fixture que proporciona
    un WebDriver configurado."""

    #SETUP: Se configura el driver antes del test.

    firefox_options = Options()

    # firefox_options.add_argument("--headless") #Para CI/CD
    firefox_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # En esta instancia python corre el test, otorgandole el driver configurado.
    yield driver

    #TEARDOWN: Se ejecuta despues del test, pase lo que pase.

    time.sleep(1) #Para ver el resultado final
    driver.quit()

@pytest.fixture
def credenciales_validas():
    return {"usuario": "standard_user", "clave": "secret_sauce"}

@pytest.fixture
def credenciales_invalidas():
    return {"usuario": "standard_user", "clave": "clave_incorrecta"}

@pytest.fixture
def usuario_bloqueado():
    return {"usuario": "locked_out_user", "clave": "secrete_sauce"}

@pytest.fixture
def usuario_logueado(driver, credenciales_validas):
    from pages import LoginPage, InventoryPage
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(
        credenciales_validas["usuario"],
        credenciales_validas["clave"]
    )
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))
    return InventoryPage(driver)

@pytest.fixture
def usuario_en_carrito(usuario_logueado: InventoryPage) -> CartPage:
    return usuario_logueado.agregar_primer_producto().ir_al_carrito()