# conftest.py

import os
import pytest
import pathlib
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import InventoryPage, CartPage

def pytest_html_results_table_header(cells):
    """Añade una columna 'URL'
    justo después de 'Test ID'."""

    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    """Rellena la columna con
    la URL almacenada en el
    atributo 'page_url'"""

    cells.insert(2, getattr(report, 'page_url', '-'))

#Titulo en el reporte vía Hook. No fue aceptado por Github Actions dentro del pytest.ini
def pytest_html_report_title(report):
    report.title = "TalentoLab - Resumen de ejecución"

@pytest.fixture(scope = "function")
def driver():
    """Fixture que proporciona
    un WebDriver configurado."""

    #SETUP: Se configura el driver antes del test.

    firefox_options = Options()

    if os.getenv("CI") == "true":
        firefox_options.add_argument("--headless")
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


# Carpeta donde se guardan las capturas
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            file_name = target / f"{item.name}.png"
            driver.save_screenshot(str(file_name))  # queda guardado en disco

            screenshot_base64 = driver.get_screenshot_as_base64()  # para embeber en el html
            pytest_html = item.config.pluginmanager.getplugin('html')
            extra = getattr(report, 'extras', [])
            extra.append(pytest_html.extras.image(screenshot_base64, name=item.name))
            report.extras = extra

#Fixtures con credenciales de prueba
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

#Teardown para liberar recursos
@pytest.fixture
def usuario_temp():
    r = requests.post('https://jsonplaceholder.typicode.com/posts', json={'title':'tmp', 'body':'test'})

    post_id = r.json()['id']
    yield post_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')