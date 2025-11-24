import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login


@pytest.mark.ui
@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_con_csv(driver, usuario, password, debe_funcionar):
    login_page = LoginPage(driver).abrir()
    login_page.login(usuario, password)

    if debe_funcionar:
        assert login_page.esta_en_inventory(), "Se esperaba login exitoso y no redirigió a inventory."
    else:
        assert not login_page.esta_en_inventory(), "Se esperaba login fallido pero redirigió a inventory."
        assert "Epic sadface" in login_page.obtener_error()
