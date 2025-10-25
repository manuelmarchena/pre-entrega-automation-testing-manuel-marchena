import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import( 
    BASE_URL,
    ID_USERNAME, 
    ID_PASSWORD, 
    ID_LOGIN_BUTTON
    )

def open_loging_page(driver: WebDriver):
    """Abre la pagina de login"""
    driver.get(BASE_URL)

def login(user: str, password: str, driver: WebDriver):
    """Realiza el login en la página."""
    driver.get(BASE_URL)

    fill_field(driver, By.ID, ID_USERNAME, user)
    fill_field(driver, By.ID, ID_PASSWORD, password)
    click_element(driver, By.ID, ID_LOGIN_BUTTON)

def wait_for_element(
        driver,
        by: By,
        selector: str,
        timeout: int = 5
    ):
    """Espera hasta que un elemento sea visible y lo devuelve."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, selector)))

def fill_field(driver: WebDriver, by: By, selector: str, text: str):
    """Espera el campo e ingresa texto."""
    element = wait_for_element(driver, by, selector)
    element.clear()
    element.send_keys(text)
    
def click_element(driver: WebDriver, by: By, selector: str):
    """Espera que el elemento esté clickeable y hace click."""
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((by, selector)))
    element.click()