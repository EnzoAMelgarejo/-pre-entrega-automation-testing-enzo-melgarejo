import pytest
from pages import CartPage, InventoryPage
from utils.datos import leer_json
from utils.logger_config import logger

PRODUCTOS = leer_json('datos/productos.json')

@pytest.mark.carrito
@pytest.mark.regression
def test_contiene_productos(usuario_logueado: InventoryPage):
    logger.info("Agregando primer producto y verificando contenido del carrito")
    cart_page = usuario_logueado.agregar_primer_producto().ir_al_carrito()
    assert len(cart_page.obtener_productos()) > 0


@pytest.mark.carrito
def test_obtener_nombres(usuario_en_carrito: CartPage):
    logger.info("Verificando nombres de productos en el carrito")
    assert usuario_en_carrito.obtener_nombres()


@pytest.mark.carrito
@pytest.mark.regression
def test_continuar_comprando(usuario_en_carrito: CartPage):
    logger.info("Volviendo al inventario desde el carrito")
    inventory_page = usuario_en_carrito.volver_al_inventario()
    assert "inventory.html" in inventory_page.driver.current_url


@pytest.mark.parametrize("producto", PRODUCTOS)
@pytest.mark.carrito
@pytest.mark.regression
def test_agregar_producto_desde_json(usuario_logueado: InventoryPage, producto):
    """
    Test que agrega cada producto del JSON al carrito
    """
    logger.info(f"Agregando producto '{producto}' al carrito desde JSON")
    cart_page = usuario_logueado.agregar_producto_por_nombre(producto).ir_al_carrito()
    assert producto in cart_page.obtener_nombres()
    logger.info(f"Producto '{producto}' confirmado en el carrito")


@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado: InventoryPage):
    """
    Test de smoke que verifica funcionalidad básica del carrito
    """
    logger.info("Ejecutando smoke test de carrito")
    cart_page = usuario_logueado.agregar_primer_producto().ir_al_carrito()
    assert len(cart_page.obtener_productos()) > 0
    logger.info("Smoke test de carrito exitoso")