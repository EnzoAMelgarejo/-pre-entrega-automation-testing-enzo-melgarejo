#3) Interacción con productos
import pytest
from pages import CartPage, InventoryPage

@pytest.mark.carrito
@pytest.mark.regression
def test_contiene_productos(usuario_logueado: InventoryPage):
    cart_page = usuario_logueado.agregar_primer_producto().ir_al_carrito()
    assert len(cart_page.obtener_productos()) > 0

@pytest.mark.carrito
def test_obtener_nombres(usuario_en_carrito: CartPage):
    assert usuario_en_carrito.obtener_nombres()

@pytest.mark.carrito
@pytest.mark.regression
def test_continuar_comprando(usuario_en_carrito: CartPage):
    inventory_page = usuario_en_carrito.volver_al_inventario()
    assert "inventory.html" in inventory_page.driver.current_url