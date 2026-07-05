from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    #URL de la pagina
    URI = "https://www.saucedemo.com/"

    #Locators
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    #Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Metodos
    def abrir(self):
        self.driver.get(self.URI)
        return self

    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))

        campo.clear()

        campo.send_keys(usuario)

        return self

    def completar_clave(self, clave: str):
        campo = self.driver.find_element(*self._PASS_INPUT)

        campo.clear()

        campo.send_keys(clave)

        return self

    def hacer_click_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()

        return self

    def login_completo(self, usuario, clave):
        self.completar_usuario(usuario)

        self.completar_clave(clave)

        self.hacer_click_login()

        return self

    def esta_error_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))

            return True

        except:
            return False

    def obtener_mensaje_error(self) -> str:
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""