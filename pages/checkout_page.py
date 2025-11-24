from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Proceso de Checkout."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_TITLE = (By.CLASS_NAME, "complete-header")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def completar_formulario(self, nombre, apellido, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(nombre)
        self.driver.find_element(*self.LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        return self

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
        return self

    def click_finish(self):
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BTN)).click()
        return self

    def checkout_completo(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.COMPLETE_TITLE))
            return True
        except:
            return False
