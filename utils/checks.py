import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from utils.actions import wait_for_element

def contains_element(selector: str, by: By, driver: WebDriver) -> bool:
    try:
        driver.find_element(by, selector)
        return True
    except NoSuchElementException:
        return False

def page_title_is(text, driver: WebDriver) -> bool:
    try:
        return text in driver.title 
    except WebDriverException:
        return False

def contains_text(by: By, selector: str, expected_text: str, driver: WebDriver) -> bool:
    try:
        element = driver.find_element(by, selector)
        return expected_text in element.text
    except NoSuchElementException:
        return False
    
def contains_texts(elements: list[tuple], driver: WebDriver) -> bool:
    results = []
    for by, selector, text in elements:
        result = contains_text(by, selector, text, driver)
        if not result:
            return False
    return all(results)

def assert_element(
        driver: WebDriver, 
        by: By, 
        selector: str, 
        expected_text: str | None = None, 
        must_exist: bool = True, 
        context: str = "page"
        ):
    
    """
    Verifica que un elemento exista y, opcionalmente, contenga cierto texto.

    Args:
        driver (WebDriver): Instancia del navegador.
        by (By): Tipo de selector (By.ID, By.CLASS_NAME, etc).
        selector (str): Localizador del elemento.
        expected_text (str, optional): Texto esperado dentro del elemento.
        must_exist (bool, optional): Si es True, falla si no existe el elemento.
        context (str, optional): Texto descriptivo del área o pantalla.

    Uso:
        assert_element(driver, By.ID, "user-name")
        assert_element(driver, By.CSS_SELECTOR, ".error", "Epic sadface")
    """

    try:
        element = wait_for_element(
            driver, 
            by, 
            selector, 
            timeout=5)
        if expected_text:
            actual = element.text.strip()
            assert expected_text in actual, (
                f"Text '{expected_text}' not found in '{context}'"
                f"para el selector '{selector}'. Texto actual: '{actual}'"
                )
    except NoSuchElementException: 
        assert not must_exist, f"Element '{selector}' not found in {context}"