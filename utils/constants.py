from selenium.webdriver.common.by import By

#* URLs
BASE_URL: str = 'https://www.saucedemo.com'

#* Selector By
BY_ID = By.ID
BY_CLASS = By.CLASS_NAME
BY_XPATH = By.XPATH

#* Selector 
ID_USERNAME = "user-name"
ID_PASSWORD = "password"
ID_LOGIN_BUTTON = "login-button"
ID_USERNAME = "user-name"
ID_PASSWORD = "password"
ID_LOGIN_BUTTON = "login-button"
CLASS_LOGIN_LOGO = "login_logo"
ID_LOGIN_CREDENTIALS = "login_credentials"
CSS_ERROR_MESSAGE = "[data-test='error']"
CSS_ERROR_ICON_USER = "#login_button_container > div > form > div:nth-child(1) > svg"
CSS_ERROR_ICON_PASS = "#login_button_container > div > form > div:nth-child(2) > svg"
CLASS_STORE_TITLE = 'title'

LOGIN_ELEMENTS = [
    (By.ID, "login_credentials", [
        "Accepted usernames are:",
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user"
    ]),
    (By.CLASS_NAME, "login_password", [
        "Password for all users:",
        "secret_sauce"
    ]),
]
"""
username_input, /html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input, #user-name
username_xicon, /html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg, #login_button_container > div > form > div:nth-child(1) > svg

password, /html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input, #password
password_xicon, /html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg, #login_button_container > div > form > div:nth-child(2) > svg

error_login /html/body/div/div/div[2]/div[1]/div/div/form/div[3], #login_button_container > div > form > div.error-message-container.error"""


#* Datos de prueba
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"
LOCKED_USER = "locked_out_user"
INVALID_USER = "fake_user"
INVALID_PASS = "wrong_pass"
LANDING_MESSAGE = 'Swag Labs'

INVALID_USERS_SET = [
    ('', '', 'error'),
    ('', 'secret_sauce', 'error'),
    ('standard_user', '', 'error'),
    ('standard_user', 'invalid_pass', 'error'),
    ('invalid_user', '', 'error'),
    ('invalid_user', 'secret_sauce', 'error'),
    ('invalid_user', 'invalid_pass', 'error')
]

VALID_USERS_SET = [
    ("standard_user", "secret_sauce", True),    # login exitoso
    ("locked_out_user", "secret_sauce", False), # bloqueado
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True)
]