from Automation.utils.driver_factory import get_driver
from Automation.utils.screenshot import take_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_settings_navigation():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saas.anointedcoder.com/app/settings")

        settings = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[normalize-space()='Settings']")
            )
        )

        assert settings.is_displayed()
        assert "/app/settings" in driver.current_url

        take_screenshot(
            driver,
            "settings_navigation_passed"
        )

        print("Settings page opened successfully")
        print("Proof screenshot captured")

    finally:
        driver.quit()