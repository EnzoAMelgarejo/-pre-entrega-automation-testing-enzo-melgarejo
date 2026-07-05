from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        """Obtiene el
        titulo de la
        pagina del
        inventario.
        """

        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        """Obtiene la
        lista de productos
        disponibles."""

        return self.driver.find_elements(*self._PRODUCTS)

    def agregar_primer_producto(self):
        """Añade el primer
        producto al carrito."""

        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]

        primer_boton.click()

        return self

    def agregar_producto_por_nombre(self, nombre_producto: str):
        """
        Añade un producto al carrito buscándolo por su nombre visible.
        """
        items = self.driver.find_elements(*self._PRODUCTS)
        for item in items:
            nombre = item.find_element(*self._PRODUCT_NAME).text
            if nombre == nombre_producto:
                item.find_element(*self._ADD_BUTTONS).click()
                return self
        raise ValueError(f"Producto '{nombre_producto}' no encontrado")

    def obtener_contador_carrito(self):
        """Obtiene el número
        de productos en el
        carrito."""

        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        
        except:
            return 0

    def esta_menu_visible(self):
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def esta_filtro_visible(self):
        return self.driver.find_element(*self._FILTRO).is_displayed()
        
    def ir_al_carrito(self):
        """Navega a la
        pagina del
        carrito."""

        self.driver.find_element(*self._CART_LINK).click()

        """Importacion lazy
        para evitar dependencias
        ciruclares."""
        from pages.cart_page import CartPage

        return CartPage(self.driver)

    def hacer_logout(self):
        """Cierra la
        sesion del
        usuario."""

        self.driver.find_element(*self._MENU_BUTTON).click()

        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))

        logout_link.click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)