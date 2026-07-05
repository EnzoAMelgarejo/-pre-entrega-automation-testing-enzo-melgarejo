import pytest
from pages import InventoryPage
from utils.logger_config import logger

@pytest.mark.catalogo
@pytest.mark.regression
def test_titulo_inventario(usuario_logueado: InventoryPage):
    logger.info("Verificando título de la página de inventario")
    assert usuario_logueado.obtener_titulo() == "Products"


@pytest.mark.catalogo
@pytest.mark.regression
def test_productos_visibles(usuario_logueado: InventoryPage):
    logger.info("Verificando que hay productos visibles en el inventario")
    assert len(usuario_logueado.obtener_productos()) > 0


@pytest.mark.catalogo
def test_agregar_productos_actualizar_carrito(usuario_logueado: InventoryPage):
    logger.info("Agregando primer producto y verificando contador de carrito")
    usuario_logueado.agregar_primer_producto()
    assert usuario_logueado.obtener_contador_carrito() == 1


@pytest.mark.catalogo
def test_esta_filtro_visible(usuario_logueado: InventoryPage):
    logger.info("Verificando visibilidad del filtro")
    assert usuario_logueado.esta_filtro_visible()


@pytest.mark.catalogo
def test_esta_menu_visible(usuario_logueado: InventoryPage):
    logger.info("Verificando visibilidad del menú")
    assert usuario_logueado.esta_menu_visible()


@pytest.mark.catalogo
@pytest.mark.regression
def test_ir_al_carrito(usuario_logueado: InventoryPage):
    logger.info("Navegando al carrito desde el inventario")
    usuario_logueado.ir_al_carrito()
    assert "cart.html" in usuario_logueado.driver.current_url


@pytest.mark.catalogo
def test_hacer_logout(usuario_logueado: InventoryPage):
    logger.info("Ejecutando logout desde el inventario")
    usuario_logueado.hacer_logout()
    assert "saucedemo.com" in usuario_logueado.driver.current_url