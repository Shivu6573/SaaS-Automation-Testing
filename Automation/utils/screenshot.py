import os


def take_screenshot(driver, name):
    os.makedirs("Automation/screenshots", exist_ok=True)

    driver.save_screenshot(
        f"Automation/screenshots/{name}.png"
    )