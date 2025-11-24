from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object para la pantalla de login de Saucedemo."""

    # Locators
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self):
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.visibility_of_element_located(self.USER_INPUT))
        return self

    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self.USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_password(self, password: str):
        campo = self.driver.find_element(*self.PASS_INPUT)
        campo.clear()
        campo.send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        return self  # permite method chaining

    def login(self, usuario: str, password: str):
        """Flujo completo de login."""
        return self.completar_usuario(usuario).completar_password(password).click_login()

    def obtener_error(self) -> str:
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
        except Exception:
            return ""

    def esta_en_inventory(self) -> bool:
        return "/inventory.html" in self.driver.current_url
