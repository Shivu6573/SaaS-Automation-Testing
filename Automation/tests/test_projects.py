from Automation.utils.driver_factory import get_driver
from Automation.utils.screenshot import take_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_projects_navigation():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saas.anointedcoder.com/app/projects")

        projects = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[normalize-space()='Projects']")
            )
        )

        assert projects.is_displayed()
        assert "/app/projects" in driver.current_url

        take_screenshot(driver, "projects_navigation_passed")

        print("Projects page opened successfully")
        print("Projects navigation verified")

    finally:
        driver.quit()