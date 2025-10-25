from selenium.webdriver.common.by import By
from utils.checks import assert_element

def assert_login_error(driver, expected_text):
    """Valida el mensaje de error al hacer login."""
    assert_element(
        driver,
        By.CSS_SELECTOR,
        "#login_button_container div.error-message-container",
        expected_text=expected_text,
        context="Login - mensaje de error"
    )