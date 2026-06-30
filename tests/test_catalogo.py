#2) Navegación y verificación de catalogo
import pytest
from pages import InventoryPage

@pytest.mark.catalogo
@pytest.mark.regression
def test_titulo_inventario(usuario_logueado: InventoryPage):
    assert usuario_logueado.obtener_titulo() == "Products"

@pytest.mark.catalogo
@pytest.mark.regression
def test_productos_visibles(usuario_logueado: InventoryPage):
    assert len(usuario_logueado.obtener_productos()) > 0

@pytest.mark.catalogo
def test_agregar_productos_actualizar_carrito(usuario_logueado: InventoryPage):
    usuario_logueado.agregar_primer_producto()
    assert usuario_logueado.obtener_contador_carrito() == 1

@pytest.mark.catalogo
def test_esta_filtro_visible(usuario_logueado: InventoryPage):
    assert usuario_logueado.esta_filtro_visible()

@pytest.mark.catalogo
def test_esta_menu_visible(usuario_logueado: InventoryPage):
    assert usuario_logueado.esta_menu_visible()

@pytest.mark.catalogo
@pytest.mark.regression
def test_ir_al_carrito(usuario_logueado: InventoryPage):
    usuario_logueado.ir_al_carrito()
    assert "cart.html" in usuario_logueado.driver.current_url

@pytest.mark.catalogo
def test_hacer_logout(usuario_logueado: InventoryPage):
    usuario_logueado.hacer_logout()
    assert "saucedemo.com" in usuario_logueado.driver.current_url