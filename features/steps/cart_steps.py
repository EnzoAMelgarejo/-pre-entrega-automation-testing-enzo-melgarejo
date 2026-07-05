from behave import given, when, then
from pages import LoginPage, InventoryPage
from utils.logger_config import logger


@given('que el usuario inicia sesion con standard_user')
def step_login_standard(context):
    logger.info("Iniciando sesion con standard_user para pruebas de carrito")
    login_page = LoginPage(context.driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)


@when('el usuario agrega el producto "{producto}" al carrito')
def step_agregar_producto(context, producto):
    logger.info(f"Agregando producto '{producto}' al carrito")
    context.inventory_page.agregar_producto_por_nombre(producto)


@then('el contador del carrito debe ser "{cantidad}"')
def step_verificar_contador(context, cantidad):
    contador = context.inventory_page.obtener_contador_carrito()
    logger.info(f"Verificando contador del carrito: obtenido={contador}, esperado={cantidad}")
    assert str(contador) == cantidad


@then('el producto "{producto}" debe estar en el carrito')
def step_verificar_producto_en_carrito(context, producto):
    cart_page = context.inventory_page.ir_al_carrito()
    nombres = cart_page.obtener_nombres()
    logger.info(f"Verificando presencia de '{producto}' en el carrito: {nombres}")
    assert producto in nombres