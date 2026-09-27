from Automation.utils.driver_factory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():

    driver = get_driver()
    driver.get("https://saas.anointedcoder.com/app/overview")

    overview = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[normalize-space()='Overview']")
        )
    )

    assert overview.is_displayed()
    assert driver.current_url == "https://saas.anointedcoder.com/app/overview"

    driver.quit()