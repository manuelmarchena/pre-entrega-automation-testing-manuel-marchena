import pytest
from utils.actions import login
from utils.checks import assert_element
from utils.constants import( 
    VALID_USER, 
    VALID_PASS, 
    BY_CLASS,
    CLASS_STORE_TITLE
)

@pytest.mark.smoke
@pytest.mark.login
def test_login_success(driver):
    """Verifica que el login con credenciales válidas funcione correctamente."""
    login(VALID_USER, VALID_PASS, driver)
    assert_element(
        driver,
        BY_CLASS,
        CLASS_STORE_TITLE,
        expected_text="Products",
        context="Página de Inventario")
    

def test_login_failed(driver, invalid_user):
    username, password, expected_error = invalid_user
    login(username, password, driver)
    assert expected_error in driver.page_source