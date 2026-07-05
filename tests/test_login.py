import pytest
from pages import LoginPage, InventoryPage
from utils.datos import leer_csv_login
from utils.logger_config import logger

CASOS_LOGIN = leer_csv_login('datos/login.csv')

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
@pytest.mark.login
@pytest.mark.regression
def test_login_exitoso(driver, usuario, clave, descripcion, debe_funcionar):
    """
    Test parametrizado que verifica el login con datos del CSV
    """
    logger.info(f"Probando login '{descripcion}' con usuario={usuario} (se espera éxito={debe_funcionar})")
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(usuario, clave)

    if debe_funcionar:
        assert InventoryPage(driver).obtener_titulo() == "Products"
        logger.info(f"Login exitoso para {usuario}, se accedió a Products")
    else:
        assert login_page.obtener_mensaje_error() != ""
        logger.info(f"Login fallido como se esperaba para {usuario}, mensaje de error mostrado")

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """
    Test de smoke para verificar que al menos un login funciona
    """
    logger.info("Ejecutando smoke test de login con standard_user")
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    assert InventoryPage(driver).obtener_titulo() == "Products"
    logger.info("Smoke test de login exitoso")