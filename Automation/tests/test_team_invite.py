from Automation.utils.driver_factory import get_driver
from Automation.utils.screenshot import take_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invite_member_form():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saas.anointedcoder.com/app/team")

        # Click Invite Member
        invite_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Invite Member')]")
            )
        )

        invite_button.click()

        # Wait for Invite Member form
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(normalize-space(), 'Invite Member')]")
            )
        )

        # Capture the successful form as proof
        take_screenshot(
            driver,
            "invite_member_form_passed"
        )

        print("Invite Member form opened successfully")
        print("Proof screenshot captured")

    finally:
        driver.quit()