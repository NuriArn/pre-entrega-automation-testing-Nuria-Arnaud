# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Chrome ---
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
   
    os.environ.setdefault("WDM_LOCAL", "1") 
  

    opts = ChromeOptions()
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    opts.add_argument("--incognito")
    # Estabilizadores útiles en Windows/CI:
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--proxy-server=direct://")
    opts.add_argument("--proxy-bypass-list=*")
    

    service = ChromeService(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=opts)

    
    d.set_window_size(1280, 900)
    d.implicitly_wait(2)  
    try:
        yield d
    finally:
        d.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


@pytest.fixture
def login_in_driver(driver, wait):
    """Abre la página, hace login y valida /inventory + textos clave."""
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validaciones post-login
    wait.until(EC.url_contains("/inventory.html"))
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Products"))
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "app_logo"), "Swag Labs"))
    return driver
