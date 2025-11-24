from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object para la pantalla de productos (inventory)."""

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    # Selector universal compatible con TODAS las versiones de Saucedemo
    ADD_TO_CART_BTNS = (
        By.CSS_SELECTOR,
        "button[data-test^='add-to-cart'], button.btn_inventory, button.btn.btn_primary.btn_small.btn_inventory"
    )

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_carga(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        self.wait.until(EC.text_to_be_present_in_element(self.TITLE, "Products"))
        self.wait.until(EC.presence_of_all_elements_located(self.INVENTORY_ITEMS))
        return self

    def agregar_primer_producto(self):
        # presence_of_all_elements funciona mejor que visibility para este UI
        botones = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_TO_CART_BTNS)
        )
        if not botones:
            raise AssertionError("No se encontraron botones de 'Add to cart'.")
        botones[0].click()
        return self

    def agregar_producto_por_nombre(self, nombre: str):
        items = self.wait.until(EC.presence_of_all_elements_located(self.INVENTORY_ITEMS))
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if title.lower() == nombre.lower():
                item.find_element(By.CSS_SELECTOR, "button").click()
                return self
        raise AssertionError(f"No se encontró el producto '{nombre}'")

    def obtener_conteo_carrito(self) -> int:
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        try:
            return int(badges[0].text)
        except ValueError:
            return 0

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()
        return self
