from Automation.utils.driver_factory import get_driver
from Automation.utils.screenshot import take_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_team_navigation():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saas.anointedcoder.com/app/team")

        team = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[normalize-space()='Team']")
            )
        )

        assert team.is_displayed()
        assert "/app/team" in driver.current_url

        take_screenshot(driver, "team_navigation_passed")

        print("Team page opened successfully")
        print("Team navigation verified")

    finally:
        driver.quit()