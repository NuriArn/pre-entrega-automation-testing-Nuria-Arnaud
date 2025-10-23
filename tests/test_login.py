from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente a la url inventario"
        
        print("Loggin exitoso y validado correctamente")
    
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()