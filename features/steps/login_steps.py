from behave import given, when, then
from behave import use_step_matcher
from pages import LoginPage, InventoryPage
from utils.logger_config import logger


@given('que el usuario abre la pagina de login')
def step_abrir_login(context):
    logger.info("Abriendo la pagina de login")
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()


use_step_matcher("re")

@when('el usuario ingresa el usuario "(?P<usuario>.*)" y la clave "(?P<clave>.*)"')
def step_login_completo(context, usuario, clave):
    logger.info(f"Ingresando credenciales usuario={usuario}")
    context.login_page.login_completo(usuario, clave)

use_step_matcher("parse")


@then('debe ser redirigido al inventario')
def step_redireccion_exitosa(context):
    inventory_page = InventoryPage(context.driver)
    resultado = inventory_page.obtener_titulo()
    logger.info(f"Verificando redireccion al inventario, titulo obtenido={resultado}")
    assert resultado == "Products"


@then('debe ver un mensaje de error visible')
def step_mensaje_error(context):
    mensaje = context.login_page.obtener_mensaje_error()
    logger.info(f"Verificando mensaje de error visible: '{mensaje}'")
    assert mensaje != ""