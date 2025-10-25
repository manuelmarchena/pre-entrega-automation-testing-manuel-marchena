from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utils.checks import assert_element
def assert_elements(
    driver: WebDriver,
    elements: list[tuple[By, str, str | None]],
    context: str = "page"
):
    """
    Verifica múltiples elementos y textos esperados.

    Args:
        driver (WebDriver): Instancia del navegador.
        elements (list): Lista de tuplas (by, selector, expected_text).
        context (str, optional): Contexto de la validación.
    """
    for by, selector, expected_texts in elements:
        if isinstance(expected_texts, list):
            for text in expected_texts:
                assert_element(
                    driver,
                    by,
                    selector,
                    expected_text=text,
                    context=context
                )
        else:
            assert_element(
                driver,
                by,
                selector,
                expected_text=text,
                context=context
            )