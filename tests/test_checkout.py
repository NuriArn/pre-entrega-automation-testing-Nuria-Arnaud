import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.ui
def test_checkout_completo(driver):
    # Login
    LoginPage(driver).abrir().login("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(driver).esperar_carga()
    inventory.agregar_primer_producto()
    assert inventory.obtener_conteo_carrito() == 1

    # Ir al carrito
    inventory.ir_al_carrito()
    cart = CartPage(driver).esperar_carga()
    assert cart.contar_items() == 1

    # Checkout
    cart.click_checkout()
    checkout = CheckoutPage(driver)
    checkout.completar_formulario("Nuria", "Arnaud", "1234") \
            .click_continue() \
            .click_finish()

    assert checkout.checkout_completo(), "El checkout no llegó a la pantalla de finalización"
