import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_agregar_primer_producto_al_carrito(driver):
    LoginPage(driver).abrir().login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver).esperar_carga()

    inventory.agregar_primer_producto()
    assert inventory.obtener_conteo_carrito() == 1
