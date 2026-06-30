#4) Flujo completo end-to-end
import pytest
from pages import LoginPage, InventoryPage

@pytest.mark.regression
def test_flujo_completo(driver, credenciales_validas):
    # Login
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(
        credenciales_validas["usuario"],
        credenciales_validas["clave"]
    )
    
    # Inventario
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products"
    
    # Agregar producto y ir al carrito
    cart_page = inventory_page.agregar_primer_producto().ir_al_carrito()
    assert len(cart_page.obtener_productos()) > 0
    
    # Volver al inventario
    inventory_page = cart_page.volver_al_inventario()
    assert "inventory.html" in inventory_page.driver.current_url
    
    # Logout
    inventory_page.hacer_logout()
    assert "saucedemo.com" in inventory_page.driver.current_url