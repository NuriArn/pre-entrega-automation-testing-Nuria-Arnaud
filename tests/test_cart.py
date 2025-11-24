
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.ui
def test_agregar_productos_y_ver_en_carrito(driver):
    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).esperar_carga()

    # Agregar 2 productos distintos
    inventory.agregar_producto_por_nombre("Sauce Labs Backpack")
    inventory.agregar_producto_por_nombre("Sauce Labs Bike Light")

    assert inventory.obtener_conteo_carrito() == 2

    inventory.ir_al_carrito()
    cart = CartPage(driver).esperar_carga()

    assert cart.contar_items() == 2
