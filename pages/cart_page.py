from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test = 'inventory-item-name']")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        """Trae los productos
        agregados al carrito."""

        return self.driver.find_elements(*self._CART_ITEM)

    def obtener_nombres(self):
        """"Obtiene los
        nombres de los
        productos en el carrito."""

        elementos = self.driver.find_elements(*self._PRODUCT_NAME)
        return [e.text for e in elementos] #Es una List Comprehension
    
    def volver_al_inventario(self):
        """Dirige al inventario."""

        self.driver.find_element(*self._CONTINUE_SHOPPING_BUTTON).click()
        from pages import InventoryPage
        return InventoryPage(self.driver)
    