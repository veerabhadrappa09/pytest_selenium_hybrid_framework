import pytest
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot

@pytest.mark.flaky(reruns=3)
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    if "Dashboard" in driver.current_url:
        take_screenshot(driver, "Login Failed")
        pytest.fail("Login failed")