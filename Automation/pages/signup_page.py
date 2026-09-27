from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    NAME_FIELD = (By.ID, "ob-name")
    EMAIL_FIELD = (By.ID, "ob-email")
    COMPANY_FIELD = (By.ID, "ob-company")
    ROLE_FIELD = (By.ID, "ob-role")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(., 'Continue')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_name(self, name):
        field = self.wait.until(
            EC.visibility_of_element_located(self.NAME_FIELD)
        )
        field.clear()
        field.send_keys(name)

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        field.clear()
        field.send_keys(email)

    def enter_company(self, company):
        field = self.wait.until(
            EC.visibility_of_element_located(self.COMPANY_FIELD)
        )
        field.clear()
        field.send_keys(company)

    def enter_role(self, role):
        field = self.wait.until(
            EC.visibility_of_element_located(self.ROLE_FIELD)
        )
        field.clear()
        field.send_keys(role)

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()