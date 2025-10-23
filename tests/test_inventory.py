from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        assert len(products) > 0, "No hay productos visibles"

        #Agrega producto al carrito
        products[0].find_element(By.TAG_NAME, 'button').click()

        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,
            "shopping_cart_badge"))
        )
        
        #Verifica que el contador del carrito incrementa 1
        assert badge.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {badge.text}"

        #Verifica que el carrito contiene el producto
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 
            "cart_item"))
        )

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()