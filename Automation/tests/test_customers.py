# from Automation.utils.driver_factory import get_driver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def test_customers_navigation():

#     driver = get_driver()
#     wait = WebDriverWait(driver, 10)

#     try:
#         # Open Customers
#         driver.get("https://saas.anointedcoder.com/app/customers")

#         # Verify Customers page
#         customers = wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//*[normalize-space()='Customers']")
#             )
#         )

#         assert customers.is_displayed()

#         # Verify URL
#         assert "/app/customers" in driver.current_url

#         print("Customers page opened successfully")
#         print("Customers navigation verified")

#     finally:
#         driver.quit()
from Automation.utils.driver_factory import get_driver
from Automation.utils.screenshot import take_screenshot

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_customers_navigation():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saas.anointedcoder.com/app/customers")

        customers = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[normalize-space()='Customers']")
            )
        )

        assert customers.is_displayed()
        assert "/app/customers" in driver.current_url

        take_screenshot(driver, "customers_navigation_passed")

        print("Customers page opened successfully")
        print("Customers navigation verified")

    finally:
        driver.quit()