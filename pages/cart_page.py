from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Carrito de compras (Your Cart)."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_carga(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        self.wait.until(EC.text_to_be_present_in_element(self.TITLE, "Your Cart"))
        return self

    def contar_items(self) -> int:
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
        return self
