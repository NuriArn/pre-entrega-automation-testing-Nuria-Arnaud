import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_logout(driver):
    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).esperar_carga()

    # Abrir menú
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_btn.click()

    # Click en Logout
    wait = WebDriverWait(driver, 10)
    logout_btn = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_btn.click()

    # Validar que vuelve al login page
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    assert "saucedemo.com" in driver.current_url and "inventory" not in driver.current_url
