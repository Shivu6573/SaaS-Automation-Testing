from Automation.utils.screenshot import take_screenshot
from Automation.utils.driver_factory import get_driver
from Automation.pages.signup_page import SignupPage
from Test_Data.signup_data import SIGNUP_DATA

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_subscription_plans():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # Open application
        driver.get("https://saas.anointedcoder.com/onboarding")

        # Complete signup
        signup = SignupPage(driver)

        signup.enter_name(SIGNUP_DATA["name"])
        signup.enter_email(SIGNUP_DATA["email"])
        signup.enter_company(SIGNUP_DATA["company"])
        signup.enter_role(SIGNUP_DATA["role"])

        signup.click_continue()

        # Open Billing
        driver.get("https://saas.anointedcoder.com/app/billing")

        # Open Change Plan
        change_plan = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Change Plan')]")
            )
        )

        change_plan.click()

        # Locate Change Plan dialog
        dialog = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='dialog']")
            )
        )

        # Verify all plans
        assert dialog.find_element(
            By.XPATH, ".//*[normalize-space()='Free']"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[normalize-space()='Starter']"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[normalize-space()='Growth']"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[normalize-space()='Scale']"
        ).is_displayed()

        # Verify prices
        assert dialog.find_element(
            By.XPATH, ".//*[contains(normalize-space(), '$0/mo')]"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[contains(normalize-space(), '$29/mo')]"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[contains(normalize-space(), '$99/mo')]"
        ).is_displayed()

        assert dialog.find_element(
            By.XPATH, ".//*[contains(normalize-space(), '$299/mo')]"
        ).is_displayed()

        print("Free plan verified: $0/month")
        print("Starter plan verified: $29/month")
        print("Growth plan verified: $99/month")
        print("Scale plan verified: $299/month")

        # Check current plan
        growth_current = dialog.find_elements(
            By.XPATH,
            ".//*[normalize-space()='Growth']/following::*[normalize-space()='Current'][1]"
        )

        if growth_current:
            print("Growth is already the current plan")

        else:
            # Select Growth
            growth = dialog.find_element(
                By.XPATH,
                ".//*[normalize-space()='Growth']"
            )

            growth.click()

            print("Growth plan selected")

            # Confirm upgrade
            confirm_upgrade = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[@role='dialog']//button[contains(., 'Confirm Demo Upgrade')]"
                    )
                )
            )

            confirm_upgrade.click()

            print("Demo upgrade confirmed")

        # Close Change Plan dialog if still open
        try:
            close_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[@role='dialog']//button[contains(., 'Keep Current Plan')]"
                    )
                )
            )

            close_button.click()

        except:
            pass

        # Verify billing page contains Growth and $99
        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "Growth" in page_text
        assert "$99" in page_text

        print("Growth plan is active")
        print("Growth price verified: $99/month")

        # Capture proof screenshot
        take_screenshot(
            driver,
            "subscription_plans_passed"
        )

    finally:
        driver.quit()