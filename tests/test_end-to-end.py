import pytest
from pages import LoginPage, InventoryPage
from utils.logger_config import logger

@pytest.mark.regression
def test_flujo_completo(driver, credenciales_validas):
    # Login
    logger.info(f"Iniciando flujo E2E con usuario={credenciales_validas['usuario']}")
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(
        credenciales_validas["usuario"],
        credenciales_validas["clave"]
    )
    logger.info("Login realizado")

    # Inventario
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products"
    logger.info("Acceso a Products confirmado")

    # Agregar producto y ir al carrito
    cart_page = inventory_page.agregar_primer_producto().ir_al_carrito()
    assert len(cart_page.obtener_productos()) > 0
    logger.info(f"Producto agregado, carrito con {len(cart_page.obtener_productos())} producto(s)")

    # Volver al inventario
    inventory_page = cart_page.volver_al_inventario()
    assert "inventory.html" in inventory_page.driver.current_url
    logger.info("Regreso al inventario confirmado")

    # Logout
    inventory_page.hacer_logout()
    assert "saucedemo.com" in inventory_page.driver.current_url
    logger.info("Logout realizado, flujo E2E completo")