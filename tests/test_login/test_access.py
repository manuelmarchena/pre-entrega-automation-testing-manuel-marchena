import pytest
from utils.constants import WAITING_TIME, BY_ID, ID_USERNAME, ID_PASSWORD, ID_LOGIN_BUTTON, LANDING_MESSAGE, LOGIN_ELEMENTS, LOGIN_ELEMENTS
from utils.actions import open_loging_page, wait_for_element
from utils.checks import contains_element, page_title_is, contains_texts
from utils.assertions import assert_elements
import time

@pytest.mark.smoke
def test_access(driver):
    open_loging_page(driver)
    assert_elements(driver, LOGIN_ELEMENTS, "login")
    time.sleep(WAITING_TIME)
