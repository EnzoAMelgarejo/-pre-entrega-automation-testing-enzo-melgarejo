#1) Automatización de login
import pytest
from pages import LoginPage, InventoryPage

@pytest.mark.parametrize("usuario,password,deberia_funcionar", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
])
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.regression
def test_login_exitoso(driver, usuario, password, deberia_funcionar):
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(usuario, password)
    
    if deberia_funcionar:
        assert InventoryPage(driver).obtener_titulo() == "Products"
    else:
        assert login_page.obtener_mensaje_error() != ""