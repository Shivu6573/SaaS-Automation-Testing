import pytest

from Automation.utils.driver_factory import get_driver
from Automation.pages.signup_page import SignupPage
from Automation.utils.screenshot import take_screenshot
from Test_Data.signup_data import SIGNUP_DATA


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_signup(driver):

    try:
        driver.get("https://saas.anointedcoder.com/onboarding")

        signup = SignupPage(driver)

        signup.enter_name(SIGNUP_DATA["name"])
        signup.enter_email(SIGNUP_DATA["email"])
        signup.enter_company(SIGNUP_DATA["company"])
        signup.enter_role(SIGNUP_DATA["role"])

        signup.click_continue()

        assert driver.find_element(
            "tag name", "body"
        ).is_displayed()

        take_screenshot(
            driver,
            "signup_passed"
        )

        print("Signup test passed")
        print("Proof screenshot captured")

    except Exception:
        take_screenshot(driver, "signup_failure")
        raise